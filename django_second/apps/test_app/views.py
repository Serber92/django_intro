from django.shortcuts import render, HttpResponse, redirect
def pidr(request):
  return HttpResponse("Idi nah pidrila")

def gnida(request):
  return HttpResponse("Ti suka gnida")

def create(request):
  return redirect('/')

def show(request, number):
  return HttpResponse("Shob ti zdoh " + number + " raz")

def edit(request, number):
  return HttpResponse("Sosi huy blia   ...   " + number)

def destroy(request, number):
  return HttpResponse("ti prosto dibil, idi ubeisia " + number + "raz")

# Create your views here.
