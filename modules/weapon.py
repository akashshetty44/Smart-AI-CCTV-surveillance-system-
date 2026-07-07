"""
=========================================================
 Smart AI CCTV Surveillance System
 Weapon Detection Module
=========================================================
"""

import cv2
import os
from datetime import datetime
from ultralytics import YOLO

import config

# Load custom weapon detection model
model = YOLO(config.WEAPON_MODEL)


def save_weapon(frame):
    """
    Save screenshot when a weapon is detected.
    """

    filename = datetime.now().strftime("weapon_%Y%m%d_%H%M%S.jpg")
    filepath = os.path.join(config.SCREENSHOT_FOLDER, filename)

    cv2.imwrite(filepath, frame)

    return filepath


def detect_weapon(frame):
    """
    Detect weapons in a frame.

    Returns:
        frame
        weapon_detected (True/False)
    """

    weapon_detected = False

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

            # Red bounding box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                config.RED,
                3
            )

            text = f"{label} {confidence:.2f}"

            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                config.RED,
                2
            )

            weapon_detected = True

            # Save evidence image
            save_weapon(frame)

    return frame, weapon_detected
