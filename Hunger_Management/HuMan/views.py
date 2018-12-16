from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import requests

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    url = "https://api.backbuckle.io/v1/users/a31775d0-0078-11e9-afa7-03a269ea2160"
    payload = "{\"country_code\":\"+1\",\"default_location\":{\"latitude\":0,\"longitude\":0},\"dob\":\"1992-01-14\",\"email\":\"dev@backbuckle.io\",\"first_name\":\"Shoaib\",\"gender\":\"MALE\",\"last_name\":\"Mohammed\",\"password\":\"backbuckle123\",\"phone_number\":2025550192,\"properties\":{\"key-1\":\"property-1\",\"key-2\":\"property-2\"},\"tags\":{\"key-1\":\"property-1\",\"key-2\":\"property-2\"},\"time_zone\":\"UTC -5\",\"user_customer_id\":\"2010C6PS627G\",\"user_name\":\"shoaib627\"}"
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", url, data=payload, headers=headers)
