from turtle import *
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
print("Show sensor digital data")
GPIO.setup(24, GPIO.IN)

colors=['white', 'red', 'green', 'yellow']
pre=0; page=0; x=0
while x<1200:
    if x % 150 == 0:
        page = 0 if page else 1
        clearscreen();bgcolor('black');
        pencolor('white');speed(0)
        up();rt(-90);fd(90);
        rt(-90);fd(150);rt(180);down()

    inx = GPIO.input(24)
    pencolor(colors[page*2+inx])
    if inx == pre : fd(10)
    if pre == 0 and inx == 1 : 
        rt(-90);fd(10);rt(90);fd(10)
    if pre == 1 and inx == 0 : 
        rt(90);fd(10);rt(-90);fd(10)
    pre = inx

    if x % 30 == 29:
        up(); rt(90);fd(30);
        rt(90);fd(30*10);rt(180); down();

    time.sleep(0.01)
    x=x+1

exitonclick()
GPIO.cleanup()
