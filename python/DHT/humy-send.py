#!/usr/bin/python
import Adafruit_DHT
import time
import requests

sensor = Adafruit_DHT.DHT11
pin = 4

while True :
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print "Temp={0:0.1f}*C Humidity={1:0.1f}%"\
                  .format(temperature, humidity)
        temp = str(int(temperature))
        hum = str(int(humidity))
        url='http://192.168.200.107:8000/?temp='\
             +temp+'&hum='+hum
        requests.get(url)
    else:
        print "Failed to get reading."
    time.sleep(3)
