import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
print("Start three LEDs blinking")
pins = [18,24,21]
for p in pins:
    GPIO.setup(p, GPIO.OUT)

cnt=50
for i in range(0,cnt*len(pins),1):
   for c in range(0, len(pins), 1):
      if (i % len(pins)) == c :
         GPIO.output(pins[c], True )
      else:
         GPIO.output(pins[c], False )
   time.sleep(0.2)
   print((int)(i/len(pins)), (i % len(pins)))
GPIO.cleanup()
