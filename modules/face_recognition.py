"""
=========================================================
 Smart AI CCTV Surveillance System
 Face Recognition Module
=========================================================
"""

import os
import cv2
import face_recognition
from datetime import datetime
import config

known_face_encodings = []
known_face_names = []


def load_known_faces():

    if not os.path.exists(config.FACE_DATASET):
        return

    for person in os.listdir(config.FACE_DATASET):

        person_folder = os.path.join(config.FACE_DATASET, person)

        if not os.path.isdir(person_folder):
            continue

        for image_name in os.listdir(person_folder):

            image_path = os.path.join(person_folder, image_name)

            image = face_recognition.load_image_file(image_path)

            encodings = face_recognition.face_encodings(image)

            if len(encodings) > 0:

                known_face_encodings.append(encodings[0])
                known_face_names.append(person)


load_known_faces()


def save_unknown_face(frame):

    filename = datetime.now().strftime(
        "unknown_%Y%m%d_%H%M%S.jpg"
    )

    filepath = os.path.join(
        config.UNKNOWN_FACE_FOLDER,
        filename
    )

    cv2.imwrite(filepath, frame)


def recognize_faces(frame):

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    locations = face_recognition.face_locations(rgb)

    encodings = face_recognition.face_encodings(
        rgb,
        locations
    )

    for (top, right, bottom, left), encoding in zip(
            locations,
            encodings):

        matches = face_recognition.compare_faces(
            known_face_encodings,
            encoding,
            tolerance=0.5
        )

        name = "Unknown"

        if True in matches:

            index = matches.index(True)

            name = known_face_names[index]

            color = config.GREEN

        else:

            color = config.RED

            save_unknown_face(frame)

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            color,
            2
        )

        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    return frame
