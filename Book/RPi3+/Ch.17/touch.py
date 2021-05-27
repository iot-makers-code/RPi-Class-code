import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
print("Test touch sensor")
GPIO.setup(12, GPIO.IN)
cnt=500
for i in range(0,cnt,1):
    tch = GPIO.input(12)
    time.sleep(0.1)
    print("Touch :", tch)
GPIO.cleanup()
