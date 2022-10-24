#!/usr/bin/env python3

from utils.brick import Motor, TouchSensor, wait_ready_sensors
from time import sleep

motor_left = Motor("A")
# Set target speed first, 360 deg/sec
# Reset power limit to limitless with 0, default values:(power=0, dps=0)
motor_left.set_limits(dps=720)

# set current position to absolute pos 0deg
motor_left.reset_encoder()

async def launch_cube():
    # command to rotate 80deg away from current position
    motor_left.set_limits(dps=0)
    motor_left.set_position_relative(-80)
    while motor_left.is_moving():
        sleep(0.1)
    print("motor_left.set_position_relative(-80)")

    sleep(1)
    # command to rotate 80deg away from current position
    motor_left.set_limits(dps=360)
    motor_left.set_position_relative(80)
    while motor_left.is_moving():
        sleep(0.1)
    print("motor_left.set_position_relative(80)")

    sleep(1)
    motor_left.set_power(0)  # always do 0% to stop motor
    print("motor_left.set_power(0)")
