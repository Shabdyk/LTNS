from django import forms
from .models import ImportFile

class ImportFileForm(forms.ModelForm):
    class Meta:
        model = ImportFile
        fields = ['file']
