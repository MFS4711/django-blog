from django.shortcuts import render, get_object_or_404
from .models import About
from .forms import CollaborateRequestForm

# Create your views here.
def about_me(request):

    about = About.objects.all().order_by('-updated_on').first()

    collaborate_request_form = CollaborateRequestForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_request_form": collaborate_request_form,
        },
    )