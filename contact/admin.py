from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Category)
class GategoryAdmin(admin.ModelAdmin):
    list_display = 'id','name',
    ordering = 'id',
    list_filter = 'name',
    search_fields = 'id', 'name',
    list_per_page = 10
    list_max_show_all = 20
    list_editable = 'name',
    list_display_links = 'id',

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'phone',
    ordering = 'first_name',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'phone',
    list_display_links = 'id', 'first_name', 'last_name'
