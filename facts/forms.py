from django import forms
from .models import Fact


class FactForm(forms.ModelForm):
    csv_file = forms.FileField(label='Upload CSV file', required=False)

    class Meta:
        model = Fact
        fields = []
