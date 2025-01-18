from django.contrib import admin
from .models import Menu

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'author', 'published', 'status']
    list_filter = ['author', 'published', 'status']
    search_fields = ['name']
    date_hierarchy = 'published'
    ordering = ['status', 'published']
    raw_id_fields = ['author']

admin.site.register(Menu, MenuAdmin)
