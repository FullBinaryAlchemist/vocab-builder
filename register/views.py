from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from register import urls


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('register:signup')
    else:
        form = UserRegisterForm()
    return render(request, 'register/users.html', {'form': form})