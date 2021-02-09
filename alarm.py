from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime
import time
current_hour = datetime.now().hour
current_minute = datetime.now().minute
current_time = current_hour*60 + current_minute

acc_morn_hr, acc_morn_min = "8", "30"
acc_night_hr, acc_night_min = "23", "30"
start_time = int(acc_morn_hr)*60 + int(acc_morn_min)
end_time = int(acc_night_hr)*60 + int(acc_night_min)

while True:
    if start_time <= current_time and end_time >= current_time:
        try:
            time.sleep(30*60)
            play(AudioSegment.from_file( "/home/aitehs/Downloads/Gerudo Valley - The Legend of Zelda Ocarina Of Time.mp3"))
        except KeyboardInterrupt:
            des = input( "\n continue or stop:")
            if des == "stop":
                break
            else:
                pass
            try:
                time.sleep(10*60)
                play(AudioSegment.from_file( "/home/aitehs/Downloads/Fire Emblem Shadow Dragon OST - 28 - Come, Join Us.mp3"))
            except KeyboardInterrupt:
                des = input("\n continue or stop:")
                if des == "stop":
                    break
                else:
                    continue
