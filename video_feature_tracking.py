import cv2

# Replace 'video.mp4' with the actual path to your video file
video_path = 'D:\\python\\video.mp4'  # Ensure the correct path with double backslashes
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read the first frame
ret, frame = cap.read()

# Initialize a CSRT tracker
tracker = cv2.TrackerCSRT_create()  # Ensure this is placed after the video opens

# Manually select the region of interest (ROI) for tracking
bbox = cv2.selectROI('Video Frame', frame, False)

# Initialize the tracker with the selected ROI
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()  # Read a frame from the video
    if not ret:
        break  # Exit the loop if there are no more frames

    # Update the tracker for the new frame
    success, bbox = tracker.update(frame)

    if success:
        # Draw a bounding box around the tracked object
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

    # Display the frame with the tracked feature
    cv2.imshow('Tracking', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
