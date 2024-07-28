from django.urls import path
from . import views
urlpatterns = [
    path("homepage", views.index, name="index"),
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")    
]
