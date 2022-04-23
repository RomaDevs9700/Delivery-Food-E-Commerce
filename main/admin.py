from django.contrib import admin
from . models import Home, About, Menu, Products, Contact

admin.site.register([About, Home])


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('title', 'price')
    list_display = ('title', 'price', 'discount')
    list_filter = ('title',)
    

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    search_fields = ('title', 'price')
    list_display = ('title', 'price', 'discount')
    list_filter = ('title', )
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email')
    list_display = ('name', 'email', 'number', 'check_display')
    list_filter = ('name', 'email')
