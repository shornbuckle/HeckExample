from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserRegisterData, User
from .models import Vegetable

class VegetableForm(forms.ModelForm):

    vegetable_choices = (
        ("Carrot", "Carrot"),
        ("Potato", "Potato"),
        ("Garlic", "Garlic"),
        ("Onion", "Onion"),
    )
    vegetable_name = forms.ChoiceField(choices=vegetable_choices)

    class Meta:
        model = Vegetable
        fields = [
            "vegetable_name",

        ]
