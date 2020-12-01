from django.contrib import admin
from .models import Product, ProductImage, Variation


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'updated']
    search_fields = ['title', 'description']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    date_hierarchy = 'timestamp'
    readonly_fields = ['timestamp', 'updated']
    prepopulated_fields = {'slug': ('title',), }

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Variation)
