from django import forms
from .models import *


class SliderForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))

    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    photo = forms.ImageField(
      widget=forms.FileInput()
    )
    tag_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "tag_uz",
                "class": "form-control"
            }
        ))

    tag_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "tag_ru",
                "class": "form-control"
            }
        ))
    tag_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "tag_en",
                "class": "form-control"
            }
        ))
    url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder": "url",
                "class": "form-control"
            }
        ))
    class Meta:
        model = Slider
        fields = "__all__"