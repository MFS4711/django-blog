from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the About model.

    This class customizes the Django admin interface for the `About` model, providing the 
    following features:
    
    - **Summernote integration**: Adds the Summernote rich text editor to the `content` field for easier editing of textual content.
    
    The `content` field is used for managing the text associated with the 'About' section of the website, 
    such as a company description or mission statement.
    """
    summernote_fields = ('content',)

# Register your models here.
# admin.site.register(About)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the CollaborateRequest model.

    This class customizes the Django admin interface for the `CollaborateRequest` model, 
    providing the following features:
    
    - **List display**: Displays the 'message' and 'read' fields in the admin list view to provide quick access 
      to the content and the read status of each collaboration request.
    
    This model is used to handle incoming collaboration requests, and the admin interface allows 
    the admin to manage and review requests effectively.
    """
    list_display = ('message', 'read',)