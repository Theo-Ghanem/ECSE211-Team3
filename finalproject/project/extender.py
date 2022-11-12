#!/usr/bin/env python3

from utils.brick import Motor, TouchSensor, wait_ready_sensors
from time import sleep

# motor_row = Motor("A")  # remove this after
# motor_column = Motor("B")  # remove this after

# constants for row distance:
row_distance = [140, 110, 90, 80, 60]
column_distance = [140, 110, 90, 80, 60]  # probably will be different than row

# grid = [
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1]
# ]


def pushRow(motor_row, motor_column, grid, iteration, verbose):

    motor_row.set_limits(dps=80)  # speed of motor
    # make sure the motor is in correct position at start!
    motorStartPosition = motor_row.get_position()
    print("do you get here")
    counter = 0
    # atLeast1Cube = False
    for i in grid[iteration]:
        if i == 1:
            print("1")
            atLeast1Cube = True
            if (verbose):
                print("Cube " + str(counter+1) + " is loaded")
            distance = row_distance[counter]
            print(1)
            # make extender extend
            motor_row.set_position(motorStartPosition + distance)
            while motor_row.is_moving():
                sleep(0.1)
                print("2")
            if (verbose):
                print("Extender extend's to row " + str(abs(counter-5)))

            sleep(2)  # wait before retracting

            # make extender retract
            motor_row.set_position(motorStartPosition)
            while motor_row.is_moving():
                sleep(0.1)
            if (verbose):
                print("Extender retract's from row " + str(abs(counter-5)))

            sleep(5)  # wait 5 seconds for cube to load in

        counter += 1
    # if (atLeast1Cube):  # If there is no cube then no need to push the column
    print("what about here")
    pushColumn(motor_column, iteration, verbose)


def pushColumn(motor_column, iteration, verbose):
    if (verbose):
        print("Pushing wall to column " + str(abs(iteration-5)))
    motor_column.set_limits(dps=80)  # speed of motor
    # make sure the motor is in correct position at start!
    motorStartPosition = motor_column.get_position()

    distance = column_distance[iteration]

    # make extender extend
    motor_column.set_position(motorStartPosition + distance)
    while motor_column.is_moving():
        sleep(0.1)
    if (verbose):
        print("wall extend's to column " + str(abs(iteration-5)))

    sleep(2)  # wait before retracting

    # make extender retract
    motor_column.set_position(motorStartPosition)
    while motor_column.is_moving():
        sleep(0.1)
    if (verbose):
        print("wall retract's from column " + str(abs(iteration-5)))

    if (verbose):
        print("Waiting for next row to be done")
    sleep(3)  # wait 3 seconds then exit


# if __name__ == '__main__':
#     pushRow(motor_row, grid, 0)
#     # pushColumn(motor_row)
