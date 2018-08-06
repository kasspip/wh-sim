from django.contrib import admin
from image_cropping import ImageCroppingMixin

from models import Figurine, Squad, FigurineGroup, Role, Army


@admin.register(Squad)
@admin.register(Army)
@admin.register(FigurineGroup)
@admin.register(Role)
class AuthorAdmin(admin.ModelAdmin):
    pass


class FigurineAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Figurine, FigurineAdmin)
