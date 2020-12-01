from django.contrib import admin
from .models import Directory, Thread


class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('section_name', 'number_topics', 'number_posts',)
    search_fields = ['section_name']

    class Meta:
        model = Directory

    def get_queryset(self, request):
        queryset = super(DirectoryAdmin, self).get_queryset(request)
        queryset = queryset.order_by('section_name')
        return queryset


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('directory', 'topic', 'posted_date', 'author', 'number_of_views',)
    search_fields = ['author']

    class Meta:
        model = Thread


# Register your models here.
admin.site.register(Directory, DirectoryAdmin)
admin.site.register(Thread, ThreadAdmin)
