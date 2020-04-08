from django.contrib import admin

# Register your models here.
from .models import Post

# Modifica a forma como vão ser exibidos os posts no admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories', 'deleted']
    search_fields = ['title', 'sub_title']

    # Exibe na listagem de posts apenas os posts aprovados
    def get_queryset(self, request):
        return Post.objects.filter(deleted=False)

admin.site.register(Post, PostAdmin)