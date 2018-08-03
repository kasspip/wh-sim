from django import forms

from home.models import Figurine


class FigurineForm(forms.ModelForm):

    name = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'class': 'white-text',
            }
        ))

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
                  'invulnerability']
