"""
main.py
Application entry point for the Video Motion Detection Event Logging System.
Starts the video capture from the webcam and runs motion detection.

"""

import cv2
# import the MotionDetector class from motion_detector.py
from motion_detector import MotionDetector
from event_logger import EventLogger
from config import VIDEO_SOURCE

def main():
    # load sample video file for testing
    cap = cv2.VideoCapture(VIDEO_SOURCE)
    if not cap.isOpened():
        print("Error: Could not access the video file")
        return
    
    # initialize the motion detector 
    detector = MotionDetector()
    # initialize the event logger
    logger = EventLogger()

    print("System started. Press ESC to exit")
    
    while True:
        # Capture the latest frame from the camera
        ret, frame = cap.read()  

        if not ret:
            print("Error: Could not read frame")
            break
        
        # Detect motion in the current frame
        frame, motion_detected = detector.detect(frame)

        # Display the frame with motion detection results
        if motion_detected:

            # save the motion detected frame
            logger.save_event(frame)
            
            cv2.putText(
                frame,
                "MOTION DETECTED!",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

        # Display live video feed
        cv2.imshow('Video Motion Detection System', frame)
        
        # Exit when the ESC key is pressed
        if cv2.waitKey(1) == 27:  
            break
    
    # Release the camera
    cap.release()  
    # Close all OpenCV windows
    cv2.destroyAllWindows()  

if __name__ == "__main__":
    main()