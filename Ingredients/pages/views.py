from django.shortcuts import render
from django.http import HttpResponse
from pages.models import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.

def home(request):
  return  render(request, 'home.html')

def cart(request):
  return  render(request, 'cart.html')

def change_password(request):
  return  render(request, 'change_password.html')

def checkout(request):
  return  render(request, 'checkout.html')

def deactivate_account(request):
  return  render(request, 'deactivate_account.html')

def faq(request):
  return  render(request, 'faq.html')

def fresh_vegan(request):
  return  render(request, 'fresh_vegan.html')

def help_support(request):
  return  render(request, 'help_support.html')

def listing(request):
  return  render(request, 'listing.html')

def my_account(request):
  return  render(request, 'my_account.html')

def my_address(request):
  return  render(request, 'my_address.html')

def my_order(request):
  return  render(request, 'my_order.html')

def picks_today(request):
  return  render(request, 'picks_today.html')

def privacy(request):
  return  render(request, 'privacy.html')

def product_details(request):
  return  render(request, 'product_details.html')

def promo_details(request):
  return  render(request, 'promo_details.html')

def promos(request):
  return  render(request, 'promos.html')

def recommend(request):
  return  render(request, 'recommend.html')

def refund_payment(request):
  return  render(request, 'refund_payment.html')

def review(request):
  return  render(request, 'review.html')

def search(request):
  return  render(request, 'search.html')

def signin(request):
  return  render(request, 'signin.html')

def signup(request):
  return  render(request, 'signup.html')

def status_canceled(request):
  return  render(request, 'status_canceled.html')

def status_complete(request):
  return  render(request, 'status_complete.html')

def status_onprocess(request):
  return  render(request, 'status_onprocess.html')

def successful(request):
  return  render(request, 'successful.html')

def terms_conditions(request):
  return  render(request, 'terms_conditions.html')

def terms_and_conditions(request):
  return  render(request, 'terms&conditions.html')

def verification(request):
  return  render(request, 'verification.html')

def search_test(request):
  search_content = request.GET.get("search_key")
  # print(search_content)
  search_result = list(product_info.objects.filter(Product_Name__icontains=search_content).values())
  # search_result = [{'Product_Id': '101484506', 'Product_Name': 'Granny Smith Apple', 'Price': 0.99, 'Type_Id': '54\r', 'Seller_Id': 'Schnucks2', 'Description': 'Apples', 'Image': 'https://storage.cloud.google.com/select_42/product_img/101484506.png'}, {'Product_Id': '10771038646', 'Product_Name': 'Good & Gather Passion Fruit Pineapple Chunks, Dragon Fruit Chunks, Passion Fruit Juice & Mango Puree Blended Cubes Tropical Blend', 'Price': 4.99, 'Type_Id': '73\r', 'Seller_Id': 
# 'Target0', 'Description': 'Ingredients,Pineapple, Dragon Fruit, Passion Fruit Juice, Mango Puree.', 'Image': 'https://storage.cloud.google.com/select_42/product_img/10771038646.png'}]
  return render(request, 'search.html', {'content': search_result})

list_result = []
list_content =''

def range(request):
  min_value = request.GET.get("min_value")
  max_value = request.GET.get("max_value")
  order = request.GET.get("order")
  relavant = request.GET.get("relavant")
  store1 = request.GET.get("ALDI")
  store2 = request.GET.get("Schnucks")
  store3 = request.GET.get("Costco")
  # print(234134)
  # print(relavant, store1, store2, store3, order, min_value, max_value)
  global list_result
  global list_content
  table = seller.objects.filter(Seller_Id__icontains='cxtnb')
  list_result= table.none()
  print(relavant)
  if relavant =='yes':
    print('jinqu')
    list_result1 = product_type.objects.filter(Product_Type__startswith = list_content).values()[:1]
    list_result1 = list(list_result1)
    list_result = product_info.objects.filter(Type_Id__exact = list_result1[0]['Type_Id'])
    print(list_result1[0]['Type_Id'])
    # product_type.objects.raw('SELECT * FROM pages_product_info NATURAL JOIN pages_product_type WHERE ')
  else:
    if store1 == '1':
      # list_result = list_result.filter(Seller_Id__icontains='ALDI')
      list_result = list_result | product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='ALDI')
    if store2 == '1':
      list_result = list_result | product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='Schnucks')
    if store3 == '1':
      list_result = list_result | product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='Costco')
    
    if min_value:
      list_result = list_result & product_info.objects.filter(Price__gte= min_value)
    if max_value:
      list_result = list_result & product_info.objects.filter(Price__lte= max_value)

  if order == '1':
    list_result = list_result.order_by('Product_Name').values()
  elif order == '2':
    list_result = list_result.order_by('-Product_Name').values()
  elif order == '3':
    list_result = list_result.order_by('-Price').values()
  elif order == '4':
    list_result = list_result.order_by('Price').values()
  
#   search_result = [{'Product_Id': '101484506', 'Product_Name': 'Granny Smith Apple', 'Price': 0.99, 'Type_Id': '54\r', 'Seller_Id': 'Schnucks2', 'Description': 'Apples', 'Image': 'https://storage.cloud.google.com/select_42/product_img/101484506.png'}, {'Product_Id': '10771038646', 'Product_Name': 'Good & Gather Passion Fruit Pineapple Chunks, Dragon Fruit Chunks, Passion Fruit Juice & Mango Puree Blended Cubes Tropical Blend', 'Price': 4.99, 'Type_Id': '73\r', 'Seller_Id': 
# 'Target0', 'Description': 'Ingredients,Pineapple, Dragon Fruit, Passion Fruit Juice, Mango Puree.', 'Image': 'https://storage.cloud.google.com/select_42/product_img/10771038646.png'}]
  return render(request, 'listing.html', {'content': list(list_result)})

def list_test(request):
  global list_result
  global list_content
  list_content = request.GET.get("list_key")
  list_result = product_info.objects.filter(Product_Name__icontains=list_content)
  print(list_content)
  # print(343)
  return render(request, 'listing.html', {'content': list(list_result.values())})

def details(request):
  pro = request.GET.get("pro")
  # print(pro)
  search_result = [{'Product_Id': '101484506', 'Product_Name': 'Granny Smith Apple', 'Price': 0.99, 'Type_Id': '54\r', 'Seller_Id': 'Schnucks2', 'Description': 'Apples', 'Image': 'https://storage.cloud.google.com/select_42/product_img/101484506.png'}, {'Product_Id': '10771038646', 'Product_Name': 'Good & Gather Passion Fruit Pineapple Chunks, Dragon Fruit Chunks, Passion Fruit Juice & Mango Puree Blended Cubes Tropical Blend', 'Price': 4.99, 'Type_Id': '73\r', 'Seller_Id': 
'Target0', 'Description': 'Ingredients,Pineapple, Dragon Fruit, Passion Fruit Juice, Mango Puree.', 'Image': 'https://storage.cloud.google.com/select_42/product_img/10771038646.png'}]
  return render(request, 'product_details.html', {'content': search_result})

username = ''

def login(request):
  """
  This is the function for login.
    Input from front-end:
      1. 'User_Name'
      2. 'Password'
    Output to front-end:
      1. 'content':
        - if the user name can't be found, return content = 100
        - if the user name can be found, but the password is incorrect, return content = 101
        - login succeeded, return content = 102.
    TO BE DETERMINED:
      if the user login in successfully, the website will jump to 'TBD.html'.
  """
  global username 
  username = request.GET.get("username")
  password = request.GET.get("password")
  print(username, password)
  if(not (user.objects.filter(User_Name__exact = username))):
    return render(request, 'signin.html', {'content': 100})
  elif(not user.objects.filter(User_Name__exact = username).filter(Password__exact = password)):
    return render(request, 'signin.html', {'content': 101})
  else:
    return render(request, 'home.html', {'content': 102})

