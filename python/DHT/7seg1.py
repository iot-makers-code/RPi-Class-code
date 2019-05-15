import RPi.GPIO as GPIO
import smbus
import time

GPIO.setmode(GPIO.BCM)
pins= [12,16,20,18,23,25,24,21]
nums=[[ 1, 1, 1, 1, 1, 1, 0, 0], #0
       [ 0, 1, 1, 0, 0, 0, 0, 0], #1
       [ 1, 1, 0, 1, 1, 0, 1, 0], #2
       [ 1, 1, 1, 1, 0, 0, 1, 0], #3
       [ 0, 1, 1, 0, 0, 1, 1, 0], #4
       [ 1, 0, 1, 1, 0, 1, 1, 0], #5
       [ 1, 0, 1, 1, 1, 1, 1, 0], #6
       [ 1, 1, 1, 0, 0, 0, 0, 0], #7
       [ 1, 1, 1, 1, 1, 1, 1, 0], #8
       [ 1, 1, 1, 1, 0, 1, 1, 0]] #9

for p in pins: 
    GPIO.setup(p, GPIO.OUT);GPIO.output(p, 1)

def digit(n) :
    for i in range(len(pins)):
       GPIO.output(pins[i], nums[n][i]==0)

try:
  while True:
    for i in range(0,10,1): 
      print i
      digit(i)
      time.sleep(.1)
except KeyboardInterrupt:
   pass
finally :
   GPIO.cleanup()
   
