from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('add-to-cart/', views.add_to_cart, name='addtocart'),
    path('show-cart/', views.show_cart, name='show-cart'),
    path('checkout/', views.checkout.as_view(), name='checkout'),
    path('pluscart/', views.pluscart, name='pluscart'),
    path('minuscart/', views.minuscart, name='minuscart'),
    path('removecart/', views.removecart, name='removecart'),
    path('showwishlist/', views.showwishlist, name='showwishlist'),
    path('pluswishlist/', views.pluswishlist),
    path('minuswishlist/', views.minuswishlist),
    
    
]