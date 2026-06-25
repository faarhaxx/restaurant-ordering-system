"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from menu.views import food_list
from orders.views import add_to_cart
from orders.views import add_to_cart, cart_view
from orders.views import add_to_cart, cart_view, increase_quantity, decrease_quantity, remove_cart_item
from orders.views import checkout, order_success
from accounts.views import register_view, login_view, logout_view
from orders.views import checkout, order_success, my_orders
from orders.views import order_detail
from menu.views import home, food_list
from django.urls import path, include
from orders.views import admin_dashboard
from menu.views import add_review
urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin/', admin.site.urls),

    
    path('about/', lambda request: render(request, 'about.html'), name='about'),
    path('service/', lambda request: render(request, 'service.html'), name='service'),
    path('booking/', lambda request: render(request, 'booking.html'), name='booking'),
    path('team/', lambda request: render(request, 'team.html'), name='team'),
    path('testimonial/', lambda request: render(request, 'testimonial.html'), name='testimonial'),
    
    path('menu/', food_list, name='menu'),
    path('add-to-cart/<int:food_id>/', add_to_cart, name='add_to_cart'),
    path('add-to-cart/<int:food_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:food_id>/', add_to_cart, name='add_to_cart'),
    path('increase/<int:cart_id>/', increase_quantity, name='increase_quantity'),
    path('decrease/<int:cart_id>/', decrease_quantity, name='decrease_quantity'),
    path('remove/<int:cart_id>/', remove_cart_item, name='remove_cart_item'),
    path('checkout/', checkout, name='checkout'),
    path('order-success/', order_success, name='order_success'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('my-orders/', my_orders, name='my_orders'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('', home, name='home'),
    path('contact/', include('contact.urls')),
    path('add-review/', add_review, name='add_review'),

    
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)