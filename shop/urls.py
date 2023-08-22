from django.contrib import admin
from django.urls import include, path

from shop import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('about/', views.about, name="about-page"),
    path('contact/', views.contact, name="contact-page"),
    
    
    path('search/', views.search, name='search-page'),
    
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('address/', views.address, name="address"),
    path('update-address/<int:pk>', views.UpdateAddress.as_view(), name="updateAddress"),
    
    path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
    path('category-title/<val>', views.CategoryTitle.as_view(), name="category-title"),
    path('product-details/<int:pk>', views.ProductDetail.as_view(), name="productDetail"),
]
