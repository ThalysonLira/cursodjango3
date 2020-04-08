from django.contrib import admin

# Register your models here.
from .models import Post

# Modifica a forma como vão ser exibidos os posts no admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories']
    search_fields = ['title', 'sub_title', 'categories']

admin.site.register(Post, PostAdmin)