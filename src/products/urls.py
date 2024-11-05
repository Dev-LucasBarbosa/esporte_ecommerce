from django.urls import path

app_name = "products"

from .views import (
    ProductListView,
    ProductDetailSlugView,
    ReviewRateAjaxView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
    path('review/rate/<int:pk>/ajax/', ReviewRateAjaxView.as_view(), name='review_rate_ajax')
]
