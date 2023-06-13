from django.urls import path, include
from .views import index,about,contact,post1,post2,post3,post4,current

urlpatterns = [
    path('index', index),
    path('about', about),
    path('current', current),
    path('contact', contact),
    path('post1', post1),
    path('post2', post2),
    path('post3', post3),
    path('post4', post4),
]
