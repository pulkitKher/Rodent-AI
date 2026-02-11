import serial

esp = serial.Serial("COM3",115200)

def send_signal(value):
    if value == 1:
        esp.write(b'1')
    else:
        esp.write(b'0')
        