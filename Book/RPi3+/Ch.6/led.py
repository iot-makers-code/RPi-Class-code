import RPi.GPIO as GPIO
import time
print("Start the LED blinking")
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
cnt=50
for i in range(0,cnt,1):
    GPIO.output(18,False)
    time.sleep(0.1)
    GPIO.output(18,True)
    time.sleep(0.1)
    print("."),
GPIO.cleanup()
