import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

print("motor test")
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.output(23, False);GPIO.output(24,True)
time.sleep(2)
GPIO.output(23, True);GPIO.output(24,True)
time.sleep(1)
GPIO.output(23, True);GPIO.output(24, False)
time.sleep(2)
GPIO.output(23, False);GPIO.output(24,False)

GPIO.cleanup()
