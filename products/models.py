import random
from django.db import models
import os

def get_file_name_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext
def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,834234872394)
    name, ext = get_file_name_ext(filename)
    final_file_name = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{final_file_name}".format(new_filename=new_filename,final_file_name=final_file_name)

class Product(models.Model):
    title           = models.CharField(max_length=120) #charfield must need max_length
    description     = models.TextField()
    price           = models.DecimalField(max_digits=20,decimal_places=2,null=True) #as we add later so we need to add null = True of set default value.
    image           = models.ImageField(upload_to=upload_image_path,null=True, blank =False) #blank = True does not used by django


    def __str__(self):# str is a function that overwrite class object in database
        return self.title
    def __unicode__(self): # this code works only python 2
        return  self.title
