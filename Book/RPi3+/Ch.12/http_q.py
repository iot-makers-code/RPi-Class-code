import RPi.GPIO as GPIO
import time

pin=24
GPIO.setmode(GPIO.BCM)
try:
    while True:
        dark = 0

        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(pin, GPIO.IN)
        while (GPIO.input(pin) == GPIO.LOW):
            dark += 1
        print ("Light : %d" % dark)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
