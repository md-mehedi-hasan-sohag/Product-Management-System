from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('changepassword/',views.changePassword, name='changePassword'),
    path('addproduct/',views.addProduct,name='product')
]
