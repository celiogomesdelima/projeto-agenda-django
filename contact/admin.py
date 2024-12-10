from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = 'id',
    list_display_links = ('id', 'name',)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone','show' )
    ordering = '-id',
    list_filter = 'created_date',
    search_fields = ('id', 'first_name', 'last_name', 'phone', )
    list_per_page = 10
    list_max_show_all = 500
    list_editable = 'email', 'phone', 'show',
    list_display_links = ('id', 'first_name',)
