import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
print("Setup LED pins as output")
GPIO.setup(24, GPIO.OUT)
cnt=50
for i in range(0,cnt,1):
   GPIO.output(24, False)
   time.sleep(0.1)
   GPIO.output(24, True)
   time.sleep(0.1)
   print(i)
GPIO.cleanup()
