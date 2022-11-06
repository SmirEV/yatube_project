# posts/urls.py
from django.urls import path

from . import views

app_name = 'posts'
#namespace='posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group_list),
    #path('group/<slug>/', views.group_posts)
    path('group/<slug:slug>/', views.group_posts, name='group_list')
]