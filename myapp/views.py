# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User

# # Create your views here.
# def home(request):
#     return render(request,'index.html')


# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username,password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponse("You are logged in successfully!")
        
# def show(request):
#     return HttpResponse('My name is Mehedi')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'logout.html')
        else:
            return HttpResponse("Invalid username or password")
    else:
        return render(request, 'index.html')
    
def logout_view(request):
    logout(request)
    return render(request, 'index.html')

