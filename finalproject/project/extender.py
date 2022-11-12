#!/usr/bin/env python3

from utils.brick import Motor, TouchSensor, wait_ready_sensors
from time import sleep

motor_row = Motor("A")  # remove this after
motor_column = Motor("B")  # remove this after


def pushRow(motor_row):
    # command to rotate 80deg away from current position
    motor_row.set_limits(dps=100)
    motor_row.set_position_relative(140)
    while motor_row.is_moving():
        sleep(0.1)
    print("motor_left.set_position_relative(-140)")

    sleep(2)
    # command to rotate 80deg away from current position
    motor_row.set_limits(dps=100)
    motor_row.set_position_relative(-140)
    while motor_row.is_moving():
        sleep(0.1)
    print("motor_left.set_position_relative(140)")

    sleep(1)
    motor_row.set_power(0)  # always do 0% to stop motor
    print("motor_left.set_power(0)")


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
    pushColumn(motor_row)
