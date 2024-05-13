from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer,CartSerializer,CartItemSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import render ,redirect
# from app_auth.models import Credentials
from django.contrib.auth.models import User

class AddToCartAPIView(APIView):
    def post(self , request, product_id):

        if 'is_logged_in' in request.session:
            current_user = request.session['username']
            
            quantity = int(request.POST['quantity'])
            print(quantity)
            user = User.objects.filter(username = current_user).first()
            serializer =CartSerializer(data={'user': user.id ,'items': product_id})
            if serializer.is_valid():
                serializer.save()
            cart = Cart.objects.filter(user= user.id).first()
            serializer = CartItemSerializer(data={'cart':cart.id,'product':product_id,'quantity':quantity })
            if serializer.is_valid():
                serializer.save()
            return redirect ("/cart/home")
            # return render(request, 'add_to_cart.html', {'obj': obj})

class ShowAddTooCartAPIView(APIView):
    def post(self , request, product_id):

        if 'is_logged_in' in request.session:
            return render(request, 'add_to_cart.html', {'obj': obj})


            
class RemoveFromCartAPIView(APIView):
    def post(self, request, cart_item_id):
        try:
            # Retrieve the cart item
            cart_item = CartItem.objects.get(id=cart_item_id)

            # Check if the cart item belongs to the logged-in user
            if cart_item.cart.user != request.session.get('username'):
                return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

            # Delete the cart item
            cart_item.delete()

            return redirect("/cart/home")

        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)
            

class DisplayProducts(APIView):
    def get(self, request):
        products = Product.objects.all()

        return render(request,'products.html',{'products':products})
