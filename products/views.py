from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
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

class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView,self).get_context_data(*args, **kwargs)
        print(context)
        return context
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance