from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registered user')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('contact:user_update')

    return render(
        request,
        'contact/user_update.html',
        {
            'form': form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('contact:index')
        messages.error(request, 'Invalid login')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')