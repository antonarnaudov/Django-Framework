from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render

from Auth.forms import RegisterForm, LoginForm, EditDataForm, ProfileForm
from common_functionality.get_redirect_url import get_redirect_url


@transaction.atomic
def register_user(request):
    if request.method == 'GET':
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'auth/register.html', context)

    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        redirect_url = get_redirect_url(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)

            user.groups.add(2)

            profile.user = user
            profile.save()

            login(request, user)
            return redirect(redirect_url)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
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


def view_user_profile(request, pk):
    if request.user.id != pk:
        logout(request)
        return redirect('login user')

    context = {
        'profile': request.user
    }
    return render(request, 'auth/view_profile.html', context)


def edit_user_profile(request, pk):
    if request.user.id != pk:
        logout(request)
        return redirect('login user')

    user = User.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'user': user,
            'form': EditDataForm(instance=user)
        }
        return render(request, 'auth/edit_profile.html', context)
    else:

        form = EditDataForm(request.POST, instance=user)
        if form.is_valid():
            if form.cleaned_data['username']:
                user.username = form.cleaned_data['username']

            if form.cleaned_data['email']:
                user.email = form.cleaned_data['email']

            if form.cleaned_data['first_name']:
                user.first_name = form.cleaned_data['first_name']

            if form.cleaned_data['last_name']:
                user.last_name = form.cleaned_data['last_name']

            user.save()

            return redirect('view profile', pk)
        context = {
            'user': user,
            'form': form,
        }
        return render(request, 'auth/edit_profile.html', context)
