from django.db import models

class Product(models.Model):
    title           = models.CharField(max_length=120) #charfield must need max_length
    description     = models.TextField()
    price           = models.DecimalField(max_digits=20,decimal_places=2,null=True) #as we add later so we need to add null = True of set default value.

    def __str__(self):# str is a function that overwrite class object in database
        return self.title
    def __unicode__(self): # this code works only python 2
        return  self.title
