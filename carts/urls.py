from django.urls import path

app_name = "carts"

from .views import cart_page, cart_update

urlpatterns = [
    path('', cart_page, name='home'),
    path('update/', cart_update, name='update')
]