#!/usr/bin/env python3

from utils.brick import Motor, TouchSensor, wait_ready_sensors
from utils.sound import Sound
from time import sleep

def start_drum(touch_sensor):
    # command to rotate 80deg away from current position
    while True:
        tone1 = Sound(duration=1.0, volume=80, pitch="A3")
        tone1.play()
        
