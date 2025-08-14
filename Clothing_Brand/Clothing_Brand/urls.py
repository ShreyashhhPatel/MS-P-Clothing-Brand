"""
URL configuration for Clothing_Brand project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from everything.views import login, home, suits, suits_page, addtocart, cart, polo, polo_page, delete, aboutus, adminp, new_product, delete_user, delete_product, logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('', home),
    path('suits', suits, name="suits"),
    path("suits_page/<int:id>", suits_page, name="suits_page"),
    path("suits_page/add-to-cart/<int:id>", addtocart, name="addtocart"),
    path('polo', polo, name="polo"),
    path("polo_page/<int:id>", polo_page, name="polo_page"),
    path("polo_page/add-to-cart/<int:id>", addtocart, name="addtocart"),
    path("cart", cart, name="cart"),
    path("delete_cart/<int:id>", delete, name="delete"),
    path("aboutus", aboutus, name="aboutus"),
    path("adminpage", adminp, name="admin"),
    path("new_product", new_product, name="new_product"),
    path("delete_user/<int:id>", delete_user, name="delete_user"),
    path("delete_product/<int:id>", delete_product, name="delete_product"),

]
