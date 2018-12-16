from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import requests
<<<<<<< HEAD

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    url = "https://api.backbuckle.io/v1/users/a31775d0-0078-11e9-afa7-03a269ea2160"
    payload = "{\"country_code\":\"+1\",\"default_location\":{\"latitude\":0,\"longitude\":0},\"dob\":\"1992-01-14\",\"email\":\"dev@backbuckle.io\",\"first_name\":\"Shoaib\",\"gender\":\"MALE\",\"last_name\":\"Mohammed\",\"password\":\"backbuckle123\",\"phone_number\":2025550192,\"properties\":{\"key-1\":\"property-1\",\"key-2\":\"property-2\"},\"tags\":{\"key-1\":\"property-1\",\"key-2\":\"property-2\"},\"time_zone\":\"UTC -5\",\"user_customer_id\":\"2010C6PS627G\",\"user_name\":\"shoaib627\"}"
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", url, data=payload, headers=headers)

class Location(request):
    url = "https://api.backbuckle.io/v1/users/search/"
    payload = "[\n{\n\"operation_type\":\"GEO_DISTANCE_MAX\",\n\"attribute_type\":\"default_location\",\n\"values\":[\n{\n\"geo_point\":{\n\"longitude\": \"77.6974\",\n\"latitude\":\"12.9592\"\n},\n\"max_distance\": 6\n}\n]\n}\n]"
    headers = {
    'Authorization': "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoiOGI3N2I2ZDAtZmZjYy0xMWU4LWI4ZjgtN2YwMWMwNjdiZTlhIiwicHJvamVjdF9pZCI6ImNjMWU2ODQwLWZmZDItMTFlOC1iOGY4LTdmMDFjMDY3YmU5YSIsImVudmlyb25tZW50X2lkIjoiY2MyMDhiMjAtZmZkMi0xMWU4LWI4ZjgtN2YwMWMwNjdiZTlhIiwiZGltZW5zaW9uX2lkIjoiY2MyZDgzNzAtZmZkMi0xMWU4LWI4ZjgtN2YwMWMwNjdiZTlhIiwiYXBpX2FjY2Vzc19sZXZlbCI6IlNFUlZFUiIsImtleV9pZCI6ImNjM2EyZGEwLWZmZDItMTFlOC1iOGY4LTdmMDFjMDY3YmU5YSIsImlzcyI6Im9qNldGaW9OR2RuQktDM1gyN1ZRWktZMHVOTVRWckhCIiwiaWF0IjoxNTQ0ODE0MTQ3fQ.5cb3mqoJzL7tofndcmwhVI6HbgQX7Ze7otYw6Dj3M9A",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "85360ea8-5221-4c05-9d8d-b9bf7aa0dab3"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    location = request.
=======
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
                url = "https://api.backbuckle.io/v1/users/a31775d0-0078-11e9-afa7-03a269ea2160"
                payload = {"country_code": "+91","default_location": {"latitude": 0,"longitude": 0  }, "dob": "","email": "",  "first_name": form.first_name,  "gender":"",  "last_name":form.last_name ,"password":form.password1,  "phone_number": form.phone,"time_zone": "Asia/Kolkata",  "user_customer_id": "","user_name": "Idly"}
                headers = {'content-type': 'application/json'}
                response = requests.request("POST", url, data=payload, headers=headers)
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
def Donate(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=forms.DonateFood(request.POST)
            if form.is_valid():
                form.save()
                url = "https://api.backbuckle.io/v1/users/"
                payload = {"country_code": "+91","default_location": {"latitude": 0,"longitude": 0  }, "dob": "","email": "",  "first_name": "",  "gender":"",  "last_name":"" ,"password":"",  "phone_number":"","time_zone": "Asia/Kolkata",  "user_customer_id": "","user_name": "Idly","properties":{"DOE":"","DOM":"","Quantity":""}}
                headers = {
                'Authorization': "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoiOGI3N2I2ZDAtZmZjYy0xMWU4LWI4ZjgtN2YwMWMwNjdiZTlhIiwicHJvamVjdF9pZCI6ImNjMWU2ODQwLWZmZDItMTFlOC1iOGY4LTdmMDFjMDY3YmU5YSIsImVudmlyb25tZW50X2lkIjoiY2MyMDhiMjAtZmZkMi0xMWU4LWI4ZjgtN2YwMWMwNjdiZTlhIiwiZGltZW5zaW9uX2lkIjoiY2MyZDgzNzAtZmZkMi0xMWU4LWI4ZjgtN2YwMWMwNjdiZTlhIiwiYXBpX2FjY2Vzc19sZXZlbCI6IlNFUlZFUiIsImtleV9pZCI6ImNjM2EyZGEwLWZmZDItMTFlOC1iOGY4LTdmMDFjMDY3YmU5YSIsImlzcyI6Im9qNldGaW9OR2RuQktDM1gyN1ZRWktZMHVOTVRWckhCIiwiaWF0IjoxNTQ0ODE0MTQ3fQ.5cb3mqoJzL7tofndcmwhVI6HbgQX7Ze7otYw6Dj3M9A",
                'Content-Type': "application/json",
                'cache-control': "no-cache",
                'Postman-Token': "46bce5c4-b1ed-41b6-9d8e-fefed0b8461d"
                }
                response = requests.request("POST", url, data=payload, headers=headers)
>>>>>>> c68f3deee986dd87762feaca875fe1f7a32b4418
