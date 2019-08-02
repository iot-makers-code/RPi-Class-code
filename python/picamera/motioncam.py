from picamera import PiCamera
from time import sleep

cam=PiCamera()
cam.rotation=0
cam.resolution = (1024, 768)

a=raw_input('the start number ?:'); start = int(a)
a=raw_input('the end number ?:'); end = int(a)
try:
   cam.start_preview(alpha=200)
   for i in range(start, end, 1):
      a=raw_input('Press enter to take a photo! ')
      cam.capture('/home/pi/camera/image%03d.png' % i)
      print ('Took #%03d, ' % i), 

except KeyboardInterrupt:
   pass
finally:
   cam.stop_preview()
