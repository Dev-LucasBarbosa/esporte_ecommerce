from django.db import models
from carts.models import Cart

# Create your models here.
ORDER_STATUS_CHOICES = (('created', 'Criado'),
                        ('paid', 'Pago'),
                        ('shipped', 'Enviado'),
                        ('refunded', 'Devolvido'),
                       )

class Order(models.Model):
    order_id = models.CharField(max_length = 120, blank = True)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, null = True)
    status = models.CharField(max_length = 120, default = 'created', choices = ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default = 5.99, max_digits = 100, decimal_places = 2)

    def __str__(self):
        return self.order_id