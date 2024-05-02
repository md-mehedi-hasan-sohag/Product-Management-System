from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from myapp.models import Product
from django.contrib import messages 

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
@login_required   
def logout_view(request):
    logout(request)
    return render(request, 'index.html')

@login_required                 #sohag #sohagsohag(user)
def changePassword(request):    #mehedi #BracBrac(admin)
    if request.method == 'POST':
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')

        user = request.user
        if user.check_password(current_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request,user)
                return render(request,'index.html')
            else:
                return HttpResponse("New password and confirm password do not match.")
        else:
            return HttpResponse("Current password is incorrect.")
    else:
        return render(request,'changepassword.html')

@login_required
def addproductpage(request):
    return render(request,'addproduct.html')

@login_required
def addProduct(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        country = request.POST.get('country')
        quantity = request.POST.get('quantity')
        rating = request.POST.get('rating')
        picture = request.FILES.get('image')
        description = request.POST.get('description')

        Product.objects.create(
            name=name,
            price=price,
            category=category,
            brand=brand,
            country=country,
            quantity=quantity,
            rating = rating,
            img=picture,
            description=description
        )
        messages.success(request,"Product Added")
        return render(request, 'addproduct.html')
    else:
        return HttpResponse("Product cannot add!")
