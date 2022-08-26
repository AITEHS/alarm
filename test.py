import itertools

save_timer = 0


class Interval:
    sound_choice = input("Do you want to use default sound?(Y/N)")
    if sound_choice == "Y" or sound_choice == "y":
            sound_path = r"./default_sound/basic.mp3"
    else:
        sound_path = input("Input path to the played sound:")
    while True:

        length_choice = input("Input length of timer.(In minutes)")
        try: 
            int(length_choice)
            break
        except:
            continue
    alarm_text = input("Input desired alarm text:")

class Timer:
    interval_count = 0
    while True:
        interval_count +=1
        if save_timer == 0:
            Interval()
            next_action = input("Save as it is or add another time interval to the loop?(S/A)")
            save_timer = 1 if next_action == "S" or next_action == "s" else 0
        else: 
            break

