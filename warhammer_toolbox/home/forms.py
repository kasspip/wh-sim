from django import forms

from home.models import Figurine, Army


class FigurineForm(forms.ModelForm):

    name = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'class': 'white-text',
            }
        ))
    army = forms.ModelChoiceField(queryset=Army.objects.all())

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
                  'picture',
                  # 'cropping',
                  'army']

        # widgets = {
        #     'picture': ImageCropWidget,
        # }
