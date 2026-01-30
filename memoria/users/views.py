from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def users(request):
    return render(request, 'users.html')

def profile(request):
    return render(request, 'profile.html')

def registration(request):
    return render(request, 'register.html')