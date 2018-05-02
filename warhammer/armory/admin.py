from django.contrib import admin

from armory.models import Figurine, Squad, Faction, FigurineGroup, Role


@admin.register(Squad)
@admin.register(Faction)
@admin.register(Figurine)
@admin.register(FigurineGroup)
@admin.register(Role)
class AuthorAdmin(admin.ModelAdmin):
    pass
