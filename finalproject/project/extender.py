#!/usr/bin/env python3

from utils.brick import Motor, TouchSensor, wait_ready_sensors
from time import sleep

motor_row = Motor("A")  # remove this after
motor_column = Motor("B")  # remove this after

# constants for row distance:
row_distance = [140, 110, 90, 80, 60]
column_distance = [140, 110, 90, 80, 60]  # probably will be different than row

grid = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]


def pushRow(motor_row, grid, iteration):

    motor_row.set_limits(dps=80)  # speed of motor
    # make sure the motor is in correct position at start!
    motorStartPosition = motor_row.get_position()

    counter = 0
    for i in grid[iteration]:
        if i == 1:
            print("Cube " + str(counter+1) + " is loaded")
            distance = row_distance[counter]

            # make extender extend
            motor_row.set_position(motorStartPosition + distance)
            while motor_row.is_moving():
                sleep(0.1)
            print("Extender extend's to row " + str(abs(counter-5)))

            sleep(2)  # wait before retracting

            # make extender retract
            motor_row.set_position(motorStartPosition)
            while motor_row.is_moving():
                sleep(0.1)
            print("Extender retract's from row " + str(abs(counter-5)))

            sleep(5)  # wait 5 seconds for cube to load in

        counter += 1
    pushColumn(motor_column, iteration)


def pushColumn(motor_column, iteration):
    print("Pushing wall to column " + str(abs(iteration-5)))
    motor_column.set_limits(dps=80)  # speed of motor
    # make sure the motor is in correct position at start!
    motorStartPosition = motor_column.get_position()

    distance = column_distance[iteration]

    # make extender extend
    motor_column.set_position(motorStartPosition + distance)
    while motor_column.is_moving():
        sleep(0.1)
    print("wall extend's to column " + str(abs(iteration-5)))

    sleep(2)  # wait before retracting

    # make extender retract
    motor_column.set_position(motorStartPosition)
    while motor_column.is_moving():
        sleep(0.1)
    print("wall retract's from column " + str(abs(iteration-5)))

    print("Waiting for next row to be done")
    sleep(3)  # wait 3 seconds then exit


if __name__ == '__main__':
    pushRow(motor_row, grid, 0)
    # pushColumn(motor_row)
