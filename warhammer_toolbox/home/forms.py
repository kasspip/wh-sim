from django import forms

from home.models import Profile, Army, Role, Unit


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

    name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'white-text',}))
    role = forms.ModelChoiceField(queryset=Role.objects.all())

    class Meta:
        model = Profile
        exclude = ['unit']
