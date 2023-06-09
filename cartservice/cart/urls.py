from django.urls import path
from .views import *
urlpatterns = [
    path('get_all_cart_items/', getAllCartItem),
    path('get_cart_item/<user_id>', getCartItemByUser),
    path('add_to_cart/', add_to_cart),
    path('update_cart/<cart_id>', update_cart),
    path('delete_cart/<cart_id>', delete_cart),
    path('get_cart/<cart_id>', getCartItemById),
]
