from django import forms

from home import choices
from home.models import Profile, Army, Role, Unit, DegressiveProfile
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
        exclude = ['unit', 'degressive_profile']


ProfileCreateFormSet = inlineformset_factory(parent_model=Unit,
                                             model=Profile,
                                             form=ProfileForm,
                                             extra=1)

ProfileEditFormSet = inlineformset_factory(parent_model=Unit,
                                           model=Profile,
                                           form=ProfileForm,
                                           extra=0)


class DegressiveProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DegressiveProfileForm, self).__init__(*args, **kwargs)
        self.fields['life_1'].widget.attrs.update({'class': 'browser-default'})
        self.fields['life_2'].widget.attrs.update({'class': 'browser-default'})
        self.fields['life_3'].widget.attrs.update({'class': 'browser-default'})
        self.fields['movement_1'].widget.attrs.update({'class': 'browser-default'})
        self.fields['movement_2'].widget.attrs.update({'class': 'browser-default'})
        self.fields['movement_3'].widget.attrs.update({'class': 'browser-default'})
        self.fields['melee_1'].widget.attrs.update({'class': 'browser-default'})
        self.fields['melee_2'].widget.attrs.update({'class': 'browser-default'})
        self.fields['melee_3'].widget.attrs.update({'class': 'browser-default'})
        self.fields['range_1'].widget.attrs.update({'class': 'browser-default'})
        self.fields['range_2'].widget.attrs.update({'class': 'browser-default'})
        self.fields['range_3'].widget.attrs.update({'class': 'browser-default'})
        self.fields['attacks_1'].widget.attrs.update({'class': 'browser-default'})
        self.fields['attacks_2'].widget.attrs.update({'class': 'browser-default'})
        self.fields['attacks_3'].widget.attrs.update({'class': 'browser-default'})

    class Meta:
        model = DegressiveProfile
        exclude = []