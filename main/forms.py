from django import forms
from .models import Contact, Chat
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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


class CustomRecoveryForm(forms.ModelForm):
    class Meta:
        captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
        model = User
        fields = ['email']


class ShowChat(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['message']