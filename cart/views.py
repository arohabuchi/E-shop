from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.views import View
from shop import views
from shop.models import Product
from Authen.models import Customer
from cart.models import Cart, Wishlist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
def add_to_cart(request):
    user= request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('show-cart')
    

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user = user)
    amount=0
    for p in cart:
        val = p.quantity * p.product.discounted_price
        amount = amount + val
    totalamount = amount + 60
    return render(request, 'cart/addtocart.html', locals())

def pluscart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0
        for p in cart:
            val=p.quantity * p.product.discounted_price
            amount = amount + val
        totalamount = amount + 60
        print(prod_id)
        
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)
    pass

def minuscart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0
        for p in cart:
            val=p.quantity * p.product.discounted_price
            amount = amount + val
        totalamount = amount + 60
        print(prod_id)
        
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)
    pass

def removecart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0
        for p in cart:
            val=p.quantity * p.product.discounted_price
            amount = amount + val
        totalamount = amount + 60
        print(prod_id)
        
        data={
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)
    pass

@login_required
def pluswishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user,product=product).save()
        data={
            'message':"wishlist added successfully",
        }
        return JsonResponse(data)
    pass

def minuswishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user,product=product).delete()
        data={
            'message':"wishlist removed successfully",
        }
        return JsonResponse(data)
    pass
def showwishlist(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Wishlist.objects.filter(user=user)
    return render(request, 'cart/showwishlist.html', locals())
    
    
@method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 60
        return render(request, 'cart/checkout.html', locals())