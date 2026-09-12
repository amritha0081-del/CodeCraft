import cv2
import serial
import time

# Connect to Arduino
arduino = serial.Serial("COM3", 9600)
time.sleep(2)

# Open camera
camera = cv2.VideoCapture(0)

# Remember previous state
previous_state = None

print("Anti Study Lamp started")
print("Press Q to stop")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Camera not found")
        break

    # Area where you keep the book
    x1, y1 = 150, 100
    x2, y2 = 500, 400

    area = frame[y1:y2, x1:x2]

    # Convert to grayscale
    gray = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY)

    # Detect edges
    edges = cv2.Canny(gray, 80, 150)

    # Count edges
    edge_count = cv2.countNonZero(edges)

    # Decide whether an object is present
    if edge_count > 5000:
        state = 1
        text = "OBJECT DETECTED"
    else:
        state = 0
        text = "NO OBJECT"

    # Send only when state changes
    if state != previous_state:
        if state == 1:
            arduino.write(b"1")
            print("Object detected -> Sent 1")
        else:
            arduino.write(b"0")
            print("No object -> Sent 0")

        previous_state = state

    # Draw detection area
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)
    cv2.putText(frame, text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Anti Study Lamp", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
arduino.close()
cv2.destroyAllWindows()