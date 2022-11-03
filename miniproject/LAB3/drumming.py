 
from utils.sound import Sound
from time import sleep

def start_drum(tone1):
    while True:
        tone1.play()
        sleep(0.2)
