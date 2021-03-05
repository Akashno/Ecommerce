from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from authenticate.decorators import unauthenticated_view
from authenticate.forms import CreateUserForm
from user.models import Cart


@unauthenticated_view
def register_page(request):
    form = CreateUserForm()
    if request.POST:
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        else:
            messages.success(request, 'invalid values')
    context = {'form': form}
    return render(request, 'authenticate/register_page.html', context)


@unauthenticated_view
def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_page')
            else:
                return redirect('index')
        else:
            messages.error(request, 'Invalid username / password')
    context = {}
    return render(request, 'authenticate/login_page.html', context)


def logout_page(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_items.delete()
    logout(request)

    return redirect('index')
