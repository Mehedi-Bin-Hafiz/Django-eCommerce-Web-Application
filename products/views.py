from django.shortcuts import render

from django.views.generic import  ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Product

#class based view
class ProductListView(ListView):
    queryset = Product.objects.all() # the way of making query set. it getting every thing from database
    template_name = 'products/product_list.html'
    """It works with object_list"""
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args,**kwargs)
    #     print(context) #paginated = পৃষ্ঠায়িত
    #     return context

class ProductDetailView(DetailView):
    queryset = Product.objects.all() # the way of making query set. it getting every thing from database
    template_name = 'products/product_detail.html'

    """It works with object // To know description {{ object.description }}"""

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
    #     print(context) #paginated = পৃষ্ঠায়িত
    #     return context



#function based view

def product_List_view(request):
    queryset = Product.objects.all()
    context={
        'object_list': queryset
    }

    return render(request,'products/product_list.html',context)

def product_detail_view(request, pk = None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)

    instance = get_object_or_404(Product,pk=pk)

    context={
        'object': instance
    }
    return render(request,'products/product_detail.html',context)
