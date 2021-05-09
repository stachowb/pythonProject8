from django import forms

class ShiftFileForm(forms.Form):
    file = forms.FileField()