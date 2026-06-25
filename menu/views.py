from django.shortcuts import render
from .models import Food
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Food, Review
def home(request):

    foods = Food.objects.all()[:6]

    reviews = Review.objects.filter(
        approved=True
    ).order_by('-created_at')[:6]

    return render(request, 'index.html', {
        'foods': foods,
        'reviews': reviews,
    })


from django.shortcuts import render
from .models import Food


def home(request):
    foods = Food.objects.all()[:6]

    return render(request, 'index.html', {
        'foods': foods
    })


def food_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    foods = Food.objects.all()

    if query:
        foods = foods.filter(name__icontains=query)

    if category:
        foods = foods.filter(category=category)

    categories = Food.objects.values_list('category', flat=True).distinct()

    return render(request, 'menu.html', {
        'foods': foods,
        'categories': categories,
        'query': query,
        'selected_category': category,
    })

@login_required
def add_review(request):

    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Review.objects.create(
            user=request.user,
            rating=rating,
            comment=comment
        )

        return redirect("home")

    return render(request, "add_review.html")

# Create your views here.
