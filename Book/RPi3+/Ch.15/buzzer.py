import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:
   while True:
      text = raw_input("Enter frequency[hz]: ")
      frequency = float(text)
      period = 1.0/frequency
      for i  in range (0,int(3*frequency),1):
         GPIO.output(18, False)
         time.sleep(period/2.0)
         GPIO.output(18, True)
         time.sleep(period/2.0)
finally:
    GPIO.cleanup()
