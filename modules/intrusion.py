"""
=========================================================
 Smart AI CCTV Surveillance System
 Intrusion Detection Module
=========================================================
"""

import cv2
import os
from datetime import datetime
from ultralytics import YOLO

import config

# Load YOLO model once
model = YOLO(config.YOLO_MODEL)

# Virtual security line (can be adjusted)
LINE_Y = 350


def save_intrusion(frame):
    """
    Save a screenshot when intrusion is detected.
    """

    filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")
    filepath = os.path.join(config.SCREENSHOT_FOLDER, filename)

    cv2.imwrite(filepath, frame)

    return filepath


def detect_intrusion(frame):
    """
    Detects people crossing the virtual line.
    Returns:
        frame
        intrusion_detected (True/False)
    """

    intrusion = False

    results = model.predict(
        frame,
        conf=config.CONFIDENCE_THRESHOLD,
        verbose=False
    )

    # Draw the virtual boundary
    cv2.line(
        frame,
        (0, LINE_Y),
        (frame.shape[1], LINE_Y),
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        "Security Line",
        (10, LINE_Y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            # Person class in COCO
            if cls != 0:
                continue

            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            center_y = (y1 + y2) // 2

            color = config.GREEN

            if center_y > LINE_Y:

                intrusion = True
                color = config.RED

                save_intrusion(frame)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            cv2.putText(
                frame,
                f"Person {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

            cv2.circle(
                frame,
                ((x1 + x2) // 2, center_y),
                5,
                color,
                -1
            )

    return frame, intrusion
