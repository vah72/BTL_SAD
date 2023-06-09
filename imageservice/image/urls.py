from django.urls import path
from .views import *

urlpatterns = [
    path('add_image/<product_id>', add_image),
    path('delete_image/<product_id>', delete_image),
    path('get_all_image/', getAllImage),
]
