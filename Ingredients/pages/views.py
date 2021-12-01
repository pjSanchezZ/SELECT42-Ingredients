from django.shortcuts import render
from django.http import HttpResponse
from pages.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from pages.forms import select_testform

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.

temp_list_result = None

def home(request):
  print("home:"+str(request.GET))
  return  render(request, 'home.html')

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

def product_details(request, productid = ''):
  flag1 = 0
  flag2 = 0
  product_Name = ''
  price = -1.0
  description = ''
  image = ''
  calories = ''
  total_Fat = ''
  saturated_Fat = ''
  transfat = ''
  cholesterol = ''
  sodium = ''
  total_Carbohydrate = ''
  protein = ''
  print("product_details:"+str(request.GET))
  table = seller.objects.filter(Seller_Id__icontains='cxtnb')
  list_result = table.none()
  nutrition_result = table.none()
  list_result = product_info.objects.filter(Product_Id__icontains = productid).values()
  if list_result:
    print('product_details: list_result[0]:'+str(list_result[0]))
    flag1 = 1
    product_Name = list_result[0]['Product_Name']
    price = list_result[0]['Price']
    description = list_result[0]['Description']
    image = list_result[0]['Image']
    nutrition_result = nutrition_table.objects.filter(Product_Name__icontains=product_Name).values()
    if nutrition_result:
      print('product_details: nutrition_result[0]:'+str(nutrition_result[0]))
      flag2 = 1
      calories = nutrition_result[0]['Calories']
      total_Fat = nutrition_result[0]['Total_Fat']
      saturated_Fat = nutrition_result[0]['Saturated_Fat']
      transfat = nutrition_result[0]['Transfat']
      cholesterol = nutrition_result[0]['Cholesterol']
      sodium = nutrition_result[0]['Sodium']
      total_Carbohydrate = nutrition_result[0]['Total_Carbohydrate']
      protein =  nutrition_result[0]['Protein']
  
  return render(request, 'product_details.html', {'product_Name': product_Name,
                                          'price':price,
                                          'description':description,
                                          'image':image,
                                          'calories':calories,
                                          'total_Fat':total_Fat,
                                          'saturated_Fat':saturated_Fat,
                                          'transfat':transfat,
                                          'cholesterol':cholesterol,
                                          'sodium':sodium,
                                          'total_Carbohydrate':total_Carbohydrate,
                                          'protein':protein})


def recipe_details(request, recipeid = ''):
  """
    Output to front-end:
      { 
        'type_list':list of types(string) e.g. [type1, type2, type3]
        'product_list': list of lists. [[many products with type1], [many products with type2], [many products with type3],]
          - the num of products returned can be controled by PRODUCT_DISPLAY_NUM, default = 5
        'recipe': a recipe object
        'ingredient_name_list': [ingredient_name1, ingredient_name2, ...],
        'ingredient_image_list': [image1, image2, image3, ...]
      }
  """
  PRODUCT_DISPLAY_NUM = 5
  Recipe_Id = recipeid
  recipes = recipe.objects.filter(Recipe_Id__exact=Recipe_Id).values()
  ingredient_name_list = recipe_ingredients.objects.filter(Recipe_Id__exact=Recipe_Id).values()
  type_list = []
  product_list = []
  # print(ingredient_name_list) 
  for name in ingredient_name_list:
    type = name['Type_Id_id']
    typen = list(product_type.objects.filter(Type_Id__exact = type).values())[0]['Product_Type']
    type_list.append(typen)
    product = list(product_info.objects.filter(Type_Id__exact = type).values()[:PRODUCT_DISPLAY_NUM])
    product_list.append(product)
  
  ingredient_name = []
  for name in ingredient_name_list:
    ingredient_name.append(name['Ingredient'])
  ingredient_image_list = recipe_images.objects.filter(Recipe_Id__exact=Recipe_Id).values()
  image_list = []
  for image in ingredient_image_list:
    image_list.append(image['Image'])
  
  print(ingredient_name)

  print(image_list)
  return render(request, 'recipe_details.html', {
      'type_list': type_list,
      'product_list': product_list,
      'recipe': recipes,
      'ingredient_name_list': ingredient_name,
      'ingredient_image_list': image_list
    })


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

list_result= []
list_content =''

def ranger(request):
  min_value = request.GET.get("min_value")
  max_value = request.GET.get("max_value")
  order = request.GET.get("order")
  relavant = request.GET.get("relavant")
  store1 = request.GET.get("ALDI")
  store2 = request.GET.get("Schnucks")
  store3 = request.GET.get("Costco")
  store4 = request.GET.get("Fresh Thyme Market")
  store5 = request.GET.get("Meijer")
  store6 = request.GET.get("Target")
  # print(234134)
  # print(relavant, store1, store2, store3, order, min_value, max_value)
  global list_result
  global list_content
  table = seller.objects.filter(Seller_Id__icontains='cxtnb')
  list_result= table.none()
  #print("relavantt:"+str(relavant))
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
      #print(list_result1[0]['Type_Id'])
      # product_type.objects.raw('SELECT * FROM pages_product_info NATURAL JOIN pages_product_type WHERE ')
   
      if store1 == '1':
        # list_result = list_result.filter(Seller_Id__icontains='ALDI')
        list_result =  list_result|product_info.objects.filter(Type_Id__exact = list_result1[0]['Type_Id'],Product_Name__icontains=list_content, Seller_Id__icontains='ALDI')
      if store2 == '1':
        list_result =  list_result|product_info.objects.filter(Type_Id__exact = list_result1[0]['Type_Id'],Product_Name__icontains=list_content, Seller_Id__icontains='Schnucks')
      if store3 == '1':
        list_result =  list_result|product_info.objects.filter(Type_Id__exact = list_result1[0]['Type_Id'],Product_Name__icontains=list_content, Seller_Id__icontains='Costco')
      if store4 == '1':
        list_result =  list_result|product_info.objects.filter(Type_Id__exact = list_result1[0]['Type_Id'],Product_Name__icontains=list_content, Seller_Id__icontains='Fresh Thyme Market')
      if store5 == '1':
        list_result =  list_result|product_info.objects.filter(Type_Id__exact = list_result1[0]['Type_Id'],Product_Name__icontains=list_content, Seller_Id__icontains='Meijer')
      if store6 == '1':
        list_result =  list_result|product_info.objects.filter(Type_Id__exact = list_result1[0]['Type_Id'],Product_Name__icontains=list_content, Seller_Id__icontains='Fresh Thyme Market')
    else:
      if store1 == '1':
        # list_result = list_result.filter(Seller_Id__icontains='ALDI')
        list_result = list_result|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='ALDI')
      if store2 == '1':
        list_result =  list_result|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='Schnucks')
      if store3 == '1':
        list_result =  list_result|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='Costco')
      if store4 == '1':
        list_result =  list_result|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='Fresh Thyme Market')
      if store5 == '1':
        list_result =  list_result|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='Meijer')
      if store6 == '1':
        list_result =  list_result|product_info.objects.filter(Product_Name__icontains=list_content, Seller_Id__icontains='Fresh Thyme Market')
    
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
  #print('Page:', page_number)

  return render(request, 'listing.html', {'page_obj': page_obj, 'content': list_result})


def listing_search(request):
  global list_result
  global list_content
  print("listing_search:"+"list_content:"+list_content)
  list_content = request.GET.get("list_key")
  list_result = product_info.objects.filter(Product_Name__icontains=list_content)
  print(list_content)
  paginator = Paginator(list_result, 8)  # Show 10 contacts per page.
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  print('Page:', page_number)
  return render(request, 'listing.html', {'page_obj': page_obj, 'content': list(list_result)})

def details(request):
  print("details:"+str(request.GET))
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



# output: title, recipe_ingredients, recipt_image
def recipe_search(request):
  """
  This is a function for recipe search
    Input from front-end:
      1. recipt_search_key: the search key of recipe.
    Output to front-end:
      1. ERROR: if ERROR == 100, no search result for this search key!
      2. content: a list of dictionaries.
        each dictionary contents following items:
         - title: a string of recipe title.
         - recipe_id: the id of the resulting recipe
         - ingredients: a list of strings, [ingredient1, ingredient2, ingredient3,...]
         - recipe_image: a list of images, [image_url1, image_url12, image_url3, ...]
  """
  list_content = request.GET.get("recipt_search_key")
  # print(list_content)
  list_result = recipe.objects.filter(Title__icontains = list_content).values()
  if len(list_result) == 0:
    return render(request, 'recommend.html', {'ERROR': 100})
  return_list = []
  for result in list_result:
    new_item = {}
    new_item['title'] = result['Title']
    id = result['Recipe_Id']
    new_item['recipe_id'] = id
    ingredients = recipe_ingredients.objects.filter(Recipe_Id__exact = id).values()
    ingredients_list = []
    for ingre in ingredients:
      ingredients_list.append(ingre['Ingredient'])
    new_item['ingredients'] = ingredients_list
    images = recipe_images.objects.filter(Recipe_Id__exact = id).values()
    images_list = []
    for image in images:
      images_list.append(image)
    new_item['recipe_image'] = images_list
    return_list.append(new_item)
    
  return render(request, 'recommend.html', {'content': return_list})

