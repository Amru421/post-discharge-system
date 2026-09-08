from django.db import models


class Patient(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    patient_id = models.CharField(
        max_length=30,
        unique=True
    )

    name = models.CharField(max_length=100)

    age = models.IntegerField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    contact = models.CharField(max_length=15)

    diagnosis = models.TextField()

    admission_date = models.DateField()

    discharge_date = models.DateField()

    treating_doctor = models.CharField(
        max_length=100
    )

    final_diagnosis = models.TextField(
        blank=True
    )

    procedures = models.TextField(
        blank=True
    )

    diet_instructions = models.TextField(
        blank=True
    )

    activity_restrictions = models.TextField(
        blank=True
    )

    warning_signs = models.TextField(
        blank=True
    )

    doctor_instructions = models.TextField(
        blank=True
    )

    follow_up_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.patient_id} - {self.name}"


class Medication(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="medications"
    )

    medicine_name = models.CharField(
        max_length=100
    )

    dosage = models.CharField(
        max_length=100
    )

    frequency = models.CharField(
        max_length=100
    )

    duration = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.medicine_name


class MonitoringRecord(models.Model):

    RISK_CHOICES = [
        ("LOW", "LOW RISK"),
        ("MODERATE", "MODERATE RISK"),
        ("HIGH", "HIGH RISK"),
    ]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="monitoring_records"
    )

    temperature = models.FloatField(
        null=True,
        blank=True
    )

    blood_pressure = models.CharField(
        max_length=30,
        blank=True
    )

    heart_rate = models.IntegerField(
        null=True,
        blank=True
    )

    blood_glucose = models.FloatField(
        null=True,
        blank=True
    )

    pain_level = models.IntegerField(
        null=True,
        blank=True
    )

    symptoms = models.TextField(
        blank=True
    )

    medication_status = models.CharField(
        max_length=20,
        default="Taken"
    )

    general_health = models.CharField(
        max_length=100,
        blank=True
    )

    risk_level = models.CharField(
        max_length=20,
        choices=RISK_CHOICES,
        default="LOW"
    )

    emergency_alert = models.BooleanField(
        default=False
    )

    ai_summary = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.patient.name} - {self.risk_level}"