from django import forms

from armory.models import Figurine


class FigurineForm(forms.ModelForm):

    class Meta:
        model = Figurine
        exclude = []

    def __init__(self, *args, **kwargs):
        super(FigurineForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            self.fields[key].widget.attrs.update({'class': 'white-text'})
