#!/usr/bin/env python3

import asyncio
from os import kill
from threading import Thread
from multiprocessing import Process

from utils.sound import Sound
from colour_sensing import play_note
from utils.brick import Motor, TouchSensor, EV3ColorSensor, wait_ready_sensors 
from time import sleep
from catapult import *
from drumming import *

motor_left = Motor("A")
# Set target speed first, 360 deg/sec
# Reset power limit to limitless with 0, default values:(power=0, dps=0)
motor_left.set_limits(dps=720)
# set current position to absolute pos 0deg
motor_left.reset_encoder()

ts_colour = TouchSensor(1)
ts_drums = TouchSensor(2)
ts_stop = TouchSensor(3)
drumTone = Sound(duration=0.1, volume=80, pitch="F5")
tone1 = Sound(duration=0.1, volume=100, pitch="C5")
tone2 = Sound(duration=0.1, volume=100, pitch="D5")
tone3 = Sound(duration=0.1, volume=100, pitch="E5")
tone4 = Sound(duration=0.1, volume=100, pitch="G5")

color_sensor = EV3ColorSensor(4)

wait_ready_sensors(True)

async def read_button_colour(touch_sensor, motor_left, color_sensor):
    try:
        running = False
        while True:
            sleep(0.01)
            if touch_sensor.is_pressed() and not running:
                print("Colour button pressed")
                # Read colour, wait till done then launch cube
                play_note(color_sensor, tone1, tone2, tone3, tone4)
                launch_cube(motor_left)
                running = True
            elif not touch_sensor.is_pressed():
                running = False
    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException:
        exit()

async def read_button_drums(touch_sensor):
    try:
        while True:
            sleep(0.01)
            if touch_sensor.is_pressed():
                print("Drum button pressed")
                start_drum(drumTone)

    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException:
        exit()

async def read_button_stop(touch_sensor):
    try:
        while True:
            sleep(0.01)
            if touch_sensor.is_pressed():
                print("Emergency stop button pressed")
                break
    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException:
        exit()



if __name__ == '__main__':
    try:
        print("Starting threads")
        kill_threads = False
        colour_thread = Thread(target=asyncio.run, args=(read_button_colour(ts_colour, motor_left, color_sensor),))
        colour_thread.daemon = True
        drum_thread = Thread(target=asyncio.run, args=(read_button_drums(ts_drums),))
        drum_thread.daemon = True
        stop_thread = Thread(target=asyncio.run, args=(read_button_stop(ts_stop),))
        stop_thread.daemon = True

        colour_thread.start()
        drum_thread.start()
        stop_thread.start()

        stop_thread.join()

        exit()
    except BaseException:
        exit()




