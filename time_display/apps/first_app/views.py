from django.shortcuts import render, redirect
from time import gmtime, strftime

def index(request):
  return render(request, 'first_app/index.html')

def display_time(request):
  context = {
    "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  return render(request, 'first_app/display_time.html', context)

def word_generator(request):
  import string
  import random
  word = ''
  if 'counter' not in request.session:
    request.session['counter'] = 0
  for counter in range(15):
    word += random.choice(string.ascii_letters)
  context = {
      'word': word
  }
  return render(request, 'first_app/word_generator.html', context)

def process(request):
  if 'counter' not in request.session:
    request.session['counter'] = 0
  else:
    request.session['counter'] += 1
  return redirect('/word_generator')

# Create your views here.
