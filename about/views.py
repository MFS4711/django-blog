from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import About
from .forms import CollaborateRequestForm

# Create your views here.


def about_me(request):
    """
    Renders the most recent information on the website author 
    and allows user collaboration requests
    Displays an individual instance of :model:`about.About`
    **Context**
    ``about``
        The most recent instance of :model:`about.About`
    ''collaborate_request_form``
        An instance of :form:`about.CollaborateRequestForm`
    **Template:**
    :template:`about.about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        collaborate_request_form = CollaborateRequestForm(data=request.POST)
        if collaborate_request_form.is_valid():
            collaborate_request.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )

    collaborate_request_form = CollaborateRequestForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_request_form": collaborate_request_form,
        },
    )
