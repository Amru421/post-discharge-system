from datetime import date


class FollowUpAgent:

    def check(self, patient):

        if not patient.follow_up_date:

            return {
                "status": "NO_DATE",
                "message": "No follow-up date recorded."
            }

        days = (
            patient.follow_up_date - date.today()
        ).days

        if days < 0:

            return {
                "status": "OVERDUE",
                "message": "Follow-up date has passed."
            }

        if days <= 3:

            return {
                "status": "UPCOMING",
                "message": "Follow-up appointment is due soon."
            }

        return {
            "status": "SCHEDULED",
            "message": "Follow-up appointment is scheduled."
        }