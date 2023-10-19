from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login

from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from users.models import User


# Create your views here.
def user_register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user = authenticate(request)
            login(request, user)
            messages.success(request, "you registered successfully")
            return redirect ('users:home')
        else:
            messages.warning(request, "register unsuccessfully")
            return render (request, 'user/user_register_form.html', {'form': form})
    elif request.method == "GET":
        form = UserRegisterForm()
        return render(request, 'user/user_register_form.html', {'form': form})

def user_login_view(request):
    if request.method == "GET":
        form = UserLoginForm()
        return render(request, 'user/user_login_form.html', {'form': form})
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, "login successful")
                login(request, user)
                return redirect('users:home')
            else:
                messages.warning(request, "login unsuccessful")
                return render(request, 'user/user_login_form.html', {'form': form})

def user_logout_view(request):
    logout(request)
    return redirect('users:home')


def user_profile_view(request, uid):
    pass


def user_profile_edit_view(request):
    if request.method == "GET":
        form = UserUpdateForm()
        return render(request, 'user/user_edit.html', {'form': form})
    else:
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:home')
        else:
            return render(request, 'user/user_edit.html', {"form": form})
            

def user_home_view(request):
    return render(request, 'home.html')
