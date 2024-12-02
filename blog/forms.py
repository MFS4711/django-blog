from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    A form for creating and updating Comment instances.

    This class uses Django's ModelForm to generate a form based on the Comment model. 
    It includes the following features:

    - **Model**: The form is tied to the `Comment` model.
    - **Fields**: The form includes a single field, 'body', which corresponds to the content of the comment.
    
    This form is typically used in situations where users can submit or update comments, such as in blog posts or discussion threads.
    """
    class Meta:
        model = Comment
        fields = ('body',)