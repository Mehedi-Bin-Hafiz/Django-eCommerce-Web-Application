# Generated by Django 3.1.2 on 2020-10-24 20:54

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=products.models.upload_image_path),
        ),
    ]
