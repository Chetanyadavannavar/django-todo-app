from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile


# Login
def login_(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Incorrect username or password.")
            return render(request, "login_.html")

    return render(request, "login_.html")


# Register
def register(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "register.html")

        User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=fname,
            last_name=lname
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect("login_")

    return render(request, "register.html")


# Profile
@login_required(login_url="login_")
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    return render(request, "profile.html", {"profile": profile})


# Update Profile
@login_required(login_url="login_")
def update_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        user.first_name = request.POST.get("fname")
        user.last_name = request.POST.get("lname")
        user.email = request.POST.get("email")
        user.save()

        pic = request.FILES.get("pic")
        if pic:
            profile.profile_pic = pic
            profile.save()

        messages.success(request, "Profile updated successfully.")
        return redirect("profile")

    return render(request, "update_profile.html", {"data": user})


# Logout
@login_required(login_url="login_")
def logout_(request):
    logout(request)
    return redirect("login_")


# Reset Password
@login_required(login_url="login_")
def rest_pass(request):
    user = request.user

    if request.method == "POST":

        if "oldpasw" in request.POST:
            old_pass = request.POST.get("oldpasw")

            auth_user = authenticate(
                request,
                username=user.username,
                password=old_pass
            )

            if auth_user:
                return render(request, "rest_pass.html", {"new_pass": True})
            else:
                messages.error(request, "Old password is incorrect.")
                return render(request, "rest_pass.html")

        if "newpasw" in request.POST:
            new_pass = request.POST.get("newpasw")

            if user.check_password(new_pass):
                messages.error(request, "New password cannot be the same as the old password.")
                return render(request, "rest_pass.html")

            user.set_password(new_pass)
            user.save()

            messages.success(request, "Password changed successfully.")
            return redirect("login_")

    return render(request, "rest_pass.html")


# Forget Password
def forget_pass(request):
    if request.method == "POST":
        username = request.POST.get("username")

        try:
            user = User.objects.get(username=username)
            request.session["fp_user"] = user.username
            return redirect("new_password")
        except User.DoesNotExist:
            messages.error(request, "Username not found.")
            return render(request, "forget_pasw.html")

    return render(request, "forget_pasw.html")


# New Password
def new_password(request):
    username = request.session.get("fp_user")

    if username is None:
        return redirect("forget_pass")

    user = User.objects.get(username=username)

    if request.method == "POST":
        new_pass = request.POST.get("password")

        if user.check_password(new_pass):
            messages.error(request, "New password cannot be the same as the old password.")
            return render(request, "new_passw.html")

        user.set_password(new_pass)
        user.save()

        del request.session["fp_user"]

        messages.success(request, "Password changed successfully.")
        return redirect("login_")

    return render(request, "new_passw.html")