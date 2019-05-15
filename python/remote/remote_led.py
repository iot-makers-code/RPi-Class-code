import RPi.GPIO as GPIO
import time
import sys
import requests
GPIO.setmode(GPIO.BCM)
print("Remote On/Off led:")
GPIO.setup(24,GPIO.IN)
while True:
    time.sleep(0.1)
    inx=GPIO.input(24)
    url="http://192.168.200.17:8000/"+('ON' if inx else 'OFF')
    requests.get(url)
GPIO.cleanup()
print("End of Test")
