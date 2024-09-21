from django.contrib import admin
from . import models


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_read_by_admin']

admin.site.register(models.ContactUs, ContactUsAdmin)