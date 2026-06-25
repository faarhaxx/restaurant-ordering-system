from django.contrib import admin
from .models import Food, Review


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')
    list_filter = ('category', 'available')
    search_fields = ('name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'approved', 'created_at')
    list_filter = ('approved', 'rating')
    search_fields = ('user__username', 'comment')
    list_editable = ('approved',)

# Register your models here.
