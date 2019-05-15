import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pins=[12,20,25,23,18,16,21,24]
coms=[ 26,19,13,6]
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

for p in pins: GPIO.setup(p, GPIO.OUT);GPIO.output(p, 1)
for c in coms: GPIO.setup(c, GPIO.OUT);GPIO.output(c, 0)

def digit(n) :
    for i in range(len(pins)):
       GPIO.output(pins[i], nums[n][i]==0)

def number(n) :
    for com in coms:
       if n < 1: break
       r = n % 10
       n = n / 10
       GPIO.output(com, 1)
       digit(r)
       time.sleep(.001)	
       GPIO.output(com, 0)

try:
  while True:
    for i in range(0,10000,1): 
      print i
      number(i)

except KeyboardInterrupt:
   pass
finally :
   GPIO.cleanup()
   
