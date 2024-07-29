from django import forms
from .models import Contact
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


class CustomRecoveryForm(PasswordResetForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    email = forms.EmailField(label="Email", max_length=255)


