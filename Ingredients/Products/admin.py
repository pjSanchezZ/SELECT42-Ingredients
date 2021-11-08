from django.contrib import admin
from .models import user, brand, seller, product_info, product_type, wanted_item, nutrition_table, test_image, recipe, recipe_images, recipe_ingredients
# Register your models here.

admin.site.register(user)
admin.site.register(brand)
admin.site.register(seller)
admin.site.register(product_type)
admin.site.register(product_info)
admin.site.register(wanted_item)
admin.site.register(nutrition_table)
admin.site.register(test_image)
admin.site.register(recipe)
admin.site.register(recipe_images)
admin.site.register(recipe_ingredients)