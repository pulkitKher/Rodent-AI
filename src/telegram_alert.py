import requests

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_alert():
    message = "Mouse Detected Inside Car!"
    url = f"/sendMessage"
    data = {"chat_id": CHAT_ID,"text":message}
    requests.post(url,data=data)