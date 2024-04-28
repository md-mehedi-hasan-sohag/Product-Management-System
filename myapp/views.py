from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User

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

# @login_required
# def changePassword(request):
#     if request.method == 'POST':
#         current_password = request.POST.get('currentPassword')
#         new_password = request.POST.get('newPassword')
#         confirm_password = request.POST.get('confirmPassword')

#         user = request.user
#         if user.check_password(current_password):
#             if new_password == confirm_password:
#                 user.set_password(new_password)
#                 user.save()
#                 update_session_auth_hash(request,user)
#                 return HttpResponse("Password has changed!")
#     else:
#         return render(request,'changepassword.html')
@login_required
def changePassword(request):
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
