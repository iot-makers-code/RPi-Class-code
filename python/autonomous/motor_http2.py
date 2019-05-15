from BaseHTTPServer \
	import BaseHTTPRequestHandler,HTTPServer
from gpiozero import PWMOutputDevice
import time

pin1 = 23
pin2 = 24

pin3 = 17
pin4 = 27

forwardRight=PWMOutputDevice(pin1, True, 0, 1000)
reverseRight=PWMOutputDevice(pin2, True, 0, 1000)

forwardLeft=PWMOutputDevice(pin3, True, 0, 1000)
reverseLeft=PWMOutputDevice(pin4, True, 0, 1000)

state=0
num = 0

state_dict={"Forward":[0.6, 0.6, 0.0, 0.0, 1.0, 0.0],
            "Backward":[0.0, 0.0, 0.6, 0.6, 0.0, 1.0],
            "RightTurn":[0.0, 0.6, 0.0, 0.0, 0.0 , 0.0],
            "LeftTurn":[0.6, 0.0, 0.0, 0.0, 0.0, 0.0],
            "Stop":[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            }

def Move(status):
    global num,state_dict
    fr,fl,rer,rel,Fo,Bw = state_dict[status]
    print(status)
    forwardRight.value=fr+(Fo*0.2*num)
    reverseRight.value=rer+(Bw*0.2*num)
    forwardLeft.value=fl+(Fo*0.2*num)
    reverseLeft.value=rel+(Bw*0.2*num)
    time.sleep(1)

def State_Change(stat):
    global state,num
    if state == stat and num < 2:
        num+=1
    elif state != stat:
        num=0
        state=stat
    
class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
            if self.path =='favicon.ico': return
            self.send_response(200)
            self.send_header('Content-type','texthtml')
            self.end_headers()
            
            message= '<a href=/FW>Forward</a><br>'\
                     '<a href=/BW>Backward</a><br>'\
                     '<a href=/LT>LeftTurn</a><br>'\
                     '<a href=/RT>RightTurn</a><br>'\
                     '<a href=/ST>STOP</a>' \
                     
            self.wfile.write(bytes(message))
            print(self.path)
            if self.path=='/FW':
                State_Change(1)
                Move("Forward")
                Move("Stop")
            elif self.path=='/BW':
                State_Change(2)
                Move("Backward")
                Move("Stop")
            elif self.path=='/LT':
                State_Change(3)
                Move("LeftTurn")
                Move("Stop")
            elif self.path=='/RT':
                State_Change(4)
                Move("RightTurn")
                Move("Stop")
            elif self.path=='/ST':
                State_Change(0)
                Move("Stop")
            
            return
def run():
	server_addr=('0.0.0.0', 8000)
	httpd=HTTPServer(server_addr, MyHandler)
	print('starting web server...')
	httpd.serve_forever()
	
run()
