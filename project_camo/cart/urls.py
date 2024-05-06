from django.urls import path
from .views import AddToCartAPIView, RemoveFromCartAPIView, DisplayProducts

urlpatterns = [
    path('add-to-cart/<int:product_id>/', AddToCartAPIView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', RemoveFromCartAPIView.as_view(), name='remove_from_cart'),
    path('home/', DisplayProducts.as_view(), name='Product'),
]
