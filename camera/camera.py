"""
=========================================================
 Smart AI CCTV Surveillance System
 Camera Module
=========================================================
"""

import cv2
from config import CAMERA_SOURCE, FRAME_WIDTH, FRAME_HEIGHT, FPS


class Camera:
    def __init__(self, source=CAMERA_SOURCE):
        self.source = source
        self.cap = cv2.VideoCapture(source)

        if not self.cap.isOpened():
            raise Exception(f"Unable to open camera: {source}")

        # Camera Settings
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, FPS)

    def read(self):
        """
        Read one frame from the camera.
        Returns:
            success (bool), frame (numpy.ndarray)
        """
        success, frame = self.cap.read()

        if not success:
            return False, None

        return True, frame

    def get_resolution(self):
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return width, height

    def get_fps(self):
        return self.cap.get(cv2.CAP_PROP_FPS)

    def is_open(self):
        return self.cap.isOpened()

    def release(self):
        if self.cap.isOpened():
            self.cap.release()


if __name__ == "__main__":

    camera = Camera()

    print("Camera Started")
    print("Resolution:", camera.get_resolution())
    print("FPS:", camera.get_fps())

    while True:

        success, frame = camera.read()

        if not success:
            break

        cv2.putText(
            frame,
            "Smart AI CCTV",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        cv2.imshow("Camera Test", frame)

        key = cv2.waitKey(1)

        if key == 27 or key == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()
