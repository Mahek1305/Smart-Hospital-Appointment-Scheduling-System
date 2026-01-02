# Smart Hospital Appointment Scheduling System

## Project Overview

The Smart Hospital Appointment Scheduling System is a Streamlit-based web application designed to manage and schedule hospital patient appointments efficiently. The system uses Multilevel Queue Scheduling and Priority Queue algorithms to ensure that emergency and critical patients are given higher priority while maintaining fairness for all patients.

This project applies core concepts of Operating Systems and Data Structures to a real-world healthcare problem.

---

## Objectives

* To automate hospital appointment scheduling
* To prioritize patients based on emergency level and disease severity
* To reduce waiting time for critical patients
* To implement Multilevel Queue Scheduling using Priority Queues
* To provide a user-friendly web interface using Streamlit

---

## Features

* Patient registration with personal and disease details
* Emergency-based prioritization (High, Medium, Low)
* Severity-based scheduling within the same emergency level
* Automatic appointment time allocation
* Real-time appointment schedule display
* FIFO-based fair scheduling for same-priority patients
* Option to clear all appointments

---

## Scheduling Logic

The system uses a Priority Queue with the following priority tuple:

(Emergency Priority, -Severity, Arrival Time)

Priority rules:

* High emergency patients are scheduled first
* Higher disease severity gets higher priority
* Earlier arrival time ensures fair FIFO scheduling

---

## Technology Stack

* Programming Language: Python
* Web Framework: Streamlit
* Scheduling Algorithm: Priority Queue (heapq)
* Data Handling: Pandas
* Time Management: datetime
* State Management: Streamlit Session State

---

## How to Run the Project

1. Install the required libraries:

pip install streamlit pandas

2. Run the Streamlit application:

streamlit run app.py

3. Open the application in your browser:

[http://localhost:8501](http://localhost:8501)

---

## Project Structure

Hospital-Appointment-Scheduler/
│
├── app.py
├── README.md

---

## Example Workflow

1. A patient enters their details including disease and emergency level
2. The system assigns a priority based on urgency and severity
3. Emergency patients are scheduled first
4. Appointment times are generated automatically
5. The final appointment schedule is displayed in real time

---

## Advantages

* Efficient hospital queue management
* Faster handling of emergency cases
* Fair scheduling for non-emergency patients
* Scalable and modular system design
* Real-world application of OS scheduling algorithms

---

## Future Enhancements

* Database integration (SQLite/MySQL)
* Doctor-wise appointment scheduling
* Machine learning-based waiting time prediction
* Role-based access (Admin/Receptionist)
* Appointment history and analytics dashboard

---

## Conclusion

This project demonstrates the practical implementation of Operating System scheduling concepts and data structures in a real-world healthcare environment. It highlights efficient resource management, algorithmic thinking, and modern web application development using Python and Streamlit.


