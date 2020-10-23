from django.shortcuts import render

from django.views.generic import  ListView
from django.shortcuts import render
from .models import Product

#class based view
class ProductListView(ListView):
    queryset = Product.objects.all() # the way of making query set. it getting every thing from database
    template_name = 'products/product_list.html'



#function based view

def product_List_view(request):
    queryset = Product.objects.all()
    context={
        'object_list': queryset
    }

    return render(request,'products/product_list.html',context)
