import cv2
import os
import csv
from datetime import datetime
from ultralytics import YOLO
from hardware_serial import send_signal
from telegram_alert import send_alert
import time

model = YOLO("weights/best.pt")
cap = cv2.VideoCapture(0)

os.makedirs("logs", exist_ok=True)

last_alert_time = 0
cooldown = 120  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.6)
    annotated = results[0].plot()

    detected = len(results[0].boxes) > 0

    if detected:
        send_signal(1)

        current_time = time.time()
        if current_time - last_alert_time > cooldown:
            send_alert()
            last_alert_time = current_time

        
            with open("logs/events.csv", "a", newline="") as file:
                writer = csv.writer(file)

                
                confidence = float(results[0].boxes.conf[0])

                writer.writerow([
                    datetime.now().strftime("%Y-%m-%d"),
                    datetime.now().strftime("%H:%M:%S"),
                    "Mouse Detected",
                    round(confidence, 3)
                ])

    else:
        send_signal(0)

    cv2.imshow("Rodent Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


