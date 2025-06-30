from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Candle, RoomSpray

# Create your views here.

def index(request):
    """
    Renders the homepage of the site.
    """
    return render(request, 'products/index.html')


@login_required
def candles(request):
    """
    Displays a list of available candle products.
    """
    candles = Candle.objects.all()
    return render(request, 'products/candles.html', {'candles': candles})


@login_required
def room_sprays(request):
    """
    Displays a list of available room spray products.
    """
    room_sprays = RoomSpray.objects.all()
    return render(request, 'products/room_sprays.html', {'room_sprays': room_sprays})


def about(request):
    """
    Renders the about page with company information.
    """
    return render(request, 'products/about.html')


def register(request):
    """
    Handles user registration using Django's built-in UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page on successful registration
    else:
        form = UserCreationForm()
    return render(request, 'products/register.html', {'form': form})
