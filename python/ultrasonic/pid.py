import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

while 1:
    if GPIO.input(18):
        print ("Detected")
    else:
        print ("Not Detected")
    time.sleep(0.5)

GPIO.cleanup()
