from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum

from menu.models import Food
from contact.models import ContactMessage
from .models import Cart, Order, OrderItem


def add_to_cart(request, food_id):
    food = get_object_or_404(Food, id=food_id)

    cart_item = Cart.objects.filter(food=food).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart.objects.create(food=food, quantity=1)

    return redirect('cart')


def cart_view(request):
    cart_items = Cart.objects.all()

    total = 0
    for item in cart_items:
        total += item.food.price * item.quantity

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def increase_quantity(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)
    item.quantity += 1
    item.save()
    return redirect('cart')


def decrease_quantity(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')


def remove_cart_item(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)
    item.delete()
    return redirect('cart')


def checkout(request):
    cart_items = Cart.objects.all()

    total = 0
    for item in cart_items:
        total += item.food.price * item.quantity

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            customer_name=name,
            phone=phone,
            address=address,
            total_amount=total
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                food=item.food,
                quantity=item.quantity,
                price=item.food.price
            )

        cart_items.delete()

        return redirect('order_success')

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total
    })


def order_success(request):
    return render(request, 'orders_success.html')


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'my_orders.html', {
        'orders': orders
    })


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = OrderItem.objects.filter(order=order)

    return render(request, 'order_detail.html', {
        'order': order,
        'items': items
    })


@staff_member_required
def admin_dashboard(request):
    total_orders = Order.objects.count()

    total_revenue = Order.objects.filter(status='Delivered').aggregate(
        total=Sum('total_amount')
    )['total'] or 0

    pending_orders = Order.objects.filter(status='Pending').count()
    preparing_orders = Order.objects.filter(status='Preparing').count()
    out_delivery_orders = Order.objects.filter(status='Out for Delivery').count()
    delivered_orders = Order.objects.filter(status='Delivered').count()
    cancelled_orders = Order.objects.filter(status='Cancelled').count()

    total_foods = Food.objects.count()
    total_messages = ContactMessage.objects.count()

    return render(request, 'admin_dashboard.html', {
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending_orders': pending_orders,
        'preparing_orders': preparing_orders,
        'out_delivery_orders': out_delivery_orders,
        'delivered_orders': delivered_orders,
        'cancelled_orders': cancelled_orders,
        'total_foods': total_foods,
        'total_messages': total_messages,
    })
