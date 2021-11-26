from django.shortcuts import render
from django.http import HttpResponse
from pages.models import *
# Create your views here.

def home(request):
  print("home:"+str(request.GET))
  return  render(request, 'home.html')

def cart(request):
  print("cart:"+str(request.GET))
  return  render(request, 'cart.html')

def change_password(request):
  print("change_password:"+str(request.GET))
  return  render(request, 'change_password.html')

def checkout(request):
  print("checkout:"+str(request.GET))
  return  render(request, 'checkout.html')

def deactivate_account(request):
  print("deactivate_account:"+str(request.GET))
  return  render(request, 'deactivate_account.html')

def faq(request):
  print("faq:"+str(request.GET))
  return  render(request, 'faq.html')

def fresh_vegan(request):
  print("fresh_vegan:"+str(request.GET))
  return  render(request, 'fresh_vegan.html')

def help_support(request):
  print("help_support:"+str(request.GET))
  return  render(request, 'help_support.html')

def listing(request):
  print("listing:"+str(request.GET))
  return  render(request, 'listing.html')

def my_account(request):
  print("my_account:"+str(request.GET))
  return  render(request, 'my_account.html')

def my_address(request):
  print("my_address:"+str(request.GET))
  return  render(request, 'my_address.html')

def my_order(request):
  print("my_order:"+str(request.GET))
  return  render(request, 'my_order.html')

def picks_today(request):
  print("picks_today:"+str(request.GET))
  return  render(request, 'picks_today.html')

def privacy(request):
  print("privacy:"+str(request.GET))
  return  render(request, 'privacy.html')

def product_details(request):
  print("product_details:"+str(request.GET))
  return  render(request, 'product_details.html')

def promo_details(request):
  print("promo_details:"+str(request.GET))
  return  render(request, 'promo_details.html')

def promos(request):
  print("promos:"+str(request.GET))
  return  render(request, 'promos.html')

def recommend(request):
  print("recommend:"+str(request.GET))
  return  render(request, 'recommend.html')

def refund_payment(request):
  print("refund_payment:"+str(request.GET))
  return  render(request, 'refund_payment.html')

def review(request):
  print("review:"+str(request.GET))
  return  render(request, 'review.html')

def search(request):
  print("search:"+str(request.GET))
  return  render(request, 'search.html')

def signin(request):
  print("signin:"+str(request.GET))
  return  render(request, 'signin.html')

def signup(request):
  print("signup:"+str(request.GET))
  return  render(request, 'signup.html')

def status_canceled(request):
  print("status_canceled:"+str(request.GET))
  return  render(request, 'status_canceled.html')

def status_complete(request):
  print("status_complete:"+str(request.GET))
  return  render(request, 'status_complete.html')

def status_onprocess(request):
  print("status_onprocess:"+str(request.GET))
  return  render(request, 'status_onprocess.html')

def successful(request):
  print("successful:"+str(request.GET))
  return  render(request, 'successful.html')

def terms_conditions(request):
  print("terms_conditions:"+str(request.GET))
  return  render(request, 'terms_conditions.html')

def terms_and_conditions(request):
  print("terms_and_conditions:"+str(request.GET))
  return  render(request, 'terms&conditions.html')

def verification(request):
  print("verification:"+str(request.GET))
  return  render(request, 'verification.html')

def search_test(request):
  print("search_test:"+str(request.GET))
  search_content = request.GET.get("search_key")
  # print(search_content)
  search_result = list(product_info.objects.filter(Product_Name__icontains=search_content).values())
  # search_result = [{'Product_Id': '101484506', 'Product_Name': 'Granny Smith Apple', 'Price': 0.99, 'Type_Id': '54\r', 'Seller_Id': 'Schnucks2', 'Description': 'Apples', 'Image': 'https://storage.cloud.google.com/select_42/product_img/101484506.png'}, {'Product_Id': '10771038646', 'Product_Name': 'Good & Gather Passion Fruit Pineapple Chunks, Dragon Fruit Chunks, Passion Fruit Juice & Mango Puree Blended Cubes Tropical Blend', 'Price': 4.99, 'Type_Id': '73\r', 'Seller_Id': 
# 'Target0', 'Description': 'Ingredients,Pineapple, Dragon Fruit, Passion Fruit Juice, Mango Puree.', 'Image': 'https://storage.cloud.google.com/select_42/product_img/10771038646.png'}]
  return render(request, 'search.html', {'content': search_result})

list_result = []
list_content =''

def range(request):
  print("range:"+str(request.GET));
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
  print("relavantt:"+relavant)
  flag = 0
  #print(min_value)

  if store1 != '1' and store2 != '1' and store3 != '1':

    flag = 1

  else:

    if relavant =='yes':
      #print('jinqu')
      list_result1 = product_type.objects.filter(Product_Type__startswith = list_content).values()[:1]
      list_result1 = list(list_result1)
      list_result = list_result&product_info.objects.filter(Type_Id__exact = list_result1[0]['Type_Id'])
      print(list_result1[0]['Type_Id'])
      # product_type.objects.raw('SELECT * FROM pages_product_info NATURAL JOIN pages_product_type WHERE ')
   
      if store1 == '1':
        # list_result = list_result.filter(Seller_Id__icontains='ALDI')
        list_result =  list_result|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='ALDI')
      if store2 == '1':
        list_result =  list_result|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='Schnucks')
      if store3 == '1':
        list_result =  list_result|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='Costco')
    else:
      if store1 == '1':
        # list_result = list_result.filter(Seller_Id__icontains='ALDI')
        list_result = list_result|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='ALDI')
      if store2 == '1':
        list_result =  list_resul|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='Schnucks')
      if store3 == '1':
        list_result =  list_result|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='Costco')
    
  if min_value and flag!=1:
    list_result = list_result & product_info.objects.filter(Price__gte= float(min_value))
  if max_value and flag!=1:
    list_result = list_result & product_info.objects.filter(Price__lte= float(max_value))

  if order == '1' and flag!=1:
    list_result = list_result.order_by('Product_Name').values()
  elif order == '2'and flag!=1:
    list_result = list_result.order_by('-Product_Name').values()
  elif order == '3'and flag!=1:
    list_result = list_result.order_by('-Price').values()
  elif order == '4'and flag!=1:
    list_result = list_result.order_by('Price').values()
  
#   search_result = [{'Product_Id': '101484506', 'Product_Name': 'Granny Smith Apple', 'Price': 0.99, 'Type_Id': '54\r', 'Seller_Id': 'Schnucks2', 'Description': 'Apples', 'Image': 'https://storage.cloud.google.com/select_42/product_img/101484506.png'}, {'Product_Id': '10771038646', 'Product_Name': 'Good & Gather Passion Fruit Pineapple Chunks, Dragon Fruit Chunks, Passion Fruit Juice & Mango Puree Blended Cubes Tropical Blend', 'Price': 4.99, 'Type_Id': '73\r', 'Seller_Id': 
# 'Target0', 'Description': 'Ingredients,Pineapple, Dragon Fruit, Passion Fruit Juice, Mango Puree.', 'Image': 'https://storage.cloud.google.com/select_42/product_img/10771038646.png'}]
  #print("hqd:" + str(type(list_result)))
  return render(request, 'listing.html', {'content': list(list_result)})


def list_test(request):
  print("list_test:"+str(request.GET))
  global list_result
  global list_content
  list_content = request.GET.get("list_key")
  list_result = product_info.objects.filter(Product_Name__icontains=list_content)
  print(list_content)
  # print(343)
  return render(request, 'listing.html', {'content': list(list_result.values())})

def details(request):
  print("details:"+str(request.GET))
  pro = request.GET.get("pro")
  # print(pro)
  search_result = [{'Product_Id': '101484506', 'Product_Name': 'Granny Smith Apple', 'Price': 0.99, 'Type_Id': '54\r', 'Seller_Id': 'Schnucks2', 'Description': 'Apples', 'Image': 'https://storage.cloud.google.com/select_42/product_img/101484506.png'}, {'Product_Id': '10771038646', 'Product_Name': 'Good & Gather Passion Fruit Pineapple Chunks, Dragon Fruit Chunks, Passion Fruit Juice & Mango Puree Blended Cubes Tropical Blend', 'Price': 4.99, 'Type_Id': '73\r', 'Seller_Id': 
'Target0', 'Description': 'Ingredients,Pineapple, Dragon Fruit, Passion Fruit Juice, Mango Puree.', 'Image': 'https://storage.cloud.google.com/select_42/product_img/10771038646.png'}]
  return render(request, 'product_details.html', {'content': search_result})