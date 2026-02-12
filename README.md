## AI-Based Automotive Rodent Detection and Prevention System

An AI-powered real-time rodent detection and prevention system for automobiles.  
The system detects rodents inside car engine compartments using a YOLO-based object detection model and activates a hardware deterrence mechanism via ESP32.

______________________________________________________________________________
## Problem Statement

Rodents often enter vehicle engine compartments and damage wiring systems, leading to costly repairs and safety risks.

This project provides:
- Real-time rodent detection
- Driver alert system
- Ultrasonic rodent repeller activation
- Mobile notification system

_______________________________________________________________________________

## System Architecture

Laptop Webcam
        ↓
YOLO Object Detection
        ↓
If Mouse Detected:
   - Send Signal to ESP32
   - Send Telegram Alert
   - Log Event
        ↓
ESP32:
   - LED ON
   - Buzzer ON
   - Manual Button Activation
   - Ultrasonic Repeller ON

_______________________________________________________________________________

## Technologies Used

- Python
- YOLO (Ultralytics)
- OpenCV
- ESP32
- PySerial
- Telegram Bot API

_______________________________________________________________________________

## Project Structure

Rodent_AI/
│
├── src/
│ ├── detect_webcam.py
│ ├── hardware_serial.py
│ ├── telegram_alert.py
│
├── dataset/ (not included in repo)
├── weights/ (not included in repo)
│
├── logs/
├── mouse.yaml
├── requirements.txt
└── README.md


_______________________________________________________________________________

## Features

✔ Real-time mouse detection using YOLO  
✔ Hardware integration with ESP32  
✔ Ultrasonic rodent repeller activation  
✔ Telegram mobile notification  
✔ Event logging system  
✔ Cooldown logic to prevent alert spam  

_______________________________________________________________________________

## Hardware Requirements

- ESP32 Development Board  
- Ultrasonic Piezo (40kHz recommended)  
- Active Buzzer  
- LED + Resistor  
- Push Button  
- MOSFET (if using 12V ultrasonic module)  
- Breadboard & Jumper wires  

_______________________________________________________________________________

## Installation & Setup

### 1️ Clone Repository



git clone https://github.com/pulkitkher/Rodent_AI.git

cd RodentAI_System


### 2️ Create Conda Environment



conda create -p venv python=3.12 -y
conda activate venv/


### 3️ Install Requirements



pip install -r requirements.txt


### 4️ Add Model Weights

Download trained `best.pt` and place inside:



weights/best.pt


### 5️ Run System



python src/detect_webcam.py


Press `q` to exit.

_______________________________________________________________________________

## Logging

Detection events are stored in:



logs/events.csv


Format:
Date | Time | Event | Confidence

_______________________________________________________________________________

## Mobile Notification

Telegram Bot API is used for real-time alerts.

Update inside `telegram_alert.py`:



TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"


_______________________________________________________________________________

## Future Improvements

- Replace laptop with Jetson Nano for standalone deployment
- Add temperature & motion sensors
- Develop Android dashboard app
- Cloud-based detection history storage

_______________________________________________________________________________

## Project Outcome

This system demonstrates integration of:

- Computer Vision
- Deep Learning
- Embedded Systems
- IoT Communication
- Automotive Safety Applications

_______________________________________________________________________________


