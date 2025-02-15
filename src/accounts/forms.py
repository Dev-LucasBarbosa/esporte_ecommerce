from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'full_name']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Suas senhas devem ser iguais")
        return cleaned_data
    
    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_verified = False
        if commit:
            user.save()
        return user
    
class UserAdminChangeForm(forms.ModelForm):
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'active', 'admin', 'is_verified']

    def clean_password(self):
        return self.initial["password"]

class GuestForm(forms.Form):
    email = forms.EmailField()

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Senha", max_length=255, widget=forms.PasswordInput(attrs={"class": "form-control"}))

class RegisterForm(forms.ModelForm):

    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'full_name']  # [ADDED] Incluído full_name no formulário
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Suas senhas devem ser iguais")
        return cleaned_data
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_verified = False  # [ADDED] Usuários não verificados por padrão
        if commit:
            user.save()
        return user