# Generated by Django 3.2.9 on 2021-11-10 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_product_info_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info',
            name='Type_Id',
            field=models.CharField(max_length=25),
        ),
    ]