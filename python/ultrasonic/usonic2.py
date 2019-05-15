import RPi.GPIO as GPIO
import time

from picamera import PiCamera
import datetime
cam=PiCamera()
cam.rotation=0

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

      if distance <= 100 :
         cam.start_preview()
         time.sleep(5)
         stamp = datetime.datetime.now()
         cam.capture('/home/pi/camera/image%s.jpg' \
              % stamp.strftime('%Y%m%d-%H%M%S') )
         cam.stop_preview()
         time.sleep(5)

except KeyboardInterrupt:
   pass
finally :
   GPIO.output(TRIG, False)
   GPIO.cleanup()
   cam.stop_preview()
