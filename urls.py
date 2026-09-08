from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "register/",
        views.register_patient,
        name="register_patient"
    ),

    path(
        "patient/<str:patient_id>/",
        views.patient_dashboard,
        name="patient_dashboard"
    ),

    path(
        "patient/<str:patient_id>/monitor/",
        views.monitor_patient,
        name="monitor_patient"
    ),

    path(
        "doctor/",
        views.doctor_dashboard,
        name="doctor_dashboard"
    ),
]