#!/usr/bin/python
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
StepPins = [17,18,27,23]
print "Setup pins"

for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
StepCount = len(Seq)
StepDir = 1 
WaitTime = 1/float(1000)
StepCounter = 0

while True:
  print StepCounter,
  print Seq[StepCounter]

  for pin in range(0,4):
    xpin=StepPins[pin]
    if Seq[StepCounter][pin]!=0:
      print " Enable GPIO %i" %(xpin)
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)

  StepCounter += StepDir

  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir

  time.sleep(WaitTime)
