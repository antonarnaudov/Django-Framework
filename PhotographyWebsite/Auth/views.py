# Create your views here.
from django.contrib.auth import logout, authenticate, login
# Create your views here.
from django.db import transaction
from django.shortcuts import redirect, render

from Auth.forms import RegisterForm, LoginForm
from common_functionality.get_redirect_url import get_redirect_url


@transaction.atomic
def register_user(request):
    if request.method == 'GET':
        context = {
            'user_form': RegisterForm(),
        }
        return render(request, 'auth/register.html', context)

    else:
        user_form = RegisterForm(request.POST)
        redirect_url = get_redirect_url(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.groups.add(2)

            login(request, user)
            return redirect(redirect_url)

        context = {
            'user_form': user_form,
        }
        return render(request, 'auth/register.html', context)


def login_user(request):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm()
        }
        return render(request, 'auth/login.html', context)
    else:
        login_form = LoginForm(request.POST)
        redirect_url = get_redirect_url(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(redirect_url)
        context = {
            'login_form': login_form,
        }
        return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('work page')
