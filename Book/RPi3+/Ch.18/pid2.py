import RPi.GPIO as GPIO
import time

IRED = 18
LED  = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(IRED, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def MOTION(ired):
      print "Motion Detected!"
      GPIO.output(LED, True)

print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)

try:
     GPIO.add_event_detect(IRED, \
             GPIO.RISING, callback=MOTION)
     while 1:
          time.sleep(100)
          GPIO.output(LED, False)
except KeyboardInterrupt:
      print "Quit"
      GPIO.cleanup()
