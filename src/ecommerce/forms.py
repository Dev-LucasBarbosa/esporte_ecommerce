from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
    nome_completo = forms.CharField(
    error_messages={'required': 'Obrigatório o preenchimento do nome'},
    widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Seu nome completo"
                }
            )
        )   

    email = forms.EmailField(
        error_messages={'invalid': 'Digite um email válido!'},
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu email"
                }
            )
        )
    
    mensagem = forms.CharField(
        error_messages={'required': 'É obrigatório o preenchimento do campo mensagem!'},
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem"
                }
            )
        )
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("gmail.com") and not email.endswith("outlook.com.br"):
            raise forms.ValidationError("O Email dever ser do gmail ou do outlook")
        return email
    
    def clean_content(self):
        raise forms.ValidationError("O conteúdo está errado.")