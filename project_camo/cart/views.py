from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer, CartItemSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import render 
class AddToCartAPIView(APIView):
    from django.shortcuts import get_object_or_404

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.user.cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            # If the cart item already exists, increment the quantity
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity  # Set the quantity to the requested value
            cart_item.save()
        return redirect('product_list')
    return render(request, 'add_to_cart.html', {'Cart': Cart})

class RemoveFromCartAPIView(APIView):
    def delete(self, request, cart_item_id):
        cart_item = get_object_or_404(CartItem, pk=cart_item_id)
        cart_item.delete()
        return Response({"message": "Product removed from cart successfully"}, status=status.HTTP_204_NO_CONTENT)

class DisplayProducts(APIView):
    def get(self, request):
        products = Product.objects.all()

        return render(request,'products.html',{'products':products})
