# Generated by Django 3.2.9 on 2021-11-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_seller_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wanted_item',
            name='Valid',
        ),
        migrations.AlterField(
            model_name='seller',
            name='Phone_Number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Phone_Number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
