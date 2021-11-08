from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display_img(request):
  return render(request, 'displaytest.html')

