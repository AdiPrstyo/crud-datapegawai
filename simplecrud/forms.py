from django import forms

from simplecrud.models import Crudsimple

class CrudsimpleForm(forms.ModelForm):

    genders = (('Pria', 'Pria'),('Wanita', 'Wanita'))
    gender = forms.ChoiceField(choices=genders,widget=forms.RadioSelect)
    class Meta:
        model = Crudsimple
        fields = "__all__"