import cv2
import serial
import time

arduino = serial.Serial("COM3", 9600)
time.sleep(2)

camera = cv2.VideoCapture(0)

print("Anti Study Lamp is running")
print("Press 1 = Relay ON")
print("Press 0 = Relay OFF")
print("Press Q = Exit")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Camera error")
        break

    cv2.imshow("Anti Study Lamp", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("1"):
        arduino.write(b"1")
        print("Relay ON")

    elif key == ord("0"):
        arduino.write(b"0")
        print("Relay OFF")

    elif key == ord("q"):
        break

camera.release()
arduino.close()
cv2.destroyAllWindows()