import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
pin=24
GPIO.setup(pin, GPIO.IN)

try:
    while True:
        time.sleep(0.1)
        i = GPIO.input(pin)
        sys.stdout.write("_" if i else "#")
        sys.stdout.flush()

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
