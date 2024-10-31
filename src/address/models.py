from django.db import models
from billing.models import BillingProfile

# Create your models here.
ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE, null = True, blank = True)
    address_type = models.CharField(max_length = 120, choices = ADDRESS_TYPES)
    endereço_1 = models.CharField(max_length = 120)
    endereço_2 = models.CharField(max_length = 120, null = True, blank = True)
    cidade = models.CharField(max_length = 120)
    país = models.CharField(max_length = 120, default = 'Brazil')
    estado = models.CharField(max_length = 120)
    cep = models.CharField(max_length = 120)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return "{line1}\n{line2}\n{city}\n{state},{postal}\n{country}".format(
            line1 = self.endereço_1,
            line2 = self.endereço_2 or "",
            city = self.cidade,
            state = self.estado,
            postal = self.cep,
            country = self.país
        )
