import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
print("Test relay to light on ")
GPIO.setup(23, GPIO.OUT)
GPIO.output(23,False)
try :
    while True:
        GPIO.output(23,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(23,GPIO.LOW)
        time.sleep(1)
finally :
    GPIO.cleanup()
