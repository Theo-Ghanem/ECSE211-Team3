#!/usr/bin/env python3

from utils.brick import Motor
from time import sleep

def dispense_cube(motor_dispenser):

    motor_start_position = -150
    print("start at ", motor_start_position)
    ##make one revolution of the motor
    

    motor_dispenser.set_dps(60)  # speed of motor
    motor_dispenser.set_position(motor_start_position)
    motor_dispenser.set_position(motor_start_position + 180)
    while motor_dispenser.is_moving():
                sleep(0.1)
    print("pushing cube out at ", motor_dispenser.get_position())
    
    sleep(2) 
    
    motor_dispenser.set_position_relative(-180)
    while motor_dispenser.is_moving():
                sleep(0.1)
    print("returning to old position at", motor_dispenser.get_position())
    motor_dispenser.set_dps(0)  # speed of motor
