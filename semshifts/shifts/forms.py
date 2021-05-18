from django import forms
from .models import Shift


class CreateShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['company', 'driver', 'clock_in', 'clock_out', 'km_driven']

        widgets = {
            "driver": forms.TextInput(attrs={"class": "form-control"}),
            "clock_in": forms.DateTimeInput(attrs={"class": "form-control"}),
            "clock_out": forms.DateTimeInput(attrs={"class": "form-control"}),
            "km_driven": forms.NumberInput(attrs={"class": "form-control"})
        }