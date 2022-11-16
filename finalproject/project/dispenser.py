#!/usr/bin/env python3

from utils.brick import Motor
from time import sleep

def dispense_cube(motor_dispensor):

    ##make one revolution of the motor
    motor_dispensor.set_position_relative(360)
