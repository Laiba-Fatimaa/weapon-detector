import cv2
import imutils
import datetime
import matplotlib.pyplot as plt

# Load the trained Haar cascade and make sure it actually loaded
gun_cascade = cv2.CascadeClassifier('cascade.xml')
if gun_cascade.empty():
    raise FileNotFoundError("Could not load 'cascade.xml'. Check that it is in the same folder as this script.")

# Open the webcam and make sure it works
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise RuntimeError("Could not open the webcam. Try a different index, e.g. cv2.VideoCapture(1).")

gun_exist = False
detected_frame = None

while True:
    ret, frame = camera.read()
    if not ret or frame is None:
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    guns = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))

    # Draw a box around every detection
    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Timestamp overlay
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 0, 255), 1)

    if len(guns) > 0:
        gun_exist = True
        detected_frame = frame.copy()
        print("Guns detected")
        break

    cv2.imshow("Security Feed", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

# Show the frame where the detection happened (after the camera is released)
if gun_exist and detected_frame is not None:
    plt.imshow(cv2.cvtColor(detected_frame, cv2.COLOR_BGR2RGB))  # OpenCV is BGR, matplotlib expects RGB
    plt.axis("off")
    plt.title("Detection")
    plt.show()
