# Generated by Django 3.2.9 on 2021-11-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_wanted_item_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='Phone_Number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]