#!/usr/bin/env python3

from utils.brick import Motor
from time import sleep

def dispense_cube(motor_dispenser):

    ##make one revolution of the motor
    motor_dispenser.set_position_relative(180)
    motor_dispenser.set_position_relative(-180)

    while motor_dispenser.is_moving():
                sleep(0.2)
