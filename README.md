Smart AI CCTV Surveillance System using Deep Learning

Final Year Engineering Project

Overview

The Smart AI CCTV Surveillance System is an AI-powered security solution that performs real-time monitoring using Computer Vision and Deep Learning. The system detects security threats, recognizes faces, identifies vehicles, analyzes crowds, and generates instant alerts.

This project is developed using Python, OpenCV, Ultralytics YOLO, EasyOCR, Face Recognition, Streamlit, and SQLite.

---

Features

- Intrusion Detection
- Weapon Detection (Gun/Knife)
- Fire & Smoke Detection
- Face Recognition
- Unknown Face Detection
- Crowd Counting and Density Analysis
- Person Tracking
- Number Plate Recognition (ANPR)
- Screenshot Capture
- Automatic Video Recording
- SQLite Event Logging
- Telegram Alerts
- Email Alerts
- Live Dashboard
- Multi-Camera Support (Future Scope)

---

Technology Stack

Technology| Purpose
Python| Programming Language
OpenCV| Image & Video Processing
Ultralytics YOLO| Object Detection
EasyOCR| Number Plate Recognition
Face Recognition| Face Identification
Streamlit| Dashboard
SQLite| Database
NumPy| Numerical Processing

---

Project Structure

Smart_AI_CCTV/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── camera/
│   └── camera.py
│
├── modules/
│   ├── intrusion.py
│   ├── weapon.py
│   ├── fire_smoke.py
│   ├── face_recognition.py
│   ├── crowd_analysis.py
│   ├── number_plate.py
│   ├── tracker.py
│   ├── alerts.py
│   ├── recording.py
│   └── database.py
│
├── models/
├── dataset/
├── dashboard/
├── database/
├── logs/
├── screenshots/
└── videos/

---

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/Smart_AI_CCTV.git
cd Smart_AI_CCTV

Install the required packages:

pip install -r requirements.txt

Download the required AI models and place them in the "models/" directory:

- yolo11n.pt
- weapon.pt
- fire.pt
- plate.pt

---

Run the Project

python app.py

---

Future Enhancements

- Fight Detection
- Fall Detection
- Helmet Detection
- PPE Detection
- Parking Violation Detection
- Wrong-Way Vehicle Detection
- Speed Estimation
- Accident Detection
- Loitering Detection
- Heat Map Generation
- Cloud Backup
- Mobile Application
- Voice Assistant
- AI Analytics Dashboard

---

Expected Output

- Detects people in real time.
- Identifies intrusions across virtual boundaries.
- Detects weapons, fire, and smoke.
- Recognizes known and unknown faces.
- Reads vehicle number plates.
- Counts people and analyzes crowd density.
- Stores events in the database.
- Captures screenshots and records videos.
- Sends alerts to users.

---

Author

Akash B R

Final Year Engineering Project

---

License

This project is developed for educational and research purposes.
