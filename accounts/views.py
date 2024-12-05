from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'accounts/login.html')
def forgotPass(request):
    return render(request, 'accounts/forgot-pass.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        rePassword = request.POST['re_password']
        accept = request.POST['agree-term']
        if password != rePassword:
            messages.error(request, 'Passwords không trùng')
            return redirect('register')
        if accept == 'no':
            messages.error(request, 'Bạn phải chấp nhận điều khoảng')
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')
    return render(request, 'accounts/register.html')
def resetPass(request):
    user = request.user
    if request.method == 'POST':
        password = request.POST['password']
        password2 = request.POST['re-password']
        if password != password2:
            messages.error(request,'Mật khẩu xác nhận không trùng với mật khẩu mới')
            return redirect('resetPass')
        user.set_password(password)
        user.save()
        messages.success(request, 'Đổi thành công')
        return redirect('login')
    return render(request, 'accounts/reset-pass.html')
def home_view(request):
    user = request.user
    return render(request,'accounts/index.html',{'user':user})
def logout_view(request):
    logout(request)
    return redirect('login')
