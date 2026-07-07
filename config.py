"""
=========================================================
 Smart AI CCTV Surveillance System
 Configuration File
=========================================================
"""

import os

# ======================================================
# Camera Settings
# ======================================================

# 0 = Laptop Webcam
# 1 = External Webcam
# OR IP Camera URL
CAMERA_SOURCE = 0

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FPS = 30

# ======================================================
# AI Detection Settings
# ======================================================

CONFIDENCE_THRESHOLD = 0.50
IOU_THRESHOLD = 0.45

# ======================================================
# YOLO Model Paths
# ======================================================

YOLO_MODEL = "models/yolo11n.pt"
WEAPON_MODEL = "models/weapon.pt"
FIRE_MODEL = "models/fire.pt"
NUMBER_PLATE_MODEL = "models/plate.pt"

# ======================================================
# Face Recognition
# ======================================================

FACE_DATASET = "dataset/faces"
UNKNOWN_FACE_FOLDER = "screenshots/unknown_faces"

# ======================================================
# Output Folders
# ======================================================

SCREENSHOT_FOLDER = "screenshots"
VIDEO_FOLDER = "videos"
LOG_FOLDER = "logs"

# ======================================================
# Database
# ======================================================

DATABASE_PATH = "database/surveillance.db"

# ======================================================
# Alert Settings
# ======================================================

ENABLE_EMAIL = False
ENABLE_TELEGRAM = False
ENABLE_SOUND = True

EMAIL = ""
EMAIL_PASSWORD = ""

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

TELEGRAM_TOKEN = ""
TELEGRAM_CHAT_ID = ""

# ======================================================
# Feature Enable / Disable
# ======================================================

ENABLE_INTRUSION = True
ENABLE_WEAPON = True
ENABLE_FIRE = True
ENABLE_FACE = True
ENABLE_CROWD = True
ENABLE_NUMBER_PLATE = True

ENABLE_FIGHT = True
ENABLE_FALL = True
ENABLE_HELMET = True
ENABLE_MASK = True
ENABLE_PPE = True
ENABLE_LOITERING = True
ENABLE_ABANDONED_OBJECT = True
ENABLE_ACCIDENT = True
ENABLE_SPEED_ESTIMATION = True
ENABLE_WRONG_WAY = True
ENABLE_POTHOLE = True

# ======================================================
# Colors (BGR Format)
# ======================================================

GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
ORANGE = (0, 165, 255)
WHITE = (255, 255, 255)

# ======================================================
# Font Settings
# ======================================================

FONT = 0  # cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.7
THICKNESS = 2

# ======================================================
# Create Required Directories Automatically
# ======================================================

folders = [
    SCREENSHOT_FOLDER,
    VIDEO_FOLDER,
    LOG_FOLDER,
    FACE_DATASET,
    UNKNOWN_FACE_FOLDER,
    "database",
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Configuration Loaded Successfully")
