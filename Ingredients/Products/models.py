from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

class user(models.Model):
  User_Name = models.CharField(max_length = 50, primary_key = True)
  First_Name = models.CharField(max_length = 25)
  Last_Name = models.CharField(max_length = 25)
  Email = models.EmailField()
  State = models.CharField(max_length = 25, blank=True)
  City = models.CharField(max_length = 25, blank=True)
  Address = models.CharField(max_length = 100, blank=True)
  Zip_Code = models.IntegerField(null=True, blank=True)
  Phone_Number = models.IntegerField(null=True, blank=True)
  
  class Meta:
    ordering = ('User_Name',)
  
  def __str__(self):
      return self.User_Name

class brand(models.Model):
  Brand_Id = models.CharField(max_length = 25, primary_key = True)
  Brand_Name = models.CharField(max_length = 50)
  Rating = models.FloatField(blank=True, null=True)

  class Meta:
    ordering = ('Brand_Id',)

  def __str__(self):
      return self.Brand_Id

class seller(models.Model):
  Seller_Id = models.CharField(max_length = 25, primary_key = True)
  Brand_Id = models.ForeignKey('brand', on_delete = models.CASCADE, db_column='Brand_Id')
  State = models.CharField(max_length = 25, blank = True)
  City = models.CharField(max_length = 25, blank = True)
  Address = models.CharField(max_length = 100, blank=True)
  Zip_Code = models.IntegerField(null=True, blank=True)
  Phone_Number = models.IntegerField(null=True, blank=True)

  class Meta:
    ordering = ('Seller_Id',)

  def __str__(self) :
      return self.Seller_Id

class product_type(models.Model):
  Type_Id = models.CharField(max_length=25, primary_key=True)
  Product_Type = models.CharField(max_length = 50, unique = True)
  
  def __str__(self) :
      return self.product_type


class product_info(models.Model):
  Product_Id = models.CharField(max_length = 25, primary_key = True)
  Product_Name = models.CharField(max_length = 100)
  Price = models.FloatField(null = True)
  Type_Id = models.ForeignKey('product_type', on_delete = models.CASCADE, db_column = 'Type_Id')
  Seller_Id = models.ForeignKey('seller', on_delete = CASCADE, db_column = 'Seller_Id')
  Description = models.TextField(blank=True)
  Image = models.URLField(blank = True)

  class Meta:
    ordering = ('Product_Id',)
  
  def __str__(self):
      return self.Product_Name

#Todo: charfield -> float field
class nutrition_table(models.Model):
  Product_Name = models.CharField(max_length = 100, primary_key=True)
  Calories = models.CharField(max_length = 100,blank=True)
  Total_Fat = models.CharField(max_length = 100,blank=True)
  Saturated_Fat = models.CharField(max_length = 100,blank=True)
  Transfat = models.CharField(max_length = 100,blank=True)
  Cholesterol = models.CharField(max_length = 100,blank=True)
  Sodium = models.CharField(max_length = 100,blank=True)
  Total_Carbohydrate = models.CharField(max_length = 100,blank=True)
  Protein = models.CharField(max_length = 100,blank=True)
  class Meta:
    ordering = ('Product_Name',)
  
  def __str__(self):
      return self.Product_Name

class wanted_item(models.Model):
  User_Name = models.ForeignKey('user', on_delete=models.CASCADE, db_column='User_Name')
  Product_Id = models.ForeignKey('product_info', on_delete=models.CASCADE, db_column='product_info')
  Price = models.FloatField()
  Quantity = models.IntegerField()
  Date = DateTimeField(auto_now=True)

  class Meta:
    unique_together =(('User_Name', 'Product_Id'),)
  
  def __str__(self):
    return self.Product_Id

class test_image(models.Model):
  img = ImageField()

class recipe(models.Model):
  Recipe_Id = models.CharField(max_length=50, primary_key=True)
  Source_Url = models.URLField(null=True, blank=True)
  Title = models.CharField(max_length=100, null=True)
  Instruction = models.TextField(null=True, blank=True)

  class Meta:
    ordering = ('Recipe_Id',)
  
  def __str__(self):
      return self.Title

class recipe_ingredients(models.Model):
  Recipe_Id = models.ForeignKey('recipe', on_delete=CASCADE, db_column='Recipe_Id')
  Ingredient = models.CharField(max_length=50)

  def __str__(self):
      return self.Recipe_Id

class recipe_images(models.Model):
  Recipe_Id = models.ForeignKey('recipe', on_delete=CASCADE, db_column='Recipe_Id')
  Image = models.ImageField()

  def __str__(self):
      return self.Recipe_Id




  
  


  

  




