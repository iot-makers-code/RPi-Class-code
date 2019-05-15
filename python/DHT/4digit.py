import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pins=[12,20,25,23,18,16,21,24]
coms=[ 26,19,13,6]
for p in pins: GPIO.setup(p, GPIO.OUT);GPIO.output(p, 1)
for c in coms: GPIO.setup(c, GPIO.OUT);GPIO.output(c, 0)

while True:
   for c in coms:
     print c,
     for s in coms: GPIO.output(s, s==c)

     for p in pins: 
        print p
        GPIO.output(p, 0)
        time.sleep(.1)
        GPIO.output(p, 1)
        time.sleep(.1)
