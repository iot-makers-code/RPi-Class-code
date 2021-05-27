import RPi.GPIO as GPIO
import time
import sys

print ("SOS signal start")
GPIO.setmode(GPIO.BCM)
ok=[ 3,-1,3,-1,3,-3,3,-1,1,-1,3,-7 ]
sos=[ 1,-1,1,-1,1,-3,3,-1,3,-1,3,-3,1,-1,1,-1,1,-7 ]
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)
time.sleep(1)

for i in range(0,5,1):
   for signal in sos:
      print signal,
      delay=0
      if signal < 0:
         delay=signal * -1
         GPIO.output(18, False)
      else:
         delay=signal
         GPIO.output(18, True)
      time.sleep(delay * 0.1)
   print  ("....", i )

GPIO.cleanup()
sys.exit(0)
