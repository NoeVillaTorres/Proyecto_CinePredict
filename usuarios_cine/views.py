from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request,'index.html')


@login_required
def cines_page(request):
    return render(request, 'cine.html')

def exit(request):
    logout(request)
    return redirect('home')

