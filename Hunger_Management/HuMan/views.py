from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import requests
from . import models
from django.shortcuts import render,redirect
from . import forms
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
def signup(request):
    if request.user.is_authenticated:
        return HttpResponse("you are already logged in")
    else:
        if request.method == 'POST':
            form = forms.Register(request.POST)
            if form.is_valid():
                form.save()
                models.Otherdetail(
                user=User.objects.get(username=form.cleaned_data.get('username')),
                phone=form.cleaned_data.get('phone'),
                ).save()
                return HttpResponse("user saved")
            else:
                return render(request, 'signup.html', {'form': form})
        else:
            form = forms.Register()
        return render(request, 'signup.html', {'form': form})
def user_login(request):
    if request.user.is_authenticated:
        return HttpResponse("You have already logged in :)")
    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            member=User.objects.get(username=request.POST['username'])
            if user is not None:
                if user.is_active:
                    request.session['User_id']=member.id
                    login(request, user)
                    return render(request,'loggedin.html')
                else:
                    return render(request,'login.html',{'err':'Your account is not active at the moment please contact the Administration'})
            else:
                return render(request,'login.html',{'err':'Please enter your Authenticated credentials'})
        else:
            return render(request,'login.html',{'err':''})
def user_logout(request):
    if not request.user.is_authenticated:
        return HttpResponse("You have already logged out :)")
    else:
        logout(request)
        return HttpResponse("You have successfully logged out :)")
