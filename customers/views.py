from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def account_view(request):
    if request.POST and 'register' in request.POST :
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        user=User.objects.create_user(username=username,password=password,email=email)
        customer_obj=Customer.objects.create(user=user,phone=phone,address=address,name=username)
        return redirect ('view_account')
    if request.POST  and 'login' in request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('indexpage')
        else:
            print("invalid user credential")


    return render(request,'account.html')