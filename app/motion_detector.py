"""
motion_detector.py
Contains motion detection logic for the Video Motion Detection Event Logging System.
Uses frame differencing and contour analysis.

"""

import cv2

class MotionDetector:
    def __init__(self, min_area=500):
        """
        min_area determines how large a moving a moving object must be to be considered motion.
        """
        self.min_area = min_area
        self.previous_frame = None

    def detect(self, frame):
        """
        Detects motion and draws bounding boxes around moving regions
        """
        # convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # apply Gaussian blur to reduce noise and improve detection
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # first frame becomes our baseline
        if self.previous_frame is None:
            self.previous_frame = gray
            return frame, False

        # compare current frame against previous frame
        frame_delta = cv2.absdiff(self.previous_frame, gray)

        # convert differences into a binary image (thresholding)
        thresh = cv2.threshold(
            frame_delta,
            25,
            255,
            cv2.THRESH_BINARY
        )[1]

        # fill small gaps
        thresh = cv2.dilate(thresh, None, iterations=2)
        
        # find contours of the thresholded image
        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        motion_detected = False

        for contour in contours:

            # ignore tiny movements by checking the area of the contour
            if cv2.contourArea(contour) < self.min_area:
                continue

            motion_detected = True

            # draw a bounding box around the detected motion
            x, y, w, h = cv2.boundingRect(contour)
        
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        self.previous_frame = gray

        return frame, motion_detected