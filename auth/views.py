from django.shortcuts import render, redirect, reverse
from django.contrib.auth.admin import User
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist
from .forms import MyUserCreationForm, MyAuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.


def _login_view(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if not user:
            print("user no")
            raise ObjectDoesNotExist("User not found")
        else:
            login(request, user)
            reverse_url = reverse('list')
            return redirect(reverse_url)
    context = {}
    return render(request, "login/login.html", context)


def login_view(request):
    form = MyAuthenticationForm()
    if request.method == "POST":
        form = MyAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Successfully signed in {user.username} ")
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, "login/login_form.html", context)


def logout_view(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        messages.error(request, f"Successfully logged in {user.username}")
        return redirect('/')
    return render(request, 'login/logout.html')


def register_view(request):
    form = MyUserCreationForm()
    if request.method == "POST":
        data = request.POST
        form = MyUserCreationForm(data)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'login/register.html', context)
