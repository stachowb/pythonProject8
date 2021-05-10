from django import forms
from .models import Shift


class CreateShiftForm(forms.Form):
    class Meta:
        model = Shift
        fields = ['driver', 'clock_in', 'clock_out', 'km_driven']

        widgets = {
            "driver": forms.TextInput(attrs={"class": "form-control"}),
            "clock_in": forms.TextInput(attrs={"class": "form-control"}),
            "clock_out": forms.TextInput(attrs={"class": "form-control"}),
            "km_driven": forms.TextInput(attrs={"class": "form-control"})
        }