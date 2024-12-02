from django import forms
from .models import CollaborateRequest

class CollaborateRequestForm(forms.ModelForm):
    """
    A form for submitting a collaboration request.

    This class provides a form to gather information from users who wish to submit a 
    collaboration request. The form is based on the `CollaborateRequest` model and includes 
    the following fields:

    - **name**: The name of the person making the request.
    - **email**: The email address of the requester.
    - **message**: A message detailing the collaboration request.

    The form can be used for various collaboration purposes, such as partnership inquiries, 
    project collaborations, or general requests to work together.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message',)