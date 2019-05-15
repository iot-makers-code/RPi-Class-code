
from picamera import PiCamera
from time import sleep
import datetime
cam=PiCamera()
cam.rotation=0
try:
   while True:
      cam.start_preview()
      sleep(5)
      stamp = datetime.datetime.now()
      cam.capture('/home/pi/camera/image%s.jpg' \
           % stamp.strftime('%Y%m%d-%H%M%S') )
      cam.stop_preview()
      sleep(55)
except KeyboardInterrupt:
   pass
finally:
   cam.stop_preview()
