#!/usr/bin/env python3

from utils.brick import Motor
from time import sleep
# from dispenser import (dispense_cube)
# FOR TESTING
# motor_row = Motor("A")  # remove this after
# motor_column = Motor("B")  # remove this after
# grid = [
#     [1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1]
# ]

# constants for row distance:
# row_distance = [74, 66, 58, 50, 42]
# column_distance = [130, 110, 90, 80, 60]  # probably will be different than row
# row_distance = [120, 105, 85, 70, 54]
row_distance = [140, 120, 105, 80, 65]
column_distance = [100, 80, 60, 40, 20]  # probably will be different than row


def push_row(motor_row, motor_column, motor_dispenser, grid, iteration, verbose):

    motor_row.set_limits(dps=80)  # speed limit of motor

    # make sure the motor is in correct position at start!
    motor_start_position = motor_row.get_position()
    counter = 0
    at_least_one_cube = False
    for i in grid[iteration]:
        if i == 1:
            at_least_one_cube = True
            dispense_cube(motor_dispenser)

            if verbose:
                print("Waiting for cube to dispense")  
            sleep(2.5)

            if verbose:
                print("Cube " + str(counter+1) + " is loaded")
            distance = row_distance[counter]

            # make extender extend
            motor_row.set_position(motor_start_position - distance)
            while motor_row.is_moving():
                sleep(0.1)
            if verbose:
                print("Extender extend's to row " + str(abs(counter-5)))

            sleep(2)  # wait before retracting

            # make extender retract
            motor_row.set_position(motor_start_position)
            while motor_row.is_moving():
                sleep(0.1)
            if verbose:
                print("Extender retract's from row " + str(abs(counter-5)))

            sleep(5)  # wait 5 seconds for cube to load in

        counter += 1
    if (at_least_one_cube):  # If there is no cube then no need to push the column
        push_column(motor_column, 0, True)
    else:
        if verbose:
            print("Skipping column " + str(abs(iteration-5)) +
                  " because no cubes to push\n")


def push_column(motor_column, iteration, verbose):
    
    motor_column.set_limits(dps=80)  # speed of motor

    # make sure the motor is in correct position at start!
    motor_start_position = motor_column.get_position()

    distance = column_distance[iteration]

    # make extender extend
    motor_column.set_position(motor_start_position + distance)
    while motor_column.is_moving():
        sleep(0.1)
    if verbose:
        print("Wall extend's to column " + str(abs(iteration-5)))

    sleep(2)  # wait before retracting

    # make extender retract
    motor_column.set_position(motor_start_position)
    while motor_column.is_moving():
        sleep(0.1)
    if verbose:
        print("Wall retract's from column " + str(abs(iteration-5)))

    if verbose:
        print("Waiting for next row to be done\n")
    sleep(3)  # wait 3 seconds then exit


def dispense_cube(motor_dispenser):
    motor_dispenser.set_dps(70)  # speed of motor
    motor_dispenser.set_position_relative(200)
    
    sleep(2) 
    print("pushing cube out at ", motor_dispenser.get_position())
    
    motor_dispenser.set_position(0)

    sleep(2)
    print("returning to old position at", motor_dispenser.get_position())
    motor_dispenser.set_dps(0)  # speed of motor
