import RPi.GPIO as GPIO
import time

IRED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(IRED, GPIO.IN)

def MOTION(ired):
      print "Motion Detected!"

print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)

try:
     GPIO.add_event_detect(IRED, \
             GPIO.RISING, callback=MOTION)
     while 1:
          time.sleep(100)
except KeyboardInterrupt:
      print "Quit"
      GPIO.cleanup()
