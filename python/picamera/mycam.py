from picamera import PiCamera
from time import sleep
import datetime
cam=PiCamera()
cam.rotation=0

try:
   i = 0
   while True:
      cam.start_preview()
      sleep(5)
      cam.capture('/home/pi/camera/image%04d.png' % i)
      cam.stop_preview()
      sleep(55)
      i += 1
except KeyboardInterrupt:
   pass
finally:
   cam.stop_preview()
