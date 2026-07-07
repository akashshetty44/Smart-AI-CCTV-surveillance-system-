"""
=========================================================
 Smart AI CCTV Surveillance System
 Person Tracking Module
=========================================================
"""

from ultralytics import YOLO
import cv2
import config

# Load YOLO model
model = YOLO(config.YOLO_MODEL)


class PersonTracker:

    def __init__(self):
        self.total_people = 0
        self.tracked_ids = set()

    def track(self, frame):

        # ByteTrack
        results = model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            classes=[0],          # Person only
            verbose=False,
            conf=config.CONFIDENCE_THRESHOLD
        )

        if len(results) == 0:
            return frame, 0

        result = results[0]

        if result.boxes is None:
            return frame, 0

        boxes = result.boxes

        for box in boxes:

            # Skip if tracker ID isn't assigned yet
            if box.id is None:
                continue

            track_id = int(box.id.item())

            self.tracked_ids.add(track_id)

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            confidence = float(box.conf[0])

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                config.GREEN,
                2
            )

            cv2.putText(
                frame,
                f"ID {track_id}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                config.GREEN,
                2
            )

        self.total_people = len(self.tracked_ids)

        cv2.putText(
            frame,
            f"People Seen : {self.total_people}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            config.BLUE,
            2
        )

        return frame, self.total_people
