#!/usr/bin/env python3
#THIS CODE IS CREATED TO REMIND ME TO TAKE BREAKS FROM PC AND DO EXCERCISES 
#TODO: make amount of intervals changable; create tkinter interface
import time
import sys, os
import subprocess
from tempfile import NamedTemporaryFile
from pydub.utils import get_player_name, make_chunks
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime

current_hour = datetime.now().hour              #\
current_minute = datetime.now().minute          # > Current time
current_time = current_hour*60 + current_minute #/

def _playnn_with_ffplay(seg): #Play sound func
    PLAYER = get_player_name()
    with NamedTemporaryFile("w+b", suffix=".wav") as f:
        seg.export(f.name, "wav")
        subprocess.call([PLAYER, "-nodisp", "-autoexit", "-hide_banner", f.name],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def timer(path,*time_val):
    global stop 
    for val in time_val:
        try:
            countdown(val) #Set time
            while True:
                _playnn_with_ffplay(AudioSegment.from_file( path))
                time.sleep(0.5)
        except KeyboardInterrupt:
            print( "\r  " )#new line
            sys.stdout.write('\033[1A' + "continue or stop: " + '\033[K') # up 1 line and clean 
            dec = input()   
            if dec == "stop":
                stop = 1
            else:
                stop = 0 
                print( '\033[2A'  )# up 2 lines in console

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
        timer("/home/aitehs/Downloads/music/SSBM_Misc_Narrator/Classic and Target Test modes/nr_1p03.dsp.wav", 0,0,1,1)
        if stop:
            break
        timer("/home/aitehs/Downloads/music/SSBM_Misc_Narrator/Narrator (JP)/nr_name10.dsp.wav", 0)
    except KeyboardInterrupt:
        print( "\r  ")
        print('\033[1A' + "Bye bye" + '\033[K')
        break