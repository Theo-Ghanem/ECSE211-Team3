#!/usr/bin/env python3

import sys

from process_input import (collect_grid_terminal_input,
                           collect_grid_touch_sensor_input, print_grid,
                           validate_grid, convert_grid_to_int)
from utils.brick import TouchSensor, Motor, wait_ready_sensors

from extender import push_row

def interpret_arguments():
    # Debug mode includes terminal binary input
    # Verbose mode includes additional print statements
    # Preload_grid mode includes a preloaded grid
    if (len(sys.argv) == 4):
        if "-d" in sys.argv and "-v" in sys.argv and "-p" in sys.argv:
            debug = True
            verbose = True
            preload_grid = True
        else:
            print("Invalid arguments")
            exit()

    elif len(sys.argv) == 3:
        if "-d" in sys.argv and "-v" in sys.argv and not "-p" in sys.argv:
            debug = True
            verbose = True
            preload_grid = False
        elif "-d" in sys.argv and not "-v" in sys.argv and "-p" in sys.argv:
            debug = True
            verbose = False
            preload_grid = True
        elif not "-d" in sys.argv and "-v" in sys.argv and "-p" in sys.argv:
            debug = False
            verbose = True
            preload_grid = True
        else:
            print("Invalid arguments")
            exit()

    elif len(sys.argv) == 2:
        if sys.argv[1] == "-d":
            debug = True
            verbose = False
            preload_grid = False
        elif sys.argv[1] == "-v":
            verbose = True
            debug = False
            preload_grid = False
        elif sys.argv[1] == "-p":
            verbose = False
            debug = False
            preload_grid = True
        else:
            print("Invalid arguments")
            exit()

    elif len(sys.argv) == 1:
        debug = False
        verbose = False
        preload_grid = False
    else:
        print("Invalid arguments")
        exit()
    return debug, verbose, preload_grid

preloaded_grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]


if __name__ == '__main__':
    # Interpret arguments
    debug, verbose, preload_grid = interpret_arguments()

    # Initialise the sensors
    touch_sensor_0 = TouchSensor(1)
    touch_sensor_1 = TouchSensor(2)
    motor_row = Motor("A")  # Motor for the row pusher is in port A
    motor_column = Motor("B")  # Motor for the column pusher is in port B

    wait_ready_sensors(verbose)

    # Collect input from the user if grid not preloaded
    if not preload_grid:
        grid = []

        if debug:
            collect_grid_terminal_input(grid)
        else:
            collect_grid_touch_sensor_input(
                grid, touch_sensor_0, touch_sensor_1, verbose)

        convert_grid_to_int(grid)
        
    else:
        grid = preloaded_grid

    validate_grid(grid, verbose)
    print_grid(grid)

    # Await user confirmation
    if debug:
        input("Press enter to proceed...")

    # Run the program
    for iteration in range(5):
        push_row(motor_row, motor_column, grid, iteration, verbose)
