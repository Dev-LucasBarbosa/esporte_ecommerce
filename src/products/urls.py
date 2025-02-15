from django.urls import path

app_name = "products"

from .views import (
    ProductListView,
    ProductDetailView,
    ReviewRateAjaxView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('category/<slug:slug>/', ProductListView.as_view(), name='category'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('review/rate/<int:pk>/ajax/', ReviewRateAjaxView.as_view(), name='review_rate_ajax')
]
