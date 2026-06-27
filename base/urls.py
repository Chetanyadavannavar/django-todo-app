from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('complete/',complete,name='complete'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),

    #homepage
    path('hcompleted/<int:pk>',hcompleted,name='hcompleted'),
    path('hdelete/<int:pk>',hdelete,name='hdelete'),

    #add
    path('add/', add, name='add'),

    # complete
    path('cdelete/<int:pk>',cdelete,name='cdelete'),
    path('crestore/<int:pk>',crestore,name='crestore'),

    # delete
    path('ddelete/<int:pk>',ddelete,name='ddelete'),
    path('drestore/<int:pk>',drestore,name='drestore'),

    path('hdelete_all/',hdelete_all,name='hdelete_all'),
    path('hcomplete_all/',hcomplete_all,name='hcomplete_all'),

    
]