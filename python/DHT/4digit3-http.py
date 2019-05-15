from BaseHTTPServer \
    import BaseHTTPRequestHandler,HTTPServer
import RPi.GPIO as GPIO
import time
import threading
import Queue
import re

GPIO.setmode(GPIO.BCM)
pins=[12,20,25,23,18,16,21,24]
coms=[ 26,19,13,6]
#coms=[ 13,6,19,26]
nums=[[ 1, 1, 1, 1, 1, 1, 0, 0], #0
      [ 0, 1, 1, 0, 0, 0, 0, 0], #1
      [ 1, 1, 0, 1, 1, 0, 1, 0], #2
      [ 1, 1, 1, 1, 0, 0, 1, 0], #3
      [ 0, 1, 1, 0, 0, 1, 1, 0], #4
      [ 1, 0, 1, 1, 0, 1, 1, 0], #5
      [ 1, 0, 1, 1, 1, 1, 1, 0], #6
      [ 1, 1, 1, 0, 0, 0, 0, 0], #7
      [ 1, 1, 1, 1, 1, 1, 1, 0], #8
      [ 1, 1, 1, 1, 0, 1, 1, 0]] #9
que = Queue.Queue()
for p in pins: GPIO.setup(p, GPIO.OUT);GPIO.output(p, 1)
for c in coms: GPIO.setup(c, GPIO.OUT);GPIO.output(c, 0)
que.put(8888)

def display():
    display=0
    while True:
        if que.empty()==False : 
           display = que.get()

        n = display
        for com in coms:
           r = n % 10
           GPIO.output(com, 1)
           digit(r)
           time.sleep(.001)    
           GPIO.output(com, 0)
           n /= 10
           if n==0: break;

def digit(d) :
        for i in range(len(pins)):
           GPIO.output(pins[i], nums[d][i]==0)

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/favicon.ico" : return
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        m = re.search(r'.*?temp=(.*)&hum=(.*)', \
             self.path, re.M|re.I)
        temperature = int(float(m.group(1)))*100
        humidity    = int(float(m.group(2)))
        value       = temperature + humidity
        que.put(value)
        message = 'temperature='+m.group(1)+\
            ',humidity='+m.group(2)
        self.wfile.write(bytes(message))
        return

def run():
    try:
        thread_dis = threading.Thread(target=display)
        thread_dis.start()
        server_addr = ('0.0.0.0', 8000)
        httpd = HTTPServer(server_addr, MyHandler)
        print('starting web server...')
        httpd.serve_forever()
    except KeyboardInterrupt:
       pass
    finally:
       GPIO.cleanup()
run()
