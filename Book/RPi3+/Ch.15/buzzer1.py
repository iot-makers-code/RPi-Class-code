import RPi.GPIO as GPIO
import time

BUZZ=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZ, GPIO.OUT)

def buzz(tones, beats):
    period = 1.0 / tones
    cycles = int(tones * beats)
    for i in range(cycles):
       GPIO.output(BUZZ, True)
       time.sleep(period/2.0)
       GPIO.output(BUZZ, False)
       time.sleep(period/2.0)

tones= [261, 294, 330, 349, 392, 440, 494, 523]
buzz(tones[4], .5)
buzz(tones[4], .5)
buzz(tones[5], .5)
buzz(tones[5], .5)
buzz(tones[4], .5)
buzz(tones[4], .5)
buzz(tones[2], 1)
buzz(tones[4], .5)
buzz(tones[4], .5)
buzz(tones[2], .5)
buzz(tones[2], .5)
buzz(tones[1], 1)

GPIO.cleanup()
