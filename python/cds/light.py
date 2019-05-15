import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
print("Test photo reigster")
GPIO.setup(24, GPIO.IN)
cnt=500
for i in range(0,cnt,1):
    inx = GPIO.input(24)
    time.sleep(0.1)
    print "input :", inx
GPIO.cleanup()
