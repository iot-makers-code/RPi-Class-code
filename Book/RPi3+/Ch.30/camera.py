from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.rotation=180
try:
   camera.start_preview()
   sleep(10)
   camera.capture('/home/pi/camera/image.jpg')
   camera.stop_preview()
except KeyboardInterrupt:
   pass
finally:
   camera.stop_preview()
