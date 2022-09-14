from django.shortcuts import render

# Create your views here.

def home(requeste):
    return render(requeste,'home.html', {})
