from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ContactMessage


def contact_view(request):

    if request.method == "POST":

        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message")
        )

        messages.success(
            request,
            "Your message has been sent successfully!"
        )

        return redirect("contact")

    return render(request, "contact.html")

# Create your views here.
