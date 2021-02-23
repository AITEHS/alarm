#THIS CODE IS CREATED TO REMIND ME TO TAKE BREAKS FROM PC AND DO EXCERCISES 
import time
import sys
import subprocess
from tempfile import NamedTemporaryFile
from pydub.utils import get_player_name, make_chunks
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime

current_hour = datetime.now().hour
current_minute = datetime.now().minute
current_time = current_hour*60 + current_minute

acc_morn_hr, acc_morn_min = "8", "30"
acc_night_hr, acc_night_min = "23", "30"
start_time = int(acc_morn_hr)*60 + int(acc_morn_min)
end_time = int(acc_night_hr)*60 + int(acc_night_min)

def _playnn_with_ffplay(seg):
    PLAYER = get_player_name()
    with NamedTemporaryFile("w+b", suffix=".wav") as f:
        seg.export(f.name, "wav")
        subprocess.call([PLAYER, "-nodisp", "-autoexit", "-hide_banner", f.name],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def playnn(audio_segment):
    _playnn_with_ffplay(audio_segment)

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

while True:
    try:
        if start_time <= current_time and end_time >= current_time:
            try:
                countdown(30)       
                while True:
                    playnn(AudioSegment.from_file("/home/aitehs/Downloads/SSBM_Misc_Narrator/Classic and Target Test modes/nr_1p03.dsp.wav"))
                    time.sleep(0.5)
                
            except KeyboardInterrupt:
                print( "\r  ")
                des = input('\033[1A' + "continue or stop:" + '\033[K')      
                sys.stdout.write("\033[F")
                if des == "stop":
                    break
                else:
                    pass
                try:
                    countdown(10)
                    while True:
                        playnn(AudioSegment.from_file( "/home/aitehs/Downloads/SSBM_Misc_Narrator/Narrator (JP)/nr_name10.dsp.wav"))
                        time.sleep(0.5)
            
                except KeyboardInterrupt:
                    print( "\r  ")
                    des = input('\033[1A' + "continue or stop:" + '\033[K')        
                    sys.stdout.write("\033[F")
                
                    if des == "stop":
                        break
                    else:
                        print( '\033[1A')
                        continue
        else:
            continue
    except KeyboardInterrupt:
        print( "\r  ")
        print('\033[1A' + "Bye bye" + '\033[K')
        
        break