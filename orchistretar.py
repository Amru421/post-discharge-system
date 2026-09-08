from .monitoring_agent import MonitoringAgent
from .risk_agent import RiskAssessmentAgent
from .medication_agent import MedicationAgent
from .followup_agent import FollowUpAgent
from .emergency_agent import EmergencyAgent
from .doctor_agent import DoctorAgent


class PostDischargeOrchestrator:

    def __init__(self):

        self.monitoring_agent = MonitoringAgent()

        self.risk_agent = RiskAssessmentAgent()

        self.medication_agent = MedicationAgent()

        self.followup_agent = FollowUpAgent()

        self.emergency_agent = EmergencyAgent()

        self.doctor_agent = DoctorAgent()

    def process(self, patient, data):

        # Agent 1
        monitoring = self.monitoring_agent.analyze(
            data
        )

        # Agent 2
        risk = self.risk_agent.assess(
            data,
            monitoring
        )

        # Agent 3
        medication = self.medication_agent.check(
            patient,
            data.get("medication_status")
        )

        # Agent 4
        followup = self.followup_agent.check(
            patient
        )

        # Agent 5
        emergency = self.emergency_agent.handle(
            patient,
            risk
        )

        # Agent 6
        doctor_summary = self.doctor_agent.create_summary(
            patient,
            monitoring,
            risk,
            medication,
            followup
        )

        return {

            "monitoring": monitoring,

            "risk": risk,

            "medication": medication,

            "followup": followup,

            "emergency": emergency,

            "doctor_summary": doctor_summary
        }