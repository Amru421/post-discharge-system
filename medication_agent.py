class MedicationAgent:

    def check(self, patient, medication_status):

        medications = patient.medications.all()

        result = {
            "status": "ON_TRACK",
            "medications": []
        }

        for medicine in medications:

            result["medications"].append({
                "name": medicine.medicine_name,
                "dosage": medicine.dosage,
                "frequency": medicine.frequency,
                "duration": medicine.duration
            })

        if medication_status == "Missed":

            result["status"] = "MISSED_DOSE"

        return result