from BaseHTTPServer \
import BaseHTTPRequestHandler,HTTPServer
from gpiozero import PWMOutputDevice
import time

pin1 = 23
pin2 = 24
pin3 = 17
pin4 = 27

forwardRight=PWMOutputDevice(pin1,True,0,1000)
reverseRight=PWMOutputDevice(pin2,True,0,1000)
forwardLeft=PWMOutputDevice(pin3,True,0,1000)
reverseLeft=PWMOutputDevice(pin4,True,0,1000)

state=0
num = 0

def Forward():
    global state,num
    x=0.5
    y=0.5
	
    if state==1:
        if num <2:
            num+=1
    	print('Forward')
	print('state=1')
	forwardRight.value=x+(0.25*num)
	reverseRight.value=0
	forwardLeft.value=y+(0.25*num)
	reverseLeft.value=0
	time.sleep(1)
	
	forwardRight.value=0
	reverseRight.value=0
	forwardLeft.value=0
	reverseLeft.value=0

    else:
        state=1
        num=0
        print('Forward')
        print('state=1')
	forwardRight.value=x
	reverseRight.value=0
	forwardLeft.value=y
	reverseLeft.value=0
	time.sleep(1)

	forwardRight.value=0
	reverseRight.value=0
	forwardLeft.value=0
	reverseLeft.value=0
  
def Backward():
    global state, num
    x=0.5
    y=0.5
    
    if state==2:
        if num<2:
            num+=1
        state=2
    	print('Backward')
	print('state=2')
	forwardRight.value=0
	reverseRight.value=x+(0.25*num)
	forwardLeft.value=0
	reverseLeft.value=y+(0.25*num)
	time.sleep(1)

	forwardRight.value=0
	reverseRight.value=0
	forwardLeft.value=0
	reverseLeft.value=0
  
  
      else:
        state=2
        num=0
        print('Backward')
        print('state=2')
	forwardRight.value=0
	reverseRight.value=x
	forwardLeft.value=0
	reverseLeft.value=y
	time.sleep(1)

	forwardRight.value=0
	reverseRight.value=0
	forwardLeft.value=0
	reverseLeft.value=0

def RightTurn():
        global state
	state=3
    	print('RightTurn')
	print('state=3')
	forwardRight.value=0
	reverseRight.value=0
	forwardLeft.value=0.6
	reverseLeft.value=0
	time.sleep(1)
	
	forwardRight.value=0
	reverseRight.value=0
	forwardLeft.value=0
	reverseLeft.value=0

def LeftTurn():
        global state
	state=4
    	print('LeftTurn')
	print('state=4')
	forwardRight.value=0.6
	reverseRight.value=0
	forwardLeft.value=0
	reverseLeft.value=0
	time.sleep(1)
	
	forwardRight.value=0
	reverseRight.value=0
	forwardLeft.value=0
	reverseLeft.value=0

def STOP():
	state=0
    	print('STOP')
	print('state=0')
	forwardRight.value=0
	reverseRight.value=0
	forwardLeft.value=0
	reverseLeft.value=0
  
class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
            if self.path =='/favicon.ico': return
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            led=True if self.path=='/ON' else False
            
            message= '<a href=/FW>Forward</a><br>'\
                     '<a href=/BW>Backward</a><br>'\
                     '<a href=/LT>LeftTurn</a><br>'\
                     '<a href=/RT>RightTurn</a><br>'\
                     '<a href=/ST>STOP</a>'
            self.wfile.write(bytes(message))
            print(self.path)
            if self.path=='/FW':
                Forward()
            elif self.path=='/BW':
                Backward()
            elif self.path=='/LT':
                LeftTurn()
            elif self.path=='/RT':
                RightTurn()
            elif self.path=='/ST':
                STOP()
            return

def run():
	server_addr=('0.0.0.0', 8000)
	httpd=HTTPServer(server_addr, MyHandler)
	print('starting web server...')
	httpd.serve_forever()
	
run()
