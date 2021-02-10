from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime
import time
import sys
current_hour = datetime.now().hour
current_minute = datetime.now().minute
current_time = current_hour*60 + current_minute

acc_morn_hr, acc_morn_min = "8", "30"
acc_night_hr, acc_night_min = "23", "30"
start_time = int(acc_morn_hr)*60 + int(acc_morn_min)
end_time = int(acc_night_hr)*60 + int(acc_night_min)

def countdown(interval):    
            for i in range(interval-1,-1,-1):
                for j in range(59,-1,-1):
                    sys.stdout.write(f'\rDuration: {i} Minutes {j} Seconds to go')
                    time.sleep(1)
                    sys.stdout.flush() 

while True:
    if start_time <= current_time and end_time >= current_time:
        try:
            countdown(30)       
            while True:
                play(AudioSegment.from_file("/home/aitehs/Downloads/SSBM_Misc_Narrator/Classic and Target Test modes/nr_1p03.dsp.wav"))
                time.sleep(0.5)
        except KeyboardInterrupt:
            des = input( "\n continue or stop:")
            if des == "stop":
                break
            else:
                pass
            try:
                countdown(10)
                
                while True:
                    play(AudioSegment.from_file( "/home/aitehs/Downloads/SSBM_Misc_Narrator/Narrator (JP)/nr_name10.dsp.wav"))
                    time.sleep(0.5)
                
            except KeyboardInterrupt:
                des = input("\n continue or stop:")
                if des == "stop":
                    break
                else:
                    continue
    else:
        continue
