from django.contrib import admin
from .models import Cart, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'phone',
        'total_amount',
        'status',
        'created_at'
    )

    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'phone')
    list_editable = ('status',)
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'food', 'quantity', 'price')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('food', 'quantity')
# Register your models here.
