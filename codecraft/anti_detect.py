import cv2
import serial
import time

arduino = serial.Serial("COM3", 9600)
time.sleep(2)

camera = cv2.VideoCapture(0)

previous_state = None

print("Anti Study Lamp started")
print("Put your book in the box")
print("Press Q to stop")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Camera error")
        break

    # Study area
    x1, y1 = 150, 100
    x2, y2 = 500, 400

    area = frame[y1:y2, x1:x2]

    # Detect edges
    gray = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 150)

    # Count detected edges
    edge_count = cv2.countNonZero(edges)

    if edge_count > 5000:
        state = 1
        text = "BOOK/OBJECT DETECTED"
    else:
        state = 0
        text = "AREA EMPTY"

    # Send only when state changes
    if state != previous_state:

        if state == 1:
            arduino.write(b"1")
            print("Object detected -> sent 1")
        else:
            arduino.write(b"0")
            print("Area empty -> sent 0")

        previous_state = state

    # Show the detection area
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

    cv2.putText(
        frame,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow("Anti Study Lamp", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
arduino.close()
cv2.destroyAllWindows()