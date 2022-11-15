#!/usr/bin/env python3

from utils.brick import Motor
from time import sleep

def dispense_cube(motor_dispenser):

    motor_start_position = motor_dispenser.get_position()

    ##make one revolution of the motor
    motor_dispenser.set_position(motor_start_position + 180)
    motor_dispenser.set_position_relative(-180)
