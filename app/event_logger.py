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

        cv2.imwrite(str(filename), frame)

        print(f"[EVENT SAVED] {filename}")