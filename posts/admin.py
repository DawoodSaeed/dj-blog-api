from django.contrib import admin
from .models import Post

class CustomPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
        "author",
    )

# Register your model with the custom admin
admin.site.register(Post, CustomPostAdmin)
