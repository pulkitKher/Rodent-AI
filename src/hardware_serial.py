from ultralytics import YOLO
import cv2
import serial
import time
import requests
from datetime import datetime

TOKEN="8732225121:AAFwbCmDjSC0ydP0VZjBJHB7nNUlVjczqJQ"
CHAT_ID="6591002982"

arduino=serial.Serial("COM11",9600,timeout=1)

model=YOLO("best.pt")

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

last_update=None

def send_alert(image):

    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message=f"""
⚠ Rodent detected
Time: {now}
"""

    keyboard={
    "inline_keyboard":[
    [{"text":"Activate Repeller","callback_data":"repel"}],
    [{"text":"Ignore","callback_data":"ignore"}]
    ]
    }

    requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={"chat_id":CHAT_ID,"text":message,"reply_markup":keyboard}
    )

    requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
    files={"photo":open(image,"rb")},
    data={"chat_id":CHAT_ID}
    )

def check_telegram():

    global last_update

    url=f"https://api.telegram.org/bot{TOKEN}/getUpdates"

    if last_update:
        url+=f"?offset={last_update}"

    data=requests.get(url).json()

    for r in data["result"]:

        last_update=r["update_id"]+1

        if "callback_query" in r:

            action=r["callback_query"]["data"]

            if action=="repel":

                print("Repeller activated")

                arduino.write(b'R')

            if action=="ignore":

                arduino.write(b'O')

print("System Ready")

while True:

    check_telegram()

    if arduino.in_waiting:

        signal=arduino.readline().decode().strip()

        if signal=="MOVE":

            print("Movement detected")
            print("Camera started")

            start=time.time()

            detect_count=0
            exit_count=0
            alert_sent=False
            repeller_active=False

            while time.time()-start<20:

                ret,frame=cap.read()

                if not ret:
                    continue

                results=model(frame,conf=0.55)

                detected=False

                for r in results:
                    if len(r.boxes)>0:
                        detected=True

                if detected:

                    detect_count+=1
                    exit_count=0

                else:

                    detect_count=0
                    exit_count+=1

                if detect_count>=3:

                    arduino.write(b'A')

                    if not alert_sent:

                        img="rodent.jpg"
                        cv2.imwrite(img,frame)

                        send_alert(img)

                        alert_sent=True

                if exit_count>=5:

                    print("Rodent left engine bay")

                    arduino.write(b'B')
                    arduino.write(b'O')

                    break

                cv2.imshow("Rodent Detection",frame)

                if cv2.waitKey(1)==27:
                    break

            print("Camera stopped")

cap.release()
cv2.destroyAllWindows()