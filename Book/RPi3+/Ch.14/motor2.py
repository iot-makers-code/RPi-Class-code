import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

print (" motor test")
def run(t, r):
    print ("run ", t, " power ", r, "%")
    totime = 0
    i=0.03
    while totime < t :
        GPIO.output(25, True)
        time.sleep(i*r/100)
        GPIO.output(25, False)
        time.sleep(i*(100-r)/100)
        totime += I

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.output(23, False);GPIO.output(24, True)
run(3, 10)
run(3, 50)
run(3, 100)
GPIO.cleanup()
