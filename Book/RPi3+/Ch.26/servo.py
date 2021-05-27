import RPi.GPIO as GPIO
import time

pin = 18 # PWM pin num 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 2.5
max = 12.5

try:
    while True:
        p.ChangeDutyCycle(cnt)
        print "angle : ",cnt
        cnt = cnt+1 if cnt < max else 2.5
        time.sleep(1)
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()
