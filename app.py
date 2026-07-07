"""
=========================================================
 Smart AI CCTV Surveillance System
 Main Application
=========================================================
"""

import cv2
from camera.camera import Camera
import config

# ======================================================
# Import AI Modules (Optional until created)
# ======================================================

try:
    from modules.intrusion import detect_intrusion
except ImportError:
    detect_intrusion = None

try:
    from modules.weapon import detect_weapon
except ImportError:
    detect_weapon = None

try:
    from modules.fire_smoke import detect_fire
except ImportError:
    detect_fire = None


def main():

    print("=" * 50)
    print(" SMART AI CCTV SURVEILLANCE SYSTEM ")
    print("=" * 50)

    camera = Camera()

    while True:

        success, frame = camera.read()

        if not success:
            print("Failed to read camera.")
            break

        # -----------------------------
        # Intrusion Detection
        # -----------------------------
        if config.ENABLE_INTRUSION and detect_intrusion:
            frame, intrusion = detect_intrusion(frame)

            if intrusion:
                cv2.putText(
                    frame,
                    "INTRUSION ALERT",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 0, 255),
                    2
                )

        # -----------------------------
        # Weapon Detection
        # -----------------------------
        if config.ENABLE_WEAPON and detect_weapon:
            frame, weapon = detect_weapon(frame)

            if weapon:
                cv2.putText(
                    frame,
                    "WEAPON DETECTED",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 0, 255),
                    2
                )

        # -----------------------------
        # Fire Detection
        # -----------------------------
        if config.ENABLE_FIRE and detect_fire:
            frame, fire = detect_fire(frame)

            if fire:
                cv2.putText(
                    frame,
                    "FIRE DETECTED",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 165, 255),
                    2
                )

        # Display Camera
        cv2.imshow("Smart AI CCTV Surveillance", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q") or key == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
