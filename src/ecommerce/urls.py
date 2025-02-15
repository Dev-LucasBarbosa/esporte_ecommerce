"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView

from accounts import views
from address.views import checkout_address_create_view, checkout_address_reuse_view
from billing.views import (
    payment_method_view, 
    payment_success_view, 
    payment_failed_view,
    create_checkout_session
)
from .views import (home_page,  
                    about_page, 
                    contact_page
)

from accounts.views import LoginView, RegisterView, LogoutView, guest_register_view

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('accounts/', include('accounts.urls', namespace='accounts')),  # Inclui o namespace
    path('cart/', include("carts.urls", namespace="cart")),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('billing/create-checkout-session', create_checkout_session, name='create-checkout-session'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('billing/payment-method/', payment_method_view, name='billing-payment-method'),
    path('billing/payment-success/', payment_success_view, name='payment-success'),
    path('billing/payment-failed/', payment_failed_view, name='payment-failed'),
    path('search/', include("search.urls", namespace="search")),
    path('products/', include("products.urls", namespace="products")),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
