#!/usr/bin/env python3

from threading import Thread

from utils.sound import Sound
from colour_sensing import read_colour
from utils.brick import Motor, TouchSensor, wait_ready_sensors
from time import sleep
from catapult import *

motor_left = Motor("A")
# Set target speed first, 360 deg/sec
# Reset power limit to limitless with 0, default values:(power=0, dps=0)
motor_left.set_limits(dps=720)

# set current position to absolute pos 0deg
motor_left.reset_encoder()

ts_colour = TouchSensor(1)
ts_drums = TouchSensor(2)
ts_stop = TouchSensor(3)

wait_ready_sensors(True)

async def read_button_colour(touch_sensor):
    try:
        running = False
        while True:
            sleep(0.01)
            if touch_sensor.is_pressed() and not running:
                # Read colour, wait till done then launch cube
                await read_colour()
                #launch_cube()
                running = True
            elif not touch_sensor.is_pressed():
                running = False
    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException:
        exit()

async def read_button_drums(touch_sensor):
    try:
        running = False
        while True:
            sleep(0.01)
            if touch_sensor.is_pressed() and not running:
                tone1 = Sound(duration=1.0, volume=80, pitch="A3")
                tone1.play()
                tone1.wait_done()
                running = True
            elif not touch_sensor.is_pressed():
                running = False
    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException:
        exit()

async def read_button_stop(touch_sensor):
    try:
        running = False
        while True:
            sleep(0.01)
            if touch_sensor.is_pressed():
                exit()
    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException:
        exit()


if __name__ == '__main__':
    print("Starting threads")
    colour_thread = Thread(target=read_button_colour(ts_colour))
    drum_thread = Thread(target=read_button_drums(ts_drums))
    stop_thread = Thread(target=read_button_stop(ts_stop))

    colour_thread.start()
    drum_thread.start()
    stop_thread.start()

    colour_thread.join()
    drum_thread.join()
    stop_thread.join()




