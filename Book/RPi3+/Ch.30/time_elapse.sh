#!/bin/bash
/usr/bin/python /home/pi/strobe.py &

sleep 10
cd /home/pi/camera
/usr/bin/python -m SimpleHTTPServer 8000 &

cd
sleep 10
/bin/bash /home/pi/fehshow.sh &
