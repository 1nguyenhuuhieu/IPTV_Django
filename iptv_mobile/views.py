from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages

from .models import *
# Create your views here.

@login_required(login_url='/login/')
def index(request):
    stream = Stream.objects.all()
    context = {
        'stream': stream
    }
    return render(request, 'index.html', context)

def login_iptv(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.warning(request, 'Sai thông tin đăng nhập')
            return redirect('login')

    return render(request, 'login.html')

def logout_iptv(request):
    logout(request)
    return redirect('index')

def register_iptv(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.create_user(username=username,
                                    email=email,
                                    password=pwd)
            return redirect('login')
        except:
            messages.warning(request, 'Lỗi đăng ký tài khoản')
    return render(request, 'register.html')

@login_required(login_url='/login/')
def profile(request):
    membership = Membership.objects.filter(user=request.user)
    context = {
        'membership': membership

    }
    return render(request, 'profile.html', context)


def group(request):
    group = Group.objects.all()
    context = {
        'group': group
    }

    return render(request, 'group.html', context)

def stream(request, stream_id):
    stream = Stream.objects.get(id=stream_id)
    context = {
        'stream': stream
    }
    return render(request, 'stream.html', context)