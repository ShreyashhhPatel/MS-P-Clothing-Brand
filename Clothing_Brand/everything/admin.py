from django.contrib import admin
from .models import User_Model, Products, Cart
# Register your models here.
admin.site.register(User_Model)
admin.site.register(Products)
admin.site.register(Cart)