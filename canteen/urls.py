from django.urls import path
from .views import landing_page, add_to_cart, remove_from_cart, update_cart, cart

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update-cart/', update_cart, name='update_cart'),
    path('cart/', cart, name='cart'),
]
