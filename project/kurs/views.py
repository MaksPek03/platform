from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request, "kurs/index.html")
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "kurs/register.html", {"form": form})

def logging_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect("index")
    else: 
        form = AuthenticationForm()
    return render(request, 'kurs/logging.html', {"form": form})