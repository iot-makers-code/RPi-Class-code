import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
print("Setup LED pins as output")
pins = [18,24,21,16]
for p in pins:
    GPIO.setup(p, GPIO.OUT);GPIO.output(p, False)
time.sleep(0.1)

cnt=50
for i in range(0,cnt*len(pins),1):
   remainder = i % len(pins)
   for c in range(0, len(pins), 1):
      GPIO.output(pins[c], remainder == c )
   time.sleep(0.2)
   print((int)(i/len(pins)), remainder)
GPIO.cleanup()
