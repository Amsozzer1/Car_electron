import socket
import os
import sys  # Ensure this is imported
import picar_4wd as fc
import sys
import tty
import termios
import asyncio
from picamera2 import Picamera2,Preview
import subprocess
import multiprocessing as mp
import time
speed= 50
DIRECTION = "direction is North"
HOST = "192.168.0.191" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)



def getStep(step):
	
	while step == False:
		step = fc.scan_step(2)

	return step
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    try:
		
        while 1:
            client, clientInfo = s.accept()
            
            #client.sendall(("If you want to quit.Please press q").encode())
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                print(data)     
                ANGLE = getSpeed()
                ANGLE_bytes = str(power_val).encode() 
                DATA = data.decode().strip().split(" ")
                if DATA[0] == "stop":
                    fc.stop()
                elif (DATA[0] == "left"):
                    DIRECTION = "direction is East"
                    if(len(DATA)>=2):
                        sp = int(DATA[1])
                        fc.turn_left(sp)
                    else:
                        fc.turn_left(speed)
                elif (DATA[0] == "right"):
                    DIRECTION = "direction is West"
                    if(len(DATA)>=2):
                        sp = int(DATA[1])
                        fc.turn_right(sp)
                    else:
                        fc.turn_right(speed)
                elif (DATA[0] == "Action"):
                    DIRECTION = "direction is Currently stopped due " + DIRECTION.split(" ")[2]
                    if(len(DATA)>=2):
                        sp = int(DATA[1])
                        fc.stop()
                    else:
                        fc.stop()
                elif (DATA[0] == "up"):
                    DIRECTION = "direction is North"
                    if(len(DATA)>=2):
                        sp = int(DATA[1])
                        fc.forward(sp)
                    else:
                        fc.forward(speed)
                elif (DATA[0] == "reverse"):
                    DIRECTION = "direction is South"
                    if(len(DATA)>=2):
                        sp = int(DATA[1])
                        fc.backward(sp)
                    else:
                        fc.backward(speed)
                else:
                    print(sped.speed)
                step = False
                steps = str(getStep(step))
                st = 'SPEED is ' + str(speed) 
                reply = str(speed) +":"+ DIRECTION +":" +steps
                client.sendall(reply.encode())
        
    except Exception as e: 
        print(f"Closing socket because: {e}")
        
        client.close()
        s.close()    

