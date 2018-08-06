from django import forms

from home.models import Figurine, Army, Role


class FigurineForm(forms.ModelForm):

    name = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'class': 'white-text',
            }
        ))
    role = forms.ModelChoiceField(queryset=Role.objects.all())

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
                  'role']

        # widgets = {
        #     'picture': ImageCropWidget,
        # }
