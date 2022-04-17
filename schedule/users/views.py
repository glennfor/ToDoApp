from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # only redirect when the POST is successful
            return redirect('/home')  # 🖘 use the name of a view
    else:
        form = RegisterForm() # no form.save()
    return render(request, 'users/register.html', {'form': form})
