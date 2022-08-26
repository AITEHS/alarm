#!/usr/bin/env python
#THIS CODE IS CREATED TO REMIND ME TO TAKE BREAKS FROM PC AND DO EXCERCISES 
#TODO: make amount of intervals changable; create tkinter interface
import time
import sys, os
import subprocess
from tempfile import NamedTemporaryFile
from playsound import playsound
from datetime import datetime

clear = lambda: os.system('cls')


current_hour = datetime.now().hour              #\
current_minute = datetime.now().minute          # > Current time
current_time = current_hour*60 + current_minute #/


def timer(path,*time_val):
    global stop 
    for val in time_val:
        try:
            countdown(val) #Set time
            while True:
                playsound(path)
                time.sleep(0.5)
        except KeyboardInterrupt:
            clear()
            sys.stdout.write("continue or stop: ") # up 1 line and clean 
            dec = input()   
            if dec == "stop":
                stop = 1
                
            else:
                stop = 0 
                clear()
def countdown(interval):    
    for i in range(interval-1,-1,-1):
        for j in range(59,-1,-1):
            if i >= 10 and j >= 10:
                sys.stdout.write(f'\rDuration: {i} Minutes {j} Seconds to go')
                time.sleep(1)
                sys.stdout.flush() 
            elif i < 10 and j >= 10:
                sys.stdout.write(f'\rDuration: {"0" + str(i)} Minutes {j} Seconds to go')
                time.sleep(1)
                sys.stdout.flush() 
            elif i >= 10 and j < 10:
                sys.stdout.write(f'\rDuration: {i} Minutes {"0" + str(j)} Seconds to go')
                time.sleep(1)
                sys.stdout.flush() 
            elif i < 10 and j < 10:
                sys.stdout.write(f'\rDuration: {"0" + str(i)} Minutes {"0" + str(j)} Seconds to go')
                time.sleep(1)
                sys.stdout.flush() 

while True: #Timer
    try:  
        timer("./WD/W6.wav", 30)
        if stop:
            break
        timer("./WD/D4.wav", 10)
        if stop:
            break
    except KeyboardInterrupt or EOFError:
        
        print( "Bye bye" )
        break