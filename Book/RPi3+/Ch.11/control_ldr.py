import RPi.GPIO as GPIO
import time
import sys
import requests
GPIO.setmode(GPIO.BCM)
print("Requset Remote Condition:")
GPIO.setup(18,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
while True:
    time.sleep(1)

    url="http://192.168.200.45:8000/"
    led = requests.get(url).text
    GPIO.output(18, True if led == 'ON' else False)

    url="http://192.168.200.17:8000/"
    led = requests.get(url).text
    GPIO.output(12, True if led == 'ON' else False)

GPIO.cleanup()
print("End of Test")
