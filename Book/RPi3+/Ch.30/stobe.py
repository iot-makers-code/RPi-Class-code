from picamera import PiCamera
from time import sleep
import datetime

camera=PiCamera()
camera.rotation=0
try:
   while True:
      camera.start_preview()
      sleep(5)
      stamp = datetime.datetime.now()
      camera.capture('/home/pi/camera/image%s.jpg' \
           % stamp.strftime('%Y%m%d-%H%M%S') )
      camera.stop_preview()
      sleep(5)
except KeyboardInterrupt:
   pass
finally:
   camera.stop_preview()
