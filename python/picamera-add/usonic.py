import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG = 13
ECHO = 19
print "Start test distance"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try :
   while True :
      GPIO.output(TRIG, False)
      time.sleep(0.2)

      GPIO.output(TRIG, True)
      time.sleep(0.00001)
      GPIO.output(TRIG, False)

      while GPIO.input(ECHO) == 0 :
         time_start = time.time()

      while GPIO.input(ECHO) == 1 :
         time_end = time.time()

      time_duration = time_end - time_start
      distance = time_duration * 17000
      distance = round(distance, 2)

      print "Distance : ", distance, "cm"
except KeyboardInterrupt:
   pass
finally :
   GPIO.output(TRIG, False)
   GPIO.cleanup()
   
