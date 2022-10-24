#!/usr/bin/env python3

from utils.brick import Motor, TouchSensor, wait_ready_sensors
from time import sleep


async def launch_cube(motor_left):
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
