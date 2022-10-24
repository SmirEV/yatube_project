# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group_list),
    path('group/<gr>/', views.group_posts)
]
