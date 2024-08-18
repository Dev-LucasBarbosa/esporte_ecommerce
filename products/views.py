from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

# Class Based View
class ProductListView(ListView):
    # Traz todos os produtos do BD sem filtrar nada
    queryset = Product.objects.all()
    template_name = "products/list.html"

    #def get_context_data(self, *args, **kwargs):
    #    context = super(ProductListView,self).get_context_data(*args, **kwargs)
    #    print(context)
    #    return context