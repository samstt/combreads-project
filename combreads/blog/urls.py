from . import views
from django.urls import path

urlpatterns = [
    path("", views.blogpage, name ="blogpage"),
    path('<slug:slug>/', views.post_detail, name ='post_detail'),
    path('addpost', views.add_post, name='add_post'),
]