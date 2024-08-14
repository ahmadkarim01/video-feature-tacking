import cv2
import numpy as np

# Load the video
video_path = r'D:\python/video.mp4'  # Use raw string to handle backslashes
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"Error: Unable to open video at {video_path}")
else:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or frame is None:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(gray_frame, maxCorners=100, qualityLevel=0.01, minDistance=10)
        if corners is not None:
            corners = np.int32(corners)  # Convert corners to integer
            for corner in corners:
                x, y = corner.ravel()
                cv2.rectangle(frame, (x - 10, y - 10), (x + 10, y + 10), (0, 255, 0), 2)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()