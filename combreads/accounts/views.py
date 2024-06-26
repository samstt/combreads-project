from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "accounts/signup.html")


def signup_view(request):
     if request.method != 'POST':
        form = UserCreationForm()
     else:
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('login')
         
     context = {'form' : form}

     return render(request, 'accounts/signup.html', context)
    