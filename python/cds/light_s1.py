import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
print("Test photo register")
GPIO.setup(24,GPIO.IN)
cnt=60*50
for i in range(0,cnt,1):
    time.sleep(0.01)
    inx = GPIO.input(24)
    sys.stdout.write('#' if inx else '_')
    if i%60 == 59 : sys.stdout.write("\n")
    sys.stdout.flush()
print("")
GPIO.cleanup()
