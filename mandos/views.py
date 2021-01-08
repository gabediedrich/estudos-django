from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return(render(request, "mandos/home.html", content_type='text/html'))