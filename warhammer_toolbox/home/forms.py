from django import forms

from home import choices
from home.models import Profile, Army, Role, Unit
from django.forms.models import inlineformset_factory, BaseInlineFormSet


class ArmyForm(forms.ModelForm):

    name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'white-text',}))

    class Meta:
        model = Army
        fields = ['name', 'icon']


class UnitForm(forms.ModelForm):

    name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'white-text',}))
    power = forms.IntegerField(initial=1, widget=forms.TextInput(attrs={'class': 'white-text',}))

    class Meta:
        model = Unit
        fields = ['name', 'power', 'image']

   
class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['movement'].widget.attrs.update({'class': 'browser-default'})
        self.fields['melee'].widget.attrs.update({'class': 'browser-default'})
        self.fields['range'].widget.attrs.update({'class': 'browser-default'})
        self.fields['strength'].widget.attrs.update({'class': 'browser-default'})
        self.fields['toughness'].widget.attrs.update({'class': 'browser-default'})
        self.fields['life'].widget.attrs.update({'class': 'browser-default'})
        self.fields['attacks'].widget.attrs.update({'class': 'browser-default'})
        self.fields['command'].widget.attrs.update({'class': 'browser-default'})
        self.fields['armor'].widget.attrs.update({'class': 'browser-default'})
        self.fields['invulnerability'].widget.attrs.update({'class': 'browser-default'})

    class Meta:
        model = Profile
        exclude = ['unit']


ProfileFormSet = inlineformset_factory(parent_model=Unit,
                                       model=Profile,
                                       form=ProfileForm,
                                       extra=1)

ProfileEditFormSet = inlineformset_factory(parent_model=Unit,
                                           model=Profile,
                                           form=ProfileForm,
                                           extra=0)
