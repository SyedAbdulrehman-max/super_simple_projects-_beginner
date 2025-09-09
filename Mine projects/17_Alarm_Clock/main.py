from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

user = int(input("Enter a number:>"))

def alarm(seconds):
    time_laps = 0

    print(CLEAR)
    while time_laps < seconds :
        time.sleep(1)
        time_laps+=1

        time_left = seconds - time_laps
        min_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{min_left:02d}:{seconds_left:02d}")
    playsound('sound.mp3')

alarm(user)