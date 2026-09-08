from django import forms
from .models import Patient, MonitoringRecord


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = "__all__"

        widgets = {
            "admission_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "discharge_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "follow_up_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }


class MonitoringForm(forms.ModelForm):

    class Meta:
        model = MonitoringRecord

        fields = [
            "temperature",
            "blood_pressure",
            "heart_rate",
            "blood_glucose",
            "pain_level",
            "symptoms",
            "medication_status",
            "general_health",
        ]