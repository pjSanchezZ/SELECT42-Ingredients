from django.shortcuts import render
from django.http import HttpResponse
from pages.models import product_info
# Create your views here.

def homepage(request):
  return  render(request, 'navigate.html')

def search_test(request):
  search_content = request.GET.get('search_content')
  search_result = list(product_info.objects.filter(Product_Name__icontains=search_content).values()[:15])
  print(search_result)
<<<<<<< HEAD
  return render(request, 'search_result.html', {'content': search_result})
=======
  id = search_result[0]['Product_Name']
  return render(request, 'search_result.html',{'content': search_result})
>>>>>>> fa2a2b47e01b5ca9871e901b8848dbe894b4c66c