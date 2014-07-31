# -*- coding: UTF-8-*-

from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse


@login_required
def index(request):
    return render(request, 'page/index.html')


@login_required
def home(request):
    return render(request, 'page/index.html')


# Accounts
def login(request):

    # Si usuario ya está logado, lo devolvemos a home.
    if request.user.is_authenticated():
        return redirect('home')

    # Se define el formulario
    form = AuthenticationForm()

    # Debe ser post
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('home')
            else:
                #return render_to_response('accounts/login.html')
                # Return a 'disabled account' error message
                return HttpResponse("disabled account")
        else:
            form = AuthenticationForm(data=request.POST)
            form.is_valid()

    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    try:
        auth.logout(request)
    except:
        pass

    return redirect('login')
