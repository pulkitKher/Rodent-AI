# Rodent AI Detection and Prevention System

## Project Overview

The **Rodent AI Detection and Prevention System** is an AI + Embedded + IoT based project designed to detect rodents inside a car engine bay and prevent wire damage.
The system uses an ultrasonic sensor to detect movement, activates a webcam, runs a YOLO AI model for rodent detection, and alerts the user using LED, buzzer, and Telegram bot.
The user can activate a rodent repeller either from inside the car or remotely using Telegram.

This project combines Computer Vision, Arduino, Serial Communication, and AI model trained using Roboflow dataset.

---

## Features

* Ultrasonic sensor based motion detection
* Automatic webcam activation
* YOLO rodent detection (Ultralytics)
* Dataset trained using Roboflow
* Telegram bot alert with image + date + time
* LED + buzzer alert inside car
* Arduino UNO hardware communication
* Push button repeller activation
* Telegram remote repeller control
* Safe repeller activation (10 seconds limit)
* Secure token using .env

---

## Technologies Used

* Python
* Ultralytics YOLO (>= 8.0.0)
* OpenCV
* NumPy
* PySerial
* Requests
* Pandas
* Matplotlib
* python-dotenv
* Arduino UNO
* Roboflow Dataset
* Ultrasonic Sensor
* LED + Buzzer
* Push Button
* Repeller module

---

## Project Structure

```
RODENT_AI/
│
├── src/
│   └── detect_webcam.py
│
├── dataset/
│   ├── images/
│   ├── labels/
│
├── weights/
│   └── best.pt
│
├── runs/
├── notebooks/
│
├── .env
├── .gitignore
├── requirements.txt
├── mouse.yaml
├── README.md
```

---

## Installation

### 1. Clone repository

```
git clone https://github.com/your-username/rodent-ai.git
cd rodent-ai
```

### 2. Install requirements

```
pip install -r requirements.txt
```

requirements.txt

```
ultralytics>=8.0.0
opencv-python
numpy
pyserial
requests
pandas
matplotlib
python-dotenv
```

---

## Create .env file

Create file:

```
.env
```

Add:

```
TOKEN=your_telegram_token
CHAT_ID=your_chat_id
```

.env is ignored using .gitignore.

---

## Run the project

```
python src/detect_webcam.py
```

---

## Complete System Working

The system works in multiple stages.

### Step 1 — Motion Detection

* Ultrasonic sensor detects movement inside engine bay
* If no movement → system stays idle
* If movement detected → webcam activated

### Step 2 — AI Detection

* Webcam starts capturing video
* YOLO model detects mouse / rodent
* If no rodent → system stops
* If rodent detected → alert triggered

### Step 3 — Check User Presence

If user is inside car:

* LED ON
* Buzzer ON
* Warning given to driver
* User can press push button
* Repeller activates for 10 seconds

If user not inside car:

* Image captured
* Date and time added
* Image sent to Telegram bot

### Step 4 — Telegram Alert

Telegram sends message with options:

* Activate Repeller
* Ignore

If user selects Activate:

* Command sent to Python
* Python sends serial signal to Arduino
* Repeller ON for 10 seconds

### Step 5 — Repeller Action

* Repeller sound / ultrasonic activated
* Mouse leaves engine bay
* System stops automatically

---

## System Architecture

```
Ultrasonic Sensor
        ↓
Motion Detected
        ↓
Webcam ON
        ↓
YOLO Detection
        ↓
Mouse Found ?
   ↓           ↓
  Yes          No
   ↓
Check User Present
   ↓
Inside Car → LED + Buzzer + Button → Repeller
Outside Car → Telegram Alert → User Command → Repeller
```

---

## Hardware Used

* Arduino UNO
* Ultrasonic Sensor
* LED
* Buzzer
* Push Button
* Repeller module
* Laptop Webcam
* USB Serial communication

Python communicates with Arduino using PySerial.

---

## Model Training

* Dataset created using Roboflow
* Images labeled as mouse / rodent
* Trained using Ultralytics YOLO
* Model saved as best.pt

---

## Output

* Detection image saved
* Telegram alert sent
* Hardware triggered
* Logs generated

---

## Applications

* Car engine rodent prevention
* Smart vehicle safety system
* AI + Embedded project
* IoT surveillance system
* Industrial monitoring

---

## Author

Pulkit Kher
B.Tech CSE
Rodent AI Detection Project


---

## Note

This project is for educational and research purposes.

Secret tokens are stored in .env
.env file is not uploaded to GitHub.
