from django import forms
from HealthCheckupApp.models import HealthCheckupData,Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

class HealthCheckupDataForm(forms.ModelForm):
    class Meta:
        model=HealthCheckupData
        fields='__all__'