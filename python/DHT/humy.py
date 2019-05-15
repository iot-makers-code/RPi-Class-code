import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 16

while True :
    humidity,temperature=Adafruit_DHT.read_retry(sensor, in)
    if humidity is not None and temperature is not None:
        print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'\
                  .format(temperature, humidity)
    else:
        print "Failed to get reading."
    time.sleep(3)
    
