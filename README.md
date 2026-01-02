🏥 Smart Hospital Appointment Scheduling System

A Streamlit-based web application that intelligently schedules hospital patient appointments using Multilevel Queue Scheduling and Priority Queue algorithms.
The system ensures emergency and critical patients are prioritized, while maintaining fairness for non-emergency cases.

📌 Project Overview

Hospitals often face challenges in managing patient appointments efficiently, especially when multiple patients arrive with varying levels of urgency.
This project addresses the problem by implementing an automated, priority-based scheduling system that:

Collects patient details (disease, emergency level, severity)

Assigns appointment slots dynamically

Prioritizes emergency and critical patients

Displays a real-time scheduled appointment list

🎯 Objectives

To implement Multilevel Queue Scheduling in a real-world healthcare scenario

To use Priority Queues for efficient appointment allocation

To reduce patient waiting time for emergency cases

To provide an interactive and user-friendly hospital scheduling system

⚙️ System Features

📋 Patient registration with disease details

🚨 Emergency-level based prioritization (High / Medium / Low)

📊 Severity-based scheduling within the same emergency level

⏱ Automatic appointment time allocation

🔁 Fair scheduling using FIFO for same-priority patients

📅 Real-time appointment schedule display

❌ Option to clear all appointments

🧠 Scheduling Logic

The system uses a Priority Queue (heapq) with the following priority tuple:

(Emergency Priority, -Severity, Arrival Time)

Priority Rules:

High Emergency → Scheduled first

Higher severity → Higher priority

Earlier arrival → FIFO order

🏗️ Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
Scheduling Algorithm	Priority Queue (heapq)
Data Handling	Pandas
Time Management	datetime
State Management	Streamlit Session State
🖥️ Application Interface

The application provides:

A patient entry form

A dynamically updated appointment schedule

A separate section highlighting high-emergency patients

🚀 How to Run the Project
1️⃣ Install Dependencies
pip install streamlit pandas

2️⃣ Run the Application
streamlit run app.py

3️⃣ Open in Browser
http://localhost:8501

📂 Project Structure
Hospital-Appointment-Scheduler/
│
├── app.py          # Main Streamlit application
├── README.md       # Project documentation

🧪 Example Use Case

A patient with high emergency & severe condition is added

A patient with low emergency & mild condition is added

The system schedules the emergency patient first

Appointment times are generated automatically

📈 Advantages

Efficient handling of hospital queues

Reduced waiting time for critical patients

Scalable and extensible system design

Suitable for real-world hospital environments

🔮 Future Enhancements

Integration with SQLite / MySQL database

Doctor-wise appointment scheduling

ML-based waiting time prediction

Role-based login (Admin / Receptionist)

Appointment history and analytics dashboard

📄 Resume Description (Ready to Use)

Smart Hospital Appointment Scheduling System

Developed a Streamlit-based web application using Priority Queue and Multilevel Scheduling algorithms to automate hospital appointment management.

Implemented emergency and severity-based prioritization to ensure critical patients receive timely appointments.

Designed a fair and efficient scheduling mechanism using FIFO-based priority handling.

Tech Stack: Python, Streamlit, heapq, Pandas

🙌 Conclusion

This project demonstrates the practical application of Operating System scheduling concepts, data structures, and web application development in the healthcare domain.
It serves as a strong major project showcasing algorithmic thinking and real-world problem-solving skills.
