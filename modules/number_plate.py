"""
=========================================================
 Smart AI CCTV Surveillance System
 Automatic Number Plate Recognition (ANPR)
=========================================================
"""

import cv2
import os
import re
from datetime import datetime
from ultralytics import YOLO
import easyocr
import config

# Load YOLO Number Plate Model
model = YOLO(config.NUMBER_PLATE_MODEL)

# OCR Reader
reader = easyocr.Reader(['en'], gpu=False)


def clean_plate(text):
    """
    Clean OCR output
    """

    text = text.upper()
    text = re.sub(r'[^A-Z0-9]', '', text)

    return text


def save_plate(frame, plate_number):

    filename = datetime.now().strftime("%Y%m%d_%H%M%S")

    filepath = os.path.join(
        config.SCREENSHOT_FOLDER,
        f"{filename}_{plate_number}.jpg"
    )

    cv2.imwrite(filepath, frame)


def detect_number_plate(frame):

    detected_plate = ""

    results = model.predict(
        frame,
        conf=0.40,
        verbose=False
    )

    for result in results:

        for box in result.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            plate = frame[y1:y2, x1:x2]

            ocr = reader.readtext(plate)

            for detection in ocr:

                text = clean_plate(detection[1])

                if len(text) < 6:
                    continue

                detected_plate = text

                save_plate(frame, detected_plate)

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    config.GREEN,
                    2
                )

                cv2.putText(
                    frame,
                    detected_plate,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    config.GREEN,
                    2
                )

    return frame, detected_plate
