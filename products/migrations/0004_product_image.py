# Generated by Django 3.1.2 on 2020-10-24 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201023_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to='products/'),
        ),
    ]