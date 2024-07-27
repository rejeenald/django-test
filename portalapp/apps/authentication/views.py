# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required

#Load CORE views to inherit from
from core import views as CORE_VIEWS


def login_view(request):
    context = CORE_VIEWS.context_maker(request, {})

    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    context['form'] = form
    context['msg'] = msg

    return render(request, "authentication/login.html", context)


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "authentication/register.html", {"form": form, "msg": msg, "success": success})

@login_required(login_url="/login/")
def myteam (request):
    context = CORE_VIEWS.context_maker(request, {})
    return render(request, "authentication/myteam.html", context)

@login_required(login_url="/login/")
def userprofile (request):
    context = CORE_VIEWS.context_maker(request, {})
    return CORE_VIEWS.template_loader(request, context, 'authentication/profile.html')
