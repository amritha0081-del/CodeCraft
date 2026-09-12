<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# [Anti-Study Lamp] 🎯


## Basic Details
### Team Name: [CodeCraft]


### Team Members
- Team Lead: [Amritha P M] - [College Of engineering Munnar]
- Member 2: [Amritha P M ] - [College Of engineering Munnar]
- Member 3: [Ahalya Preman] - [College Of engineering Munnar]

### Project Description
[An AI based smart lamp that uses a camera and python to detect whether a book is open or closed and controls the lamp using Arduino and a Relay]

### The Problem (that doesn't exist)
[People often forget to switch off a lamp when they stop studying, wasting electricity]

### The Solution (that nobody asked for)
[]

## Technical Details
### Technologies/Components Used
For Software:
- [PYTHON]
- [ARDUINO IDE]
- [OPENCV]
- [Arduino board,Relay module,Webcam,laptop,USB,Serial monitor]

For Hardware:
- [Arduino board ]
- [Relay module]
- [LED strip]


# Installation
[pip install opencv-python
pip install pyserial]

# Run
[python anti_detect.py]

### Project Documentation
For Software:

# Screenshots (Add at least 3)
[]<img width="1107" height="901" alt="anti detect py" src="https://github.com/user-attachments/assets/2ee881b7-f684-4232-b892-74d76b95a679" />
"This screenshot shows the working of our Anti-Study Lamp. The laptop camera monitors the defined study area. When the book is detected inside the marked area, the Python program identifies the object and sends the signal 1 to the Arduino. The Arduino then activates the relay, which switches the LED lamp OFF. When the book is removed, the program sends 0, and the relay switches the LED lamp ON."

# Diagrams
📷 Camera
     ↓
📖 Book Detection
     ↓
🐍 Python + OpenCV
     ↓
🔌 Serial Communication
     ↓
🤖 Arduino (COM3)
     ↓
⚡ Relay Module
     ↓
💡 Study Lamp
Workflow of the Anti-Study Lamp: The camera detects the book’s state, Python processes the image and sends a command to Arduino, which controls the lamp through a relay.

For Hardware:
# Schematic & Circuit
<img width="870" height="770" alt="circuit" src="https://github.com/user-attachments/assets/f676d060-f5be-452d-8a43-a95b1e371c99" />

# Build Photos
<img width="960" height="1280" alt="components" src="https://github.com/user-attachments/assets/7d2dc2d8-60c2-4893-acab-9f38cbed7f4c" />
Arduino board, Relay module, LED strip, Battery supply, USB cable

![Build]
<img width="576" height="276" alt="build anti study lamp" src="https://github.com/user-attachments/assets/429fd696-635d-4d01-a9c6-02029a70aea2" />
Build Process
1. Collect the components
Arduino Uno,Relay module,LED bulb/lamp,USB cable
2. Connect the relay
Connect VCC → 5V,Connect GND → GND,Connect IN → an Arduino digital pin.
the relay acts as an electronic switch for the lamp.
3. Connect the LED lamp
Connect the lamp through the relay's switching terminals.
4.Upload the Arduino program
Write the program in Arduino IDE
Upload it to the Arduino through USB.
The program continuously checks the sensor.
Give the required input to the sensor.
Arduino processes the sensor value.
Arduino sends a signal to the relay.
The relay switches the LED lamp ON/OFF according to the programmed condition.
![final process]
<img width="720" height="1280" alt="anti study lamp book open" src="https://github.com/user-attachments/assets/20614ab4-552f-4613-aa32-b61fd6442bf8" />
Book opens light off
<img width="720" height="1280" alt="anti study lamp book close" src="https://github.com/user-attachments/assets/6116cc60-5146-4770-833d-bf20f48e69e7" />
Book close light on
Simple working flow:Sensor → Arduino → Relay → LED Lamp
### Project Demo
# Video:
https://github.com/user-attachments/assets/ebf6aac3-68df-44a1-b9ac-0b60b3ac746f
## Team Contributions
- [Amritha P M]: [Hardware]
- [Ahalya Preman]: [Software]
---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



