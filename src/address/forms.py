from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'endereço_1',
            'endereço_2',
            'cidade',
            'país',
            'estado',
            'cep'
        ]