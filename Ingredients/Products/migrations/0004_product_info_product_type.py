# Generated by Django 3.2.9 on 2021-11-08 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_seller_brand_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Type', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='product_info',
            fields=[
                ('Product_Id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Product_Name', models.CharField(max_length=100)),
                ('Price', models.FloatField(null=True)),
                ('Description', models.TextField(blank=True)),
                ('Image', models.ImageField(upload_to='')),
                ('Product_Type', models.ForeignKey(db_column='Product_Type', on_delete=django.db.models.deletion.CASCADE, to='Products.product_type')),
                ('Seller_Id', models.ForeignKey(db_column='Seller_Id', on_delete=django.db.models.deletion.CASCADE, to='Products.seller')),
            ],
        ),
    ]
