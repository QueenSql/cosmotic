from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Candle, RoomSpray

# Create your views here.
def index(request):
    return render(request, 'products/index.html')

@login_required
def candles(request):
    candles = Candle.objects.all()
    return render(request, 'products/candles.html', {'candles': candles})

@login_required
def room_sprays(request):
    room_sprays = RoomSpray.objects.all()
    return render(request, 'products/room_sprays.html', {'room_sprays': room_sprays})

def about(request):
    return render(request, 'products/about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page on successful registration
    else:
        form = UserCreationForm()
    return render(request, 'products/register.html', {'form': form})
