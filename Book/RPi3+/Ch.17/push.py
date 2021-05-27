import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
print("Test pullup/pulldown switch")
GPIO.setup(17, GPIO.IN)
GPIO.setup(05, GPIO.IN)
cnt=500
for i in range(0,cnt,1):
    up = GPIO.input(17)
    dw = GPIO.input(05)
    time.sleep(0.1)
    print("UP(%d) DOWN(%d)") %(up, dw)
GPIO.cleanup()
