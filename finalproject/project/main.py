#!/usr/bin/env python3

from asyncio import run
import sys
from threading import Thread

from process_input import collect_grid_terminal_input, validate_grid, print_grid, collect_grid_touch_sensor_input
from utils.brick import TouchSensor, wait_ready_sensors

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

    wait_ready_sensors(verbose)

    # Collect input from the user
    grid = []

    if debug:
        collect_grid_terminal_input(grid)
    else:
        collect_grid_touch_sensor_input(grid, touch_sensor_0, touch_sensor_1, verbose)


    validate_grid(grid, verbose)
    print_grid(grid)

    # Await user confirmation
    if debug:
        input("Press enter to proceed...")

    # Run the program






