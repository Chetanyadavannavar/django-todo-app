from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   

    def __str__(self):
        # return self.title
        return f"{self.title} - {self.desc}"
    