import cv2

def main():
    # Opens or connects to the webcam
    cap = cv2.VideoCapture(0)  

    if not cap.isOpened():
        print("Error: Could not access the camera")
        return
    
    print("Camera accessed successfully. Press ESC to exit")
    
    while True:
        # Capture the latest frame from the camera
        ret, frame = cap.read()  

        if not ret:
            print("Error: Could not read frame")
            break
        
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