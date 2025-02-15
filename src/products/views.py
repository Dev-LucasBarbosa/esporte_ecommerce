from django.http import Http404
from django.views.generic import ListView, DetailView
from analytics.models import ObjectViewed
from analytics.mixin import ObjectViewedMixin
from carts.models import Cart
from .models import Product, Review
from django.views import View
from django.http import JsonResponse

# Create your views here.

class ProductFeaturedListView(ListView):
    """Listagem de produtos destacados."""
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()

    
class ProductFeaturedDetailView(ObjectViewedMixin, DetailView):
    """Detalhes de um produto destacado."""
    queryset = Product.objects.featured()
    template_name = "products/featured-detail.html"

# Class Based View
class ProductListView(ListView):
    """Listagem de produtos disponíveis."""
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

class ProductDetailView(ObjectViewedMixin, DetailView):
    """Detalhes de um produto utilizando o slug como identificador."""
    template_name = "products/detail.html"
    model = Product  # Define o modelo diretamente

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')  # Busca pelo slug na URL
        instance = Product.objects.filter(slug=slug).first()
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance
    
class ProductDetailSlugView(ObjectViewedMixin, DetailView):
    """Detalhes de um produto utilizando slug como identificador."""
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Produto não encontrado!")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()

        # Cria o evento ObjectViewed se o usuário estiver autenticado
        if self.request.user.is_authenticated:
            ObjectViewed.objects.create(
                user=self.request.user,
                content_object=instance
            )
        return instance
    
class ReviewRateAjaxView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs.get('pk')
        product = Product.objects.get(id=product_id)
        comment = request.POST.get('comment')
        rate = request.POST.get('rate')
        user = request.user

        # Cria e salva a avaliação
        review = Review.objects.create(user=user, product=product, comment=comment, rate=rate)

        # Retorna os dados da avaliação em JSON
        return JsonResponse({
            'user': review.user,
            'comment': review.comment,
            'rate': review.rate,
            'created_at': review.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })