import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
print("LED test")
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,False)
time.sleep(1)
cnt=10
for i in range(0,cnt,1):
    GPIO.output(18,False)
    time.sleep(0.1)
    GPIO.output(18,True)
    time.sleep(0.1)
    print("."),
GPIO.cleanup()
