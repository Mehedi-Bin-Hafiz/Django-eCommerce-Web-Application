from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120) #charfield must need max_length
    description = models.TextField()
    price = models.DecimalField(max_digits=20,decimal_places=20,null=True) #as we add later so we need to add null = True of set default value.

