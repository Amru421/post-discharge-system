class RiskAssessmentAgent:

    def assess(self, data, monitoring_result):

        symptoms = data.get(
            "symptoms",
            ""
        ).lower()

        temperature = data.get("temperature")
        heart_rate = data.get("heart_rate")
        pain = data.get("pain_level")

        emergency_keywords = [
            "chest pain",
            "difficulty breathing",
            "severe bleeding",
            "unconscious",
            "loss of consciousness",
            "severe breathlessness"
        ]

        for keyword in emergency_keywords:

            if keyword in symptoms:

                return {
                    "risk": "HIGH",
                    "reason": (
                        "Potential emergency symptom "
                        "reported."
                    )
                }

        if temperature and temperature >= 39:

            return {
                "risk": "HIGH",
                "reason": "Very high temperature reported."
            }

        if pain and pain >= 8:

            return {
                "risk": "HIGH",
                "reason": "Severe pain reported."
            }

        if heart_rate:

            if heart_rate > 120 or heart_rate < 50:

                return {
                    "risk": "MODERATE",
                    "reason": "Abnormal heart rate reported."
                }

        if temperature and temperature >= 38:

            return {
                "risk": "MODERATE",
                "reason": "Elevated temperature reported."
            }

        if pain and pain >= 5:

            return {
                "risk": "MODERATE",
                "reason": "Moderate pain reported."
            }

        return {
            "risk": "LOW",
            "reason": "No predefined concerning indicators detected."
        }