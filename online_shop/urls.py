
from django.contrib import admin
from django.urls import path
from online_shop import views

urlpatterns = [
    path('product-list/', views.product_list, name='product_list'),
   ]
