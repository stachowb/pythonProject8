from django import forms
from .models import Shift


class CreateShiftForm(forms.Form):
    class Meta:
        model = Shift
        fields = ['driver', 'clock_in', 'clock_out', 'km_driven']