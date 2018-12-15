from django.shortcuts import render
from .forms import DonateFood


def denote(request):
    if request.method == "POST":
        form = DonateFood(request.POST)
    

    else:
        form = DonateFood()
        return render(request, 'donation.html' , {'form' : form })
