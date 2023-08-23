from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .forms import createAccountForm

def create_account(request):

    form = createAccountForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = createAccountForm()

        user = authenticate(request, username = request.POST['username'], password = request.POST['password1'])

        if user is not None:
            login(request, user)

            return redirect('/')

    context = {"form": form}

    return render(request, "registration/create_account.html", context)