from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (Post.__str__, 'author', 'thread', 'posted_date')
    search_fields = ['author']

    class Meta:
        model = Post


# Register your models here.
admin.site.register(Post, PostAdmin)
