# Generated by Django 3.2.9 on 2021-11-10 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20211109_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info',
            name='Seller_Id',
            field=models.CharField(max_length=25),
        ),
    ]