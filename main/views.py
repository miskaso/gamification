from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordResetForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomRecoveryForm
from .models import Media, VisitedPage
from .forms import ContactForm



# Create your views here.

@login_required
def set_cookie(request, response):
    if request.COOKIES.get('visit_count'):
        visit_count = int(request.COOKIES.get('visit_count')) + 1
    else:
        visit_count = 1
    response.set_cookie('visit_count', str(visit_count))

    return response


def index(req):
    med = Media.objects.all()
    media = dict()
    for i in med:
        media[i.name] = i.img

    response = render(req, 'index.html', {'media': media})
    response = set_cookie(req, response)
    return response


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


def chat(req):
    return render(req, 'chat.html')


@login_required()
class RecoveryPassword(PasswordResetForm):
    recovery = CustomRecoveryForm
    template_name = 'recovery.html'


def user_logout(request):
    if request.user.is_authenticated:
        visited_pages = []
        visited_cookies = request.COOKIES.get('visit_count')
        if visited_cookies:
            visited_pages = visited_cookies.split(',')
            for page in visited_pages:
                VisitedPage.objects.create(user=request.user, page_name=page)
            logout(request)
            response = redirect('login')
            response.delete_cookie('visit_count')
            return response
    else:
        return redirect('login')
