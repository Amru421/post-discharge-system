class DoctorAgent:

    def create_summary(
        self,
        patient,
        monitoring_result,
        risk_result,
        medication_result,
        followup_result
    ):

        observations = monitoring_result[
            "observations"
        ]

        summary = f"""
Patient: {patient.name}
Patient ID: {patient.patient_id}

Risk Level:
{risk_result['risk']}

Risk Reason:
{risk_result['reason']}

Monitoring Observations:
{', '.join(observations) if observations else 'No concerning observations'}

Medication Status:
{medication_result['status']}

Follow-up Status:
{followup_result['status']}

Follow-up Message:
{followup_result['message']}
"""

        return summary