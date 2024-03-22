from django.shortcuts import render, redirect
from .models import FoodItem

def landing_page(request):
    food_items = FoodItem.objects.filter(availability=True)
    return render(request, 'canteen/landing_page.html', {'food_items': food_items})

def add_to_cart(request, item_id):
    item = FoodItem.objects.get(pk=item_id)
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session['cart'] = cart
    return redirect('landing_page')

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    if item_id in cart:
        del cart[item_id]
        request.session['cart'] = cart
    return redirect('cart')

def update_cart(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        for item_id, quantity in request.POST.items():
            if item_id != 'csrfmiddlewaretoken':
                cart[int(item_id)] = int(quantity)
        request.session['cart'] = cart
    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', {})
    items = []
    total_price = 0
    for item_id, quantity in cart.items():
        item = FoodItem.objects.get(pk=item_id)
        total_price += item.price * quantity
        items.append({'item': item, 'quantity': quantity})
    return render(request, 'canteen/cart.html', {'items': items, 'total_price': total_price})
