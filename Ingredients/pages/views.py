from django.shortcuts import render
from django.http import HttpResponse
from pages.models import product_info
# Create your views here.

def homepage(request):
  return  render(request, 'navigate.html')

def search_test(request):
  search_content = request.GET.get('search_content')
  search_result = list(product_info.objects.filter(Product_Name__icontains=search_content).values())
  print(search_result)
  return render(request, 'search_result.html',)