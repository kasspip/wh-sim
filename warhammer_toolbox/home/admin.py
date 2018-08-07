from django.contrib import admin
from image_cropping import ImageCroppingMixin

from models import Profile, Unit, Role, Army, Race

@admin.register(Race)
@admin.register(Unit)
@admin.register(Army)
@admin.register(Role)
class AuthorAdmin(admin.ModelAdmin):
    pass


class FigurineAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Profile, FigurineAdmin)
