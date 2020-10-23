from django.shortcuts import render

from django.views.generic import  ListView
from django.shortcuts import render
from .models import Product

#class based view
class ProductListView(ListView):
    queryset = Product.objects.all() # the way of making query set. it getting every thing from database
    template_name = 'products/product_list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args,**kwargs)
    #     print(context) #paginated = পৃষ্ঠায়িত
    #     return context



#function based view

def product_List_view(request):
    queryset = Product.objects.all()
    context={
        'object_list': queryset
    }

    return render(request,'products/product_list.html',context)
