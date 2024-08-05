from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .decorators import redirect_authenticated_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@redirect_authenticated_user
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User added.')
            return redirect('login')  
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@redirect_authenticated_user
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})