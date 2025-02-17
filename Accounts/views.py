from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    template_data = {'title': 'Account'}
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            template_data['error'] = 'Invalid username or password.'

    return render(request, 'accounts/login.html', { 'template_data' : template_data })

def signup(request):
    template_data = {'title': 'Sign Up'}
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()

    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form

    return render(request, 'signup/signup.html', {'template_data': template_data})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('Home.home')