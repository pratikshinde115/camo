from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer,CartSerializer,CartItemSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import pandas as pd
from django.shortcuts import render ,redirect
from django.db.models import OuterRef, Subquery
from django.contrib import messages

# from app_auth.models import Credentials
@csrf_exempt
def AddToCart(request,product_id):
    
    if request.user.is_authenticated:
        user = User.objects.filter(username = request.user).first()
        serializer =CartSerializer(data={'user': user.id ,'items': product_id})
        if serializer.is_valid():
            serializer.save()
        cart = Cart.objects.filter(user= user.id).first()
        serializer = CartItemSerializer(data={'cart':cart.id,'product':product_id,})
        if serializer.is_valid():
            serializer.save()
        return redirect ("show_cart")
    
        # return render(request, 'add_to_cart.html', {'obj': obj})
    else:
        redirect('signin')

def ShowAdd(request):
    user = User.objects.filter(username=request.user.username).first()
    if user:
        carts = Cart.objects.filter(user=user).first()
        if carts:
            cart_items = CartItem.objects.filter(cart=carts)
            
            subquery = CartItem.objects.filter(cart=carts, product_id=OuterRef('product')).order_by('id')
            unique_products = CartItem.objects.filter(id__in=Subquery(subquery.values('id')[:1]))
            
            product_ids = [item.product.id for item in cart_items]
            
            # Calculate quantities
            quantities = dict(pd.Series(product_ids).value_counts())
            
            # Update quantities in the CartItem model
            for product_id, quantity in quantities.items():
                CartItem.objects.filter(cart=carts, product_id=product_id).update(quantity=quantity)
            
            # Retrieve products
            products = Product.objects.filter(id__in=product_ids)
            return render(request, 'show_cart.html', {'Products': products , 'cart_items':unique_products})
        else:
            return render(request, 'show_cart.html', )
    else:
        return redirect('signup')
        
            


def RemoveFromCart(request, product_id):
    if request.user.is_authenticated:
        try:
            # Retrieve the cart for the current user
            cart = Cart.objects.get(user=request.user)
            # Retrieve the cart item for the given product within the user's cart
            cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()
            # Check if the cart belongs to the authenticated user
            if cart.user == request.user:
                cart_item.delete()
                
            else:
                messages.error(request, 'You are not authorized to remove items from this cart')
        except Cart.DoesNotExist:
            messages.error(request, 'Cart not found')
        except CartItem.DoesNotExist:
            messages.error(request, 'Cart item not found')
        
        return redirect('show_cart')
    else:
        return redirect('signin')

