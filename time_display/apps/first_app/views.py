from django.shortcuts import render
from time import gmtime, strftime

def index(request):
  return render(request, 'first_app/index.html')

def display_time(request):
  context = {
    "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  return render(request, 'first_app/display_time.html', context)

# Create your views here.
