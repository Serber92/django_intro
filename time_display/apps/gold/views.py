from django.shortcuts import render, redirect
import random

def index(request):
  if 'gold' not in request.session:
    request.session['gold'] = 0
  if 'history' not in request.session:
    request.session['history'] = ''
  context = {
    "locations": [
      ['Gendel', 'Get money from drunk people'],
      ['Lombard', 'Sell staff at lombard'],
      ['Bank', 'Rob the Bank'],
      ['Casino', 'Take chances']
    ]
  }
  return render(request, 'gold/gold.html', context)

def process_gold(request):
  if request.POST['which_form'] == "Gendel":
    gold = random.randint(0,40)
  elif request.POST['which_form'] == "Lombard":
    gold = random.randint(10, 20)
  elif request.POST['which_form'] == "Bank":
    gold = random.randint(-100, 100)
  elif request.POST['which_form'] == "Casino":
    gold = random.randint(-400, 200)
  request.session['gold'] += gold

  if gold > 0:
    request.session['history'] = "<p class='earn'>Got " + str(gold) + " from " + request.POST['which_form'] + "</p>" + request.session['history']
  else:
    request.session['history'] = "<p class='lost'>Lost " + str(gold) + " from " + request.POST['which_form'] + "</p>" + request.session['history']
  return redirect('/gold_app')

def reset(request):
  request.session.clear()
  return redirect('/gold_app')

  


# Create your views here.
