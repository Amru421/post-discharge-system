class EmergencyAgent:

    def handle(self, patient, risk_result):

        if risk_result["risk"] == "HIGH":

            return {
                "alert": True,

                "message": (
                    "URGENT: Please contact your healthcare "
                    "provider or emergency medical services."
                ),

                "patient_id": patient.patient_id
            }

        return {
            "alert": False,
            "message": "No emergency alert triggered."
        }