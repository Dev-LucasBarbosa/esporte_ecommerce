from django.contrib import admin
from .models import Product, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__','slug')
    class meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'rate', 'comment', 'created_at')
    class meta:
        model = Review
admin.site.register(Review, ReviewAdmin) 