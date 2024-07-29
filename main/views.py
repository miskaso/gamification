from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordResetForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomRecoveryForm
from .models import Media
from .forms import ContactForm

# Create your views here.


def index(req):
    med = Media.objects.all()
    media = dict()
    for i in med:
        media[i.name] = i.img
    return render(req, 'index.html', {'media': media})


def contact(req):
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('../chat.html')
    else:
        form = ContactForm()
    return render(req, 'message.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('chat')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def chat(req):
    return render(req, 'chat.html')


class RecoveryPassword(PasswordResetForm):
    recovery = CustomRecoveryForm
    template_name = 'recovery.html'