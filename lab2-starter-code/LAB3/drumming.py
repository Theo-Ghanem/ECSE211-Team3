 
from utils.sound import Sound
from time import sleep

def start_drum():
    while True:
        tone1 = Sound(duration=0.1, volume=90, pitch="A3")
        tone1.play()
        sleep(0.15)
