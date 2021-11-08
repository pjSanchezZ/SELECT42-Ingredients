# Generated by Django 3.2.9 on 2021-11-08 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_alter_product_info_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition_table',
            name='Calories',
            field=models.CharField(blank=True, default='unknow', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nutrition_table',
            name='Cholesterol',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='nutrition_table',
            name='Protein',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='nutrition_table',
            name='Saturated_Fat',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='nutrition_table',
            name='Sodium',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='nutrition_table',
            name='Total_Carbohydrate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='nutrition_table',
            name='Total_Fat',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='nutrition_table',
            name='Transfat',
            field=models.CharField(blank=True, max_length=100),
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
