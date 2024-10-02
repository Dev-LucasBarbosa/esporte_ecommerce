from django.urls import path

app_name = "carts"

from .views import cart_page, checkout_home, cart_update, checkout_done_view

urlpatterns = [
    path('', cart_page, name='home'),
    path('checkout/success/', checkout_done_view, name='success'),
    path('checkout/', checkout_home, name='checkout'),
    path('update/', cart_update, name='update')
]