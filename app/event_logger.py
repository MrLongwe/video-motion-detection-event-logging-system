"""
event_logger.py
handles saving timestamped event images when motion is detected

"""

import cv2
from pathlib import Path
from datetime import datetime

# create a directory to save event images if it doesn't exist
class EventLogger:
    def __init__(self):
        # create events directory if it doesn't exist
        self.events_dir = Path("events")
        self.events_dir.mkdir(exist_ok=True)

    def save_event(self, frame):
        """
        Save a timestamped image of the detected event.
        """

        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        filename = self.events_dir / f"event_{timestamp}.jpg"

        # add a timestamp to the frame
        current_time = datetime.now()
        timestamp_text = current_time.strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(
            frame,
            timestamp_text,
            (10, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )
        cv2.imwrite(str(filename), frame)

        print(f"[EVENT SAVED] {filename}")