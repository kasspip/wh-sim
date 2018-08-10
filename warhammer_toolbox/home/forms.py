from django import forms

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