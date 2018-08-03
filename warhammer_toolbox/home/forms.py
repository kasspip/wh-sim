from django import forms

from home.models import Figurine
from image_cropping import ImageCropField, ImageRatioField
from keyhole.widgets import CroppedImageWidget


class FigurineForm(forms.ModelForm):

    name = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'class': 'white-text',
            }
        ))
    picture = forms.ImageField(widget=CroppedImageWidget(width=160, height=160))
    cropping = ImageRatioField('image', '384x256')

    class Meta:
        model = Figurine
        fields = ['movement',
                  'melee',
                  'range',
                  'strength',
                  'toughness',
                  'life',
                  'attacks',
                  'armor',
                  'command',
                  'points',
                  'name',
                  'invulnerability',
                  'picture']
