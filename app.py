import streamlit as st
import heapq
import time
import pandas as pd
from datetime import datetime, timedelta

# ------------------------------
# Page Setup
# ------------------------------
st.set_page_config(page_title="Hospital Appointment Scheduler", layout="wide")

# ------------------------------
# Initialize Session State
# ------------------------------
if "appointment_queue" not in st.session_state:
    st.session_state.appointment_queue = []

# ------------------------------
# Configuration
# ------------------------------
START_TIME = datetime.strptime("09:00", "%H:%M")
APPOINTMENT_DURATION = 15  # minutes

EMERGENCY_PRIORITY = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}

# ------------------------------
# Add Patient Function
# ------------------------------
def add_patient(name, age, disease, emergency, severity):
    arrival_time = time.time()

    priority = (
        EMERGENCY_PRIORITY[emergency],
        -severity,
        arrival_time
    )

    heapq.heappush(
        st.session_state.appointment_queue,
        (priority, name, age, disease, emergency, severity)
    )

# ------------------------------
# Generate Appointment Schedule
# ------------------------------
def generate_schedule():
    schedule = []
    current_time = START_TIME

    sorted_queue = sorted(st.session_state.appointment_queue)

    for item in sorted_queue:
        _, name, age, disease, emergency, severity = item

        schedule.append({
            "Patient Name": name,
            "Age": age,
            "Disease": disease,
            "Emergency Level": emergency,
            "Severity": severity,
            "Appointment Time": current_time.strftime("%I:%M %p")
        })

        current_time += timedelta(minutes=APPOINTMENT_DURATION)

    return schedule

# ------------------------------
# UI
# ------------------------------
st.title("🏥 Smart Hospital Appointment Scheduling System")
st.caption("Multilevel Priority Queue Based Scheduling")

# ------------------------------
# Patient Input Form
# ------------------------------
with st.form("patient_form", clear_on_submit=True):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Patient Name")
        age = st.number_input("Age", 0, 120)
        disease = st.text_input("Disease")

    with col2:
        emergency = st.selectbox("Emergency Level", ["High", "Medium", "Low"])
        severity = st.slider("Disease Severity (1–10)", 1, 10)

    submit = st.form_submit_button("Add Patient")

    if submit:
        if name and disease:
            add_patient(name, age, disease, emergency, severity)
            st.success("Patient added successfully")
        else:
            st.warning("Please fill all required fields")

# ------------------------------
# Display Scheduled Appointments
# ------------------------------
st.subheader("📅 Scheduled Appointments")

schedule = generate_schedule()

if schedule:
    df = pd.DataFrame(schedule)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No patients added yet")

# ------------------------------
# Emergency Highlight
# ------------------------------
st.subheader("🚨 High Emergency Patients")

emergency_cases = [
    p for p in schedule if p["Emergency Level"] == "High"
]

if emergency_cases:
    st.table(emergency_cases)
else:
    st.info("No high emergency cases")

# ------------------------------
# Clear All Data
# ------------------------------
if st.button("❌ Clear All Appointments"):
    st.session_state.appointment_queue.clear()
    st.success("All appointments cleared")
