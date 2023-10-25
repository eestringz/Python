
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreateForm,CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.http import require_POST, require_http_methods

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('articles:index')
    

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            # form.save() -> 회원가입 후, 따로 로그인을 해야함.
            # 회원가입 후 로그인을 따로 하지 않아도 되는 로직.
            user = form.save()
            auth_login(request,user)
            return redirect('articles:index')
    else:
        form = CustomUserCreateForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    request.user.delete()
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form' : form
    }
    return render(request, 'accounts/update.html', context)


def change_password(request,user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form' : form
    }
    return render(request,'accounts/change_password.html', context)