from django.urls import path

app_name = "carts"

from .views import cart_page, checkout_home, cart_update

urlpatterns = [
    path('', cart_page, name='home'),
    path('checkout/', checkout_home, name='checkout'),
    path('update/', cart_update, name='update')
]