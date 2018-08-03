from django.contrib import admin
from image_cropping import ImageCroppingMixin

from models import Figurine, Squad, Faction, FigurineGroup, Role


@admin.register(Squad)
@admin.register(Faction)
@admin.register(FigurineGroup)
@admin.register(Role)
class AuthorAdmin(admin.ModelAdmin):
    pass


class FigurineAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Figurine, FigurineAdmin)
