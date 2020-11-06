from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "date", "time")
    search_fields = ['name', 'email']


admin.site.register(Contact, ContactAdmin)