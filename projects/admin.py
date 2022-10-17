from django.contrib import admin
from . import models

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author')

admin.site.register(models.Project, AuthorAdmin)
