from django import forms
from django.forms import ModelForm

from foodies.models import Rating


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['recipe', 'user', 'number']
        widgets = {
            'recipe': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'number': forms.NumberInput()
        }


