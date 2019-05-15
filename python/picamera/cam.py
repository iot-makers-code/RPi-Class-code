from picamera import PiCamera
from time import sleep
cam=PiCamera()
cam.rotation=180
try:
   cam.start_preview()
   sleep(5)
   cam.capture('/home/pi/camera/image.jpg')
   cam.stop_preview()
except KeyboardInterrupt:
   pass
finally:
   cam.stop_preview()
