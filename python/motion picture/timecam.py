from picamera import PiCamera
from time import sleep

cam=PiCamera()
cam.rotation=0
cam.resolution = (1024, 768)

try:
   cam.start_preview()
   sleep(3)
   for i in range(0, 480, 1):
      sleep(2)
      print ('#%03d photo taking' % i)
      cam.capture('/home/pi/camera/image%03d.png' % i)
except KeyboardInterrupt:
   pass
finally:
   cam.stop_preview()
