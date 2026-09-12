import serial
import time

arduino = serial.Serial("COM3", 9600)
time.sleep(2)

print("Arduino connected!")

while True:

    command = input("Enter 1 = ON, 0 = OFF, q = quit: ")

    if command == "1":
        arduino.write(b"1")
        print("Sent 1")

    elif command == "0":
        arduino.write(b"0")
        print("Sent 0")

    elif command == "q":
        break

arduino.close()