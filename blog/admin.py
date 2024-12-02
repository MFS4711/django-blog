from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the Post model.

    This class customizes the Django admin interface for the Post model, providing the following features:
    
    - **List display**: Displays the 'title', 'slug', 'status', and 'created_on' fields in the admin list view.
    - **Search fields**: Allows searching by 'title' and 'content' in the admin search bar.
    - **List filters**: Adds filters for 'status' and 'created_on' to narrow down the list of posts.
    - **Prepopulated fields**: Automatically generates a 'slug' field based on the 'title' of the post.
    - **Summernote integration**: Adds the Summernote rich text editor to the 'content' field for easier editing.

    This class inherits from the SummernoteModelAdmin to integrate Summernote's rich text editor for the 'content' field, enhancing the user experience for content creation.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)