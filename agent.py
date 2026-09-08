class MonitoringAgent:

    def analyze(self, data):

        result = {
            "status": "NORMAL",
            "observations": []
        }

        temperature = data.get("temperature")
        heart_rate = data.get("heart_rate")
        pain = data.get("pain_level")

        if temperature is not None:
            if temperature >= 39:
                result["observations"].append(
                    "High temperature reported."
                )

            elif temperature >= 38:
                result["observations"].append(
                    "Elevated temperature reported."
                )

        if heart_rate is not None:

            if heart_rate > 120:
                result["observations"].append(
                    "Heart rate is elevated."
                )

            elif heart_rate < 50:
                result["observations"].append(
                    "Heart rate is low."
                )

        if pain is not None:

            if pain >= 8:
                result["observations"].append(
                    "Severe pain reported."
                )

            elif pain >= 5:
                result["observations"].append(
                    "Moderate pain reported."
                )

        if result["observations"]:
            result["status"] = "ATTENTION_REQUIRED"

        return result