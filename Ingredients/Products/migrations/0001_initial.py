# Generated by Django 3.2.9 on 2021-11-09 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('Brand_Id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Brand_Name', models.CharField(max_length=50)),
                ('Rating', models.FloatField(blank=True, null=True)),
            ],
            options={
                'ordering': ('Brand_Id',),
            },
        ),
        migrations.CreateModel(
            name='nutrition_table',
            fields=[
                ('Product_Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Calories', models.CharField(blank=True, max_length=100)),
                ('Total_Fat', models.CharField(blank=True, max_length=100)),
                ('Saturated_Fat', models.CharField(blank=True, max_length=100)),
                ('Transfat', models.CharField(blank=True, max_length=100)),
                ('Cholesterol', models.CharField(blank=True, max_length=100)),
                ('Sodium', models.CharField(blank=True, max_length=100)),
                ('Total_Carbohydrate', models.CharField(blank=True, max_length=100)),
                ('Protein', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ('Product_Name',),
            },
        ),
        migrations.CreateModel(
            name='product_type',
            fields=[
                ('Type_Id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Product_Type', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('Recipe_Id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Source_Url', models.URLField(blank=True, null=True)),
                ('Title', models.CharField(max_length=100, null=True)),
                ('Instruction', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('Recipe_Id',),
            },
        ),
        migrations.CreateModel(
            name='test_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('User_Name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=25)),
                ('Last_Name', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('State', models.CharField(blank=True, max_length=25)),
                ('City', models.CharField(blank=True, max_length=25)),
                ('Address', models.CharField(blank=True, max_length=100)),
                ('Zip_Code', models.IntegerField(blank=True, null=True)),
                ('Phone_Number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('User_Name',),
            },
        ),
        migrations.CreateModel(
            name='seller',
            fields=[
                ('Seller_Id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('State', models.CharField(blank=True, max_length=25)),
                ('City', models.CharField(blank=True, max_length=25)),
                ('Address', models.CharField(blank=True, max_length=100)),
                ('Zip_Code', models.IntegerField(blank=True, null=True)),
                ('Phone_Number', models.IntegerField(blank=True, null=True)),
                ('Brand_Id', models.ForeignKey(db_column='Brand_Id', on_delete=django.db.models.deletion.CASCADE, to='Products.brand')),
            ],
            options={
                'ordering': ('Seller_Id',),
            },
        ),
        migrations.CreateModel(
            name='recipe_ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ingredient', models.CharField(max_length=50)),
                ('Recipe_Id', models.ForeignKey(db_column='Recipe_Id', on_delete=django.db.models.deletion.CASCADE, to='Products.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='recipe_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='')),
                ('Recipe_Id', models.ForeignKey(db_column='Recipe_Id', on_delete=django.db.models.deletion.CASCADE, to='Products.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='product_info',
            fields=[
                ('Product_Id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Product_Name', models.CharField(max_length=100)),
                ('Price', models.FloatField(null=True)),
                ('Description', models.TextField(blank=True)),
                ('Image', models.URLField(blank=True)),
                ('Seller_Id', models.ForeignKey(db_column='Seller_Id', on_delete=django.db.models.deletion.CASCADE, to='Products.seller')),
                ('Type_Id', models.ForeignKey(db_column='Type_Id', on_delete=django.db.models.deletion.CASCADE, to='Products.product_type')),
            ],
            options={
                'ordering': ('Product_Id',),
            },
        ),
        migrations.CreateModel(
            name='wanted_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.FloatField()),
                ('Quantity', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Product_Id', models.ForeignKey(db_column='product_info', on_delete=django.db.models.deletion.CASCADE, to='Products.product_info')),
                ('User_Name', models.ForeignKey(db_column='User_Name', on_delete=django.db.models.deletion.CASCADE, to='Products.user')),
            ],
            options={
                'unique_together': {('User_Name', 'Product_Id')},
            },
        ),
    ]
