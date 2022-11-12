#!/usr/bin/env python3

from utils.brick import Motor, TouchSensor, wait_ready_sensors
from time import sleep

motor_row = Motor("A")  # remove this after
motor_column = Motor("B")  # remove this after

# constants for row distance:
row_distance = [140, 100, 60, 40, 20]

grid = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]


def pushRow(motor_row, grid, iteration):
    # command to rotate 140deg away from current position

    motor_row.set_limits(dps=100)
    motorStartPosition = motor_row.get_position()

    counter = 0
    for i in grid[iteration]:
        if i == 1:
            distance = row_distance[counter]

            # make extender extend
            motor_row.set_position(motorStartPosition + distance)
            while motor_row.is_moving():
                sleep(0.1)
            print("motor_row.set_position(motorStartPosition + distance)")
            sleep(2)  # wait before retracting

            # make extender retract
            # motor_row.set_limits(dps=100)
            motor_row.set_position(motorStartPosition)
            while motor_row.is_moving():
                sleep(0.1)
            print("motor_column.set_position(motorStartPosition)")

            sleep(5)
            # motor_row.set_power(0)  # always do 0% to stop motor
            # print("motor_left.set_power(0)")

        counter += 1


def pushColumn(motor_column):
    # command to rotate 80deg away from current position
    motor_column.set_limits(dps=100)
    motorStartPosition = motor_column.get_position()
    motor_column.set_position(motorStartPosition + 140)
    while motor_column.is_moving():
        sleep(0.1)
    print("motor_column.set_position (motorStartPosition + 140)")

    sleep(2)
    # command to rotate 80deg away from current position
    motor_column.set_limits(dps=100)
    motor_column.set_position(motorStartPosition)
    while motor_column.is_moving():
        sleep(0.1)
    print("motor_left.set_position(motorStartPosition)")

    sleep(1)
    motor_column.set_power(0)  # always do 0% to stop motor
    print("motor_left.set_power(0)")


if __name__ == '__main__':
    pushRow(motor_row, grid, 0)
    # pushColumn(motor_row)
