from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render   # Added for this step
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "BirdBuddy/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Stream Processor",
            'message' : "Please select input file",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "BirdBuddy/about.html",
        {
            'title' : "About WildlifeWatcher",
            'content' : "An AI powered wildlife camera"
        }
    )

def home(request):
    return render(
        request,
        "BirdBuddy/home.html",
        {
            'title' : "Home Page",
            'content' : "Input"
        }
    )