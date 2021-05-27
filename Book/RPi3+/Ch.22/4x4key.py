import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)

MATRIX = [ ["1","2","3","A"],
           ["4","5","6","B"],
           ["7","8","9","C"],
           ["*","0","#","D"] ]

COL = [12,13,11,7]
for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)
ROW = [19,26,16,20]
for i in range (4):
    GPIO.setup(ROW[i], GPIO.IN, \
               pull_up_down = GPIO.PUD_UP)

try:
    while(True):
        for j in range (4):
            GPIO.output(COL[j],0)

            for i in range(4):
                if GPIO.input (ROW[i]) == 0:
                    print "Pressed: ", MATRIX[i][j]
                    time.sleep(0.3)
                    while (GPIO.input(ROW[i]) == 0):
                        pass

            GPIO.output(COL[j],1)
except KeyboardInterrupt:
    GPIO.cleanup()
