"""
=========================================================
 Smart AI CCTV Surveillance System
 Crowd Analysis Module
=========================================================
"""

import cv2
from ultralytics import YOLO
import config

# Load YOLO model
model = YOLO(config.YOLO_MODEL)

# Crowd Thresholds
LOW_THRESHOLD = 5
MEDIUM_THRESHOLD = 15
HIGH_THRESHOLD = 30


def detect_crowd(frame):
    """
    Detect and count people in the frame.

    Returns:
        frame
        people_count (int)
        crowd_level (str)
    """

    people_count = 0

    results = model.predict(
        frame,
        conf=config.CONFIDENCE_THRESHOLD,
        classes=[0],  # Person class
        verbose=False
    )

    for result in results:

        for box in result.boxes:

            people_count += 1

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                config.GREEN,
                2
            )

    # Determine crowd density
    if people_count <= LOW_THRESHOLD:
        crowd_level = "LOW"
        color = config.GREEN

    elif people_count <= MEDIUM_THRESHOLD:
        crowd_level = "MEDIUM"
        color = config.YELLOW

    else:
        crowd_level = "HIGH"
        color = config.RED

    # Display crowd information
    cv2.putText(
        frame,
        f"People: {people_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    cv2.putText(
        frame,
        f"Crowd: {crowd_level}",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    # Alert if crowd is high
    if crowd_level == "HIGH":
        cv2.putText(
            frame,
            "⚠ HIGH CROWD DENSITY",
            (20, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            config.RED,
            3
        )

    return frame, people_count, crowd_level
