from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
  return  render(request, 'navigate.html')

def search_test(request):
  return render(request, 'search_result.html',)