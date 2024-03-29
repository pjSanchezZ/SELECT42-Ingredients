# Generated by Django 3.2.9 on 2021-11-09 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe_ingredients',
            name='Type_Id',
            field=models.ForeignKey(db_column='Type_Id', default=0, on_delete=django.db.models.deletion.CASCADE, to='pages.product_type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe_images',
            name='Image',
            field=models.URLField(),
        ),
    ]
