from django.db.models import Count
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

from .models import Product
from Authen.forms import CustomerProfileForm
from Authen.models import Customer
from cart.models import Cart, Wishlist
from django.db.models import Q
import uuid
from django.utils.crypto import get_random_string

# Create your views here.
def home(request):
    print(uuid.uuid4().hex[:8])
    print(get_random_string(8))
    return render(request, "shop/index.html", locals())

def about(request):
    return render(request, "shop/about.html", locals())

def contact(request):
    return render(request, "shop/contact.html", locals())

class CategoryView(View):
    def get(self, request, val):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        products = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request,'shop/category.html', locals())
    

class CategoryTitle(View):
    def get(self, request, val):
        products = Product.objects.filter(title=val)
        title = Product.objects.filter(category=products[0].category).values('title')
        return render(request,'shop/category.html', locals())
    


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        wishlist=""
        if request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(Q(product = product) & Q(user=request.user))
        return render(request, 'shop/productDetail.html', locals())
    
class ProfileView(View):
    def get(self, request):
        form=CustomerProfileForm()
        return render(request, 'shop/profile.html', locals())
    def post(self, request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user,locality=locality, mobile=mobile,name=name,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Profile save successfully')
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'shop/profile.html',locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'shop/address.html', locals())

class UpdateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request, 'shop/Updateaddress.html',locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,'Address update successfully')
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('address')
    
def search(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    query = request.GET['search']
    product = Product.objects.filter(Q(title__icontains=query) or Q(description__icontains=query))
    return render(request, 'shop/search.html', locals())
