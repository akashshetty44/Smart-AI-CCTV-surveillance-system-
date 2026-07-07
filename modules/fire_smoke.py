"""
=========================================================
 Smart AI CCTV Surveillance System
 Fire & Smoke Detection Module
=========================================================
"""

import cv2
import os
import time
from datetime import datetime
from ultralytics import YOLO
import config

# Load Fire & Smoke Detection Model
model = YOLO(config.FIRE_MODEL)

# Prevent duplicate alerts
last_alert_time = 0
ALERT_INTERVAL = 10  # seconds


def save_fire_image(frame):
    """
    Save screenshot of fire detection
    """
    filename = datetime.now().strftime("fire_%Y%m%d_%H%M%S.jpg")
    filepath = os.path.join(config.SCREENSHOT_FOLDER, filename)

    cv2.imwrite(filepath, frame)
    return filepath


def detect_fire(frame):
    """
    Detect Fire and Smoke
    Returns:
        frame
        fire_detected (bool)
    """

    global last_alert_time

    fire_detected = False

    results = model.predict(
        frame,
        conf=config.CONFIDENCE_THRESHOLD,
        verbose=False
    )

    for result in results:

        for box in result.boxes:

            confidence = float(box.conf[0])

            class_id = int(box.cls[0])

            label = model.names[class_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Orange Bounding Box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                config.ORANGE,
                3
            )

            cv2.putText(
                frame,
                f"{label} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                config.ORANGE,
                2
            )

            fire_detected = True

            current_time = time.time()

            if current_time - last_alert_time > ALERT_INTERVAL:

                save_fire_image(frame)

                last_alert_time = current_time

    return frame, fire_detected
