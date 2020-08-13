import serial
import json

#replace the string inside brackets with actual COM serial port on windows (use MODE command)
# on mac/linux, to get the serial ports use this command ls /dev/tty.usb*
s = serial.Serial('/dev/tty.usbmodem14101')

while True:
    data = json.loads(s.readline())
    proximity = data["detail"]["proximity"]
    print(proximity)
