from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("http://127.0.0.1:5500/Construction_Week_Project/index.html")
    else:
        form = SignUpForm
    return render(request, "acko/sign_up.html", {"form":form})

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect("http://127.0.0.1:5500/Construction_Week_Project/logged_in.html")
    else:
        form = AuthenticationForm
    return render(request, "acko/login.html", {"form":form})

def log_out(request):
    if request.method == "POST":
        logout(request)
        return redirect("http://127.0.0.1:5500/Construction_Week_Project/index.html")
    else:
        return render(request, "acko/logout.html")
