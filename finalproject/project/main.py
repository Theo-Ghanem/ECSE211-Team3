#!/usr/bin/env python3

import sys

from process_input import (collect_grid_terminal_input,
                           collect_grid_touch_sensor_input, print_grid,
                           validate_grid)
from utils.brick import TouchSensor, Motor, wait_ready_sensors

from extender import pushRow, pushColumn


if __name__ == '__main__':
    # Debug mode includes terminal binary input
    # Verbose mode includes additional print statements
    if len(sys.argv) == 3:
        if "-d" in sys.argv and "-v" in sys.argv:
            debug = True
            verbose = True
        else:
            print("Invalid arguments")
            exit()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-d":
            debug = True
            verbose = False
        elif sys.argv[1] == "-v":
            verbose = True
            debug = False
        else:
            print("Invalid arguments")
            exit()
    elif len(sys.argv) == 1:
        debug = False
        verbose = False
    else:
        print("Invalid arguments")
        exit()

    # Initialise the sensors
    touch_sensor_0 = TouchSensor(1)
    touch_sensor_1 = TouchSensor(2)
    motor_row = Motor("A")  # Motor for the row pusher is in port A
    motor_column = Motor("B")  # Motor for the column pusher is in port B

    wait_ready_sensors(verbose)

    # Collect input from the user
    grid = []

    if debug:
        collect_grid_terminal_input(grid)
    else:
        collect_grid_touch_sensor_input(
            grid, touch_sensor_0, touch_sensor_1, verbose)

    validate_grid(grid, verbose)
    print_grid(grid)

    # Await user confirmation
    if debug:
        input("Press enter to proceed...")

    # Run the program
    for iteration in range(5):
        print("this is the grid" + str(grid))
        pushRow(motor_row, motor_column, grid, iteration, verbose)
        pushColumn(motor_column, iteration, True)
