from django.contrib import admin
from base.models import Products




class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand','countInStock']
    list_display_links = ['brand']
    list_filter = ['brand']
    search_fields = ['title', 'brand']
    list_editable = ['title']

    class Meta:
        model = Products






admin.site.register(Products,ProductsAdmin)