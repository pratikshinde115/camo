from django.urls import path
from .views import AddToCart, RemoveFromCart ,ShowAdd

urlpatterns = [
    path('add-to-cart/<int:product_id>/', AddToCart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', RemoveFromCart, name='remove_from_cart'),
    # path('home/', DisplayProducts.as_view(), name='Product'),
    path('showcart/',ShowAdd,name ='show_cart')
]
