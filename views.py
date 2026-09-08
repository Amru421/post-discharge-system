from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Patient
from .forms import PatientForm, MonitoringForm

from agents.orchestrator import (
    PostDischargeOrchestrator
)


def home(request):

    return render(
        request,
        "patients/home.html"
    )


def register_patient(request):

    if request.method == "POST":

        form = PatientForm(request.POST)

        if form.is_valid():

            patient = form.save()

            return redirect(
                "patient_dashboard",
                patient_id=patient.patient_id
            )

    else:

        form = PatientForm()

    return render(
        request,
        "patients/register.html",
        {"form": form}
    )


def patient_dashboard(
    request,
    patient_id
):

    patient = get_object_or_404(
        Patient,
        patient_id=patient_id
    )

    records = patient.monitoring_records.all()[
        :10
    ]

    medications = patient.medications.all()

    return render(
        request,
        "patients/patient_dashboard.html",
        {
            "patient": patient,
            "records": records,
            "medications": medications
        }
    )


def monitor_patient(
    request,
    patient_id
):

    patient = get_object_or_404(
        Patient,
        patient_id=patient_id
    )

    if request.method == "POST":

        form = MonitoringForm(
            request.POST
        )

        if form.is_valid():

            record = form.save(
                commit=False
            )

            record.patient = patient

            data = {
                "temperature":
                    record.temperature,

                "blood_pressure":
                    record.blood_pressure,

                "heart_rate":
                    record.heart_rate,

                "blood_glucose":
                    record.blood_glucose,

                "pain_level":
                    record.pain_level,

                "symptoms":
                    record.symptoms,

                "medication_status":
                    record.medication_status,

                "general_health":
                    record.general_health,
            }

            orchestrator = (
                PostDischargeOrchestrator()
            )

            result = orchestrator.process(
                patient,
                data
            )

            record.risk_level = (
                result["risk"]["risk"]
            )

            record.emergency_alert = (
                result["emergency"]["alert"]
            )

            record.ai_summary = (
                result["doctor_summary"]
            )

            record.save()

            return render(
                request,
                "patients/monitoring.html",
                {
                    "form": MonitoringForm(),
                    "patient": patient,
                    "result": result
                }
            )

    else:

        form = MonitoringForm()

    return render(
        request,
        "patients/monitoring.html",
        {
            "form": form,
            "patient": patient
        }
    )


def doctor_dashboard(request):

    patients = Patient.objects.all()

    return render(
        request,
        "patients/doctor_dashboard.html",
        {
            "patients": patients
        }
    )