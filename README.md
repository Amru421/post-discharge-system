# post-discharge-system

# 🏥 Agentic AI-Based Post-Discharge Patient Care Management System

## 📌 Overview

The **Agentic AI-Based Post-Discharge Patient Care Management System** is an AI-assisted healthcare platform designed to support patients after hospital discharge.

The system uses a **multi-agent architecture** to monitor patient-reported health information, assess predefined risk indicators, track medications and follow-up appointments, and assist healthcare providers with patient summaries and alerts.

The goal is to improve **post-discharge monitoring, timely follow-up, medication adherence, and care coordination** while reducing the possibility of complications and avoidable readmissions.

> ⚠️ **Medical Safety Notice:** This project is a prototype for educational and demonstration purposes. It does not provide medical diagnosis, replace healthcare professionals, or independently prescribe/change medication.

---

# 🎯 Objectives

* Monitor patients after hospital discharge.
* Collect daily health information.
* Identify predefined concerning health indicators.
* Classify monitoring status into LOW, MODERATE, or HIGH risk.
* Track medication adherence.
* Monitor follow-up appointments.
* Generate emergency alerts for predefined warning symptoms.
* Provide doctors with concise patient summaries.
* Demonstrate how multiple AI agents can collaborate in healthcare workflows.

---

# 🤖 Agentic AI Architecture

The system consists of multiple specialized agents coordinated by an **Agent Orchestrator**.

```text
                    PATIENT / CAREGIVER
                           │
                           ▼
                  ┌──────────────────┐
                  │ Django Web App   │
                  └────────┬─────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Monitoring Agent   │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Risk Assessment    │
                 │ Agent              │
                 └─────────┬──────────┘
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
                  LOW /       CONCERNING /
                MODERATE        HIGH RISK
                    │             │
                    │             ▼
                    │      Emergency Agent
                    │             │
                    └──────┬──────┘
                           ▼
                ┌─────────────────────┐
                │ Medication Agent    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Follow-Up Agent     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Doctor Assistant    │
                │ Agent               │
                └──────────┬──────────┘
                           │
                           ▼
                    DOCTOR DASHBOARD
```

---

# 🧠 AI Agents

## 1. Monitoring Agent

Responsible for analyzing the health information entered by the patient or caregiver.

### Inputs

* Temperature
* Blood pressure
* Heart rate
* Blood glucose
* Pain level
* Symptoms
* Medication status
* General health

### Output

```text
NORMAL
or
ATTENTION REQUIRED
```

---

## 2. Risk Assessment Agent

Analyzes predefined health indicators and assigns a monitoring risk level.

```text
LOW RISK
MODERATE RISK
HIGH RISK
```

The risk assessment is based on prototype rules and should not be interpreted as a clinical diagnosis.

---

## 3. Medication Agent

Tracks prescribed medications.

It provides information such as:

* Medicine name
* Dosage
* Frequency
* Duration
* Taken/missed status

The system does **not automatically modify medication dosage or prescribe medicines**.

---

## 4. Follow-Up Agent

Monitors the patient's follow-up appointment.

It identifies:

```text
Scheduled
Upcoming
Overdue
No Follow-Up Date
```

---

## 5. Emergency Agent

Checks for predefined emergency indicators.

Examples include:

* Chest pain
* Difficulty breathing
* Severe bleeding
* Loss of consciousness
* Severe breathlessness

When a predefined emergency condition is detected, the system displays:

> **URGENT: Please contact your healthcare provider or emergency medical services.**

---

## 6. Doctor Assistant Agent

Combines information from the other agents and generates a concise patient status summary.

Example:

```text
Patient Status Summary

Risk Level: MODERATE

Monitoring:
Elevated temperature reported.

Medication:
Medication status is ON TRACK.

Follow-Up:
Appointment is scheduled soon.

The healthcare provider should review the
patient's reported information.
```

---

# 🔄 Agent Workflow

The complete workflow is:

```text
1. Patient enters health information
              ↓
2. Monitoring Agent analyzes the data
              ↓
3. Risk Assessment Agent evaluates indicators
              ↓
4. Medication Agent checks medication status
              ↓
5. Follow-Up Agent checks appointment status
              ↓
6. Emergency Agent checks for urgent indicators
              ↓
7. Doctor Agent creates patient summary
              ↓
8. Doctor Dashboard displays the result
```

The **Orchestrator** coordinates communication between these agents.

---

# 🏗️ Project Structure

```text
post_discharge_ai/
│
├── manage.py
│
├── post_discharge_ai/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── patients/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   └── views.py
│
├── agents/
│   ├── __init__.py
│   ├── monitoring_agent.py
│   ├── risk_agent.py
│   ├── medication_agent.py
│   ├── followup_agent.py
│   ├── emergency_agent.py
│   ├── doctor_agent.py
│   └── orchestrator.py
│
├── templates/
│   └── patients/
│       ├── home.html
│       ├── register.html
│       ├── patient_dashboard.html
│       ├── monitoring.html
│       └── doctor_dashboard.html
│
├── static/
│   └── css/
│       └── style.css
│
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

# 💻 Technologies Used

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| Python     | Core programming language          |
| Django     | Backend web framework              |
| SQLite     | Database                           |
| HTML       | Frontend structure                 |
| CSS        | User interface                     |
| JavaScript | Frontend interactions              |
| AI Agents  | Monitoring and care coordination   |
| LLM        | Optional intelligent summarization |

---

# 📋 Main Features

### Patient Module

* Patient registration
* Patient ID
* Personal information
* Diagnosis information
* Admission and discharge dates
* Treating doctor
* Discharge instructions

### Health Monitoring

* Temperature
* Blood pressure
* Heart rate
* Blood glucose
* Pain level
* Symptoms
* General health
* Medication status

### Risk Management

* LOW RISK
* MODERATE RISK
* HIGH RISK
* Emergency alerts

### Medication Management

* Medicine details
* Dosage
* Frequency
* Duration
* Medication adherence

### Follow-Up Management

* Follow-up date
* Upcoming appointment
* Overdue appointment
* Appointment reminders

### Doctor Dashboard

* Patient list
* Patient monitoring history
* Risk status
* Medication status
* Follow-up status
* AI-generated summary

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

Navigate into the project:

```bash
cd post_discharge_ai
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 3. Install dependencies

```bash
pip install django
```

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

---

# 🗄️ 4. Create the database

Run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

---

# ▶️ 5. Start the server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

# 👨‍⚕️ Application Flow

### Step 1 — Register Patient

The healthcare provider enters:

```text
Patient ID
Name
Age
Gender
Contact
Diagnosis
Admission Date
Discharge Date
Treating Doctor
```

---

### Step 2 — Add Discharge Information

The system stores:

```text
Final Diagnosis
Procedures
Medications
Diet Instructions
Activity Restrictions
Warning Signs
Doctor Instructions
Follow-Up Date
```

---

### Step 3 — Patient Monitoring

The patient/caregiver enters daily information:

```text
Temperature
Blood Pressure
Heart Rate
Blood Glucose
Pain Level
Symptoms
Medication Status
General Health
```

---

### Step 4 — Agent Processing

The Orchestrator sends the information to the specialized agents.

```text
Patient Data
     ↓
Monitoring Agent
     ↓
Risk Agent
     ↓
Medication Agent
     ↓
Follow-Up Agent
     ↓
Emergency Agent
     ↓
Doctor Agent
```

---

### Step 5 — Result

The patient receives a monitoring status and the doctor can review the information through the dashboard.

---

# 🧪 Example

### Input

```text
Temperature: 38.5°C
Heart Rate: 110 bpm
Pain Level: 6
Symptoms: Fever and weakness
Medication: Taken
```

### Agent Output

```text
Monitoring Agent:
ATTENTION REQUIRED

Risk Agent:
MODERATE RISK

Medication Agent:
ON TRACK

Follow-Up Agent:
SCHEDULED

Emergency Agent:
No emergency alert triggered.

Doctor Agent:
Patient reported elevated temperature
and moderate pain. Review symptoms and
follow the treating healthcare provider's
instructions.
```

---

# 🚨 Emergency Example

### Input

```text
Symptoms:
Chest pain and difficulty breathing
```

### Agent Workflow

```text
Monitoring Agent
       ↓
Risk Assessment Agent
       ↓
HIGH RISK
       ↓
Emergency Agent
       ↓
URGENT ALERT
```

The system displays:

```text
URGENT:

Please contact your healthcare provider
or emergency medical services.
```

---

# 🔐 Security Considerations

Healthcare information is sensitive. A production implementation should include:

* User authentication
* Role-based access control
* Secure password storage
* HTTPS
* Database encryption where appropriate
* Audit logging
* Secure API keys
* Input validation
* Protection against CSRF/XSS/SQL injection
* Minimum necessary data collection
* Appropriate healthcare privacy/compliance controls

The current prototype should **not be used for real patient care without proper clinical validation, security review, and regulatory/compliance assessment**.

---

# 🌟 Advantages

* Continuous post-discharge monitoring
* Multi-agent architecture
* Automated risk screening based on predefined indicators
* Medication adherence tracking
* Follow-up monitoring
* Emergency warning mechanism
* Doctor-focused patient summaries
* Scalable architecture for additional agents
* Reduces repetitive monitoring tasks
* Demonstrates practical Agentic AI coordination

---

# 🔮 Future Scope

## Wearable Integration

```text
Smartwatch / Wearable
        ↓
Vital Signs
        ↓
Monitoring Agent
        ↓
Risk Agent
        ↓
Doctor Dashboard
```

## Mobile Application

A dedicated Android/iOS application can allow patients to submit health information from anywhere.

## Voice Assistant

Patients could report symptoms through voice.

## Multilingual Support

Support for languages such as:

* English
* Kannada
* Hindi
* Tamil
* Telugu

## Hospital Integration

Future versions could integrate with hospital Electronic Medical Record systems.

## Notification System

The system can be extended with:

* SMS
* Email
* Push notifications

for reminders and alerts.

---

# 📊 Expected Impact

The proposed system aims to improve:

```text
Post-Discharge Monitoring
          ↓
Medication Adherence
          ↓
Follow-Up Compliance
          ↓
Early Identification of Concerning Indicators
          ↓
Better Care Coordination
```

It is designed to **assist healthcare providers**, rather than replace them.

---

# 🎓 Use Case

This project is suitable for:

* Agentic AI projects
* College mini projects
* Final-year projects
* Hackathons
* Healthcare AI demonstrations
* AI/ML portfolios
* Django projects

---

# 👥 User Roles

### Patient / Caregiver

```text
View discharge instructions
        ↓
View medications
        ↓
Submit health information
        ↓
View monitoring status
        ↓
Receive alerts/reminders
```

### Doctor

```text
View patients
        ↓
Review monitoring records
        ↓
View risk status
        ↓
Review medication adherence
        ↓
Review follow-up status
        ↓
Review AI-generated summary
```

---

# 🧩 Future Agent Expansion

The architecture allows additional agents to be added later:

```text
Nutrition Agent
       │
       ▼
Mental Wellness Support Agent
       │
       ▼
Appointment Scheduling Agent
       │
       ▼
Notification Agent
       │
       ▼
Report Generation Agent
```

This makes the architecture extensible for future healthcare workflows.

---

# ⚠️ Disclaimer

This software is an **educational prototype** demonstrating Agentic AI concepts in post-discharge healthcare monitoring.

It is not intended to:

* Diagnose medical conditions
* Replace doctors or nurses
* Prescribe medication
* Modify medication dosage
* Provide emergency medical treatment

Patients experiencing a medical emergency should contact appropriate emergency medical services or a healthcare professional.

---

# 👩‍💻 Author

**Post-Discharge Patient Care Management System**

Built using:

```text
Python
Django
SQLite
HTML
CSS
JavaScript
Agentic AI
```

---

# ⭐ Project Vision

> **Use Agentic AI to support continuous post-discharge monitoring and improve communication between patients and healthcare providers.**
