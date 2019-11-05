from django.shortcuts import render, HttpResponse

def index(request):
  return HttpResponse("generate word")

# Create your views here.
