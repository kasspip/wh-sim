from django.contrib import admin

from armory.models import Figurine


@admin.register(Figurine)
class AuthorAdmin(admin.ModelAdmin):
    pass
