from django.shortcuts import render
from django.http import HttpResponse
from pages.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from pages.forms import select_testform

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.

def home(request):
  return  render(request, 'home.html')

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
  return  render(request, 'signin.html', {'content': 102})

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

def ranger(request):
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

  # cxt = product_info.objects.filter(
  #     Product_Name__icontains='apple juice').values()
  # paginator = Paginator(cxt, 8)  # Show 10 contacts per page.
  paginator = Paginator(list_result, 8)  # Show 10 contacts per page.
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  print('Page:', page_number)

  return render(request, 'listing.html', {'page_obj': page_obj, 'content': list_result})


def listing_search(request):
  global list_result
  global list_content
  list_content = request.GET.get("list_key")
  list_result = product_info.objects.filter(Product_Name__icontains=list_content)
  print(list_content)
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
      if the user login in successfully, the website will jump to 'home.html'.
  """
  global username 
  username = request.GET.get("username")
  password = request.GET.get("password")
  print(username, password)
  if(username == '' or not (user.objects.filter(User_Name__exact = username))):
    return render(request, 'signin.html', {'content': 100})
  elif(password == '' or not user.objects.filter(User_Name__exact = username).filter(Password__exact = password)):
    return render(request, 'signin.html', {'content': 101})
  else:
    return render(request, 'home.html', {'content': 102})

def signup1(request):
  """
  This is the function for signup:
    Input from front-end:
      1. 'User_Name'
      2. 'Password1'
      3. 'Password2'
        - the password should be entered twice and they should match.
      4. 'Email'
      5. 'Phone_number'
    Output to front-end:
      1. 'Error':
        - 101: User name is too long, it should be less than 45 characters.
        - 102: User name already exists.
        - 103: Password is too short, it should be at least 8 characters.
        - 104: The 2 Passwords doesn't match
        - 105: Invalid phone number
        - 106: Invalid email
        - 0: Suceed:
          -- Store the user info to database
          -- auto log in with the newly created user.
          -- jump to \home.html.
  """
  global username
  name = request.GET.get('User_Name')
  password_1 = request.GET.get('Password1')
  password_2 = request.GET.get('Password2')
  email = request.GET.get('Email')
  Phone_number = request.GET.get('Phone_number')
  try:
    validate_email(email)
    email_valid = True
  except ValidationError:
    email_valid = False
  print(name, password_1, password_2, email, Phone_number)
  if name == '' or len(name) > 45:
    return render(request, 'signup.html', {'Error': 101})
  elif user.objects.filter(User_Name__exact = name):
    return render(request, 'signup.html', {'Error': 102})
  elif password_1 == '' or len(password_1) < 8:
    return render(request, 'signup.html', {'Error': 103})
  elif password_1 != password_2:
    return render(request, 'signup.html', {'Error': 104})
  elif Phone_number == '' or len(Phone_number) < 10 or len(Phone_number) > 15:
    return render(request, 'signup.html', {'Error': 105})
  elif email_valid == False:
    return render(request, 'signup.html', {'Error': 106})
  else:
    new_user = user(User_Name = name, Password = password_2, Email = email, Phone_Number = int(Phone_number))
    new_user.save()
    username = name
    return render(request, 'home.html', {'Error': 0})
  

def cart(request):
  """
  This is a function for displaying want is already in the cart
    Parameters:
      1. display_num: determine the num of items on every page.
      
    Output to front-end:
      1. Error: 
        - 100: the user hasn't log in yet, so the website will be redirected to the sign up page. But notations are needed.
    TODO:
      1. give some notations or signs if the user clicked on the cart button without logging in. Currently, if the user clicks on the cart button without logging in, the web will jump to sign up page, which is a bit weird and not user-friendly.
  """ 

  display_num = 10
  global username
  if username=='':
    return render(request, 'signin.html', {'Error': 100})
  # wanted_all is a list of dictionaries
  wanted_all = list(wanted_item.objects.filter(User_Name__exact = 'XutaoC').filter(Valid__exact = 1).values())
  sum_of_item = len(wanted_all)
  count_of_things = 0
  total_cost = 0
  product_list = []
  product_count_dict = {}
  product_cost_dict = {}
  for cart_item in wanted_all:
    product_list.append(cart_item['Product_Id_id'])
    product_count_dict[cart_item['Product_Id_id']] = cart_item['Quantity']
    product_cost_dict[cart_item['Product_Id_id']] = cart_item['Quantity']*cart_item['Price']
    count_of_things += cart_item['Quantity']
    total_cost += cart_item['Quantity']*cart_item['Price']
  # cart is a list of dictionaries
  cart = []
  for product in product_list:
    product_dict = list(product_info.objects.filter(Product_Id__exact = product).values())[0]
    product_dict['Total_Price'] = round(product_cost_dict[product],2)
    product_dict['Count'] = product_count_dict[product]
    cart.append(product_dict)  

  paginator = Paginator(cart, display_num)  # Show 10 contacts per page.
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  total_page = paginator.num_pages

  if page_number:
    page_number = (int)(page_number)
  
  return render(request, 'cart.html', {
      'user_name': username,
      'count_of_items': sum_of_item, 
      'count_of_things': count_of_things,
      # 'info_of_item': list_result,
      'sum_of_item': round(total_cost, 2),
      'page_obj': page_obj,
      'curr_page': page_number,
      'total_page': total_page,
      'range': paginator.page_range
      })


def try_search(request):

  # quantity = request.GET.get("quantity")

  # print(quantity)

  global username
  # if username=='':
  #   return render(request, 'signin.html', {'Error': 100})
  # wanted_all = wanted_item.objects.filter(User_Name__exact = username).filter(Valid__exact = 1).values()
  # print(list(wanted_all))
  list_result = product_info.objects.filter(
      Product_Name__icontains='apple juice').values()
  
  paginator = Paginator(list_result, 10)  # Show 10 contacts per page.

  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  total_page = paginator.num_pages
  # print(page_obj.count, ', ', page_number, '/', total_page)

  if page_number:
    page_number = (int)(page_number)  # page_number本来是string型

  return render(request, 'try.html', {
        'page_obj': page_obj,
        'curr_page': page_number,
        'total_page': total_page,
        'range': paginator.page_range,
        'quantity': quantity
        })


class testview(View):
  def get(self, request):
    select_form = select_testform()
    return render(request, 'try.html',{
      'select_form': select_form,
    })

  def post(self, request):
    select_form = select_testform(request.POST)
    if select_form.is_valid():
      get_value = request.POST.get('sel_value', "")
      print(get_value)
      print(1)
    else:
      print("wrong")
    
  

