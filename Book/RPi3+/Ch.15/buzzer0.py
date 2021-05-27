import RPi.GPIO as GPIO
import time

BUZZ=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZ, GPIO.OUT)

def buzz(pitch, beats):
    period = 1.0 / pitch
    cycles = int(pitch * beats)
    for i in range(cycles):
       GPIO.output(BUZZ, True)
       time.sleep(period/2.0)
       GPIO.output(BUZZ, False)
       time.sleep(period/2.0)

for i in range(1, 300, 10):
    print "Value : ", i
    pitch = 34000 / i
    buzz(pitch, 0.1)

GPIO.cleanup()
