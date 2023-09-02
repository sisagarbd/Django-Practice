from django import forms
from django.core import validators
from first_app import models

class MusitianForm(forms.ModelForm):
    class Meta:
        model = models.Musitian
        fields = "__all__"


class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"