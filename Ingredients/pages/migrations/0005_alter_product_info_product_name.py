# Generated by Django 3.2.9 on 2021-11-10 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_product_info_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info',
            name='Product_Name',
            field=models.CharField(max_length=500),
        ),
    ]
