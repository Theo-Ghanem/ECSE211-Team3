#!/usr/bin/env python3

from time import sleep
from utils.brick import TouchSensor

def reprint_partial_grid(grid):
    print("Enter a list of 25 binary inputs with spaces as delimiters: ")
    print("  v v v v v")
    for row in grid:
        print("> ", end="")
        for cell in row:
            print(cell, end=" ")
        print("\n", end="")

def validate_grid(grid, verbose):
    if verbose:
        print("Validating grid...")
    count_1 = 0
    count_total = 0
    for row in grid:
        for cell in row:
            if cell == "1" :
                count_1 += 1
                count_total += 1
            elif cell == "0":
                count_total += 1
    if count_1 > 15:
        print("Invalid grid. Please enter a grid with at most 15 1's.")
        exit()
    elif count_total != 25:
        print("Invalid grid. Please enter 25 binary inputs.")
        exit()
    elif verbose:
        print("Grid is valid.\n")
    return count_1 <= 15 and count_total == 25

def print_grid(grid):
    print("\nThe robot will place cubes at the following locations:")
    print("+---+---+---+---+---+")
    for row in grid:
        for cell in row:
            if cell == "1":
                print(f"| X ", end="")
            else:
                print(f"|   ", end="")
        print("|\n", end="")
        print("+---+---+---+---+---+")
    print("\n")

def collect_grid_terminal_input(grid):
    valid_input = False
    grid_input = ""
    input_lines = 0

    print("Enter a list of 25 binary inputs with spaces as delimiters: ")
    print("  v v v v v")
    while input_lines < 5:
        while not valid_input:
            grid_input = input("> ")
            grid_input = grid_input.strip()
            if len(grid_input) != 9:
                print("\nInvalid input. Please enter 5 binary inputs.\n")
                reprint_partial_grid(grid)
                continue
            valid_input = True
        
        input_lines += 1
        valid_input = False

        array = grid_input.split(" ")
        grid.append(array)
    print("\n")

def collect_grid_touch_sensor_input(grid, touch_sensor_0: TouchSensor, touch_sensor_1: TouchSensor, verbose):
    try:
        print ("  v v v v v")
        for i in range(0, 5):
            print("> ", end="")
            row = []
            for j in range(0, 5):
                running_ts_0 = False
                running_ts_1 = False
                while True:
                    sleep(0.01)
                    if touch_sensor_0.is_pressed() and not running_ts_0:
                        print("0", end=" ")
                        row.append("0")
                        running_ts_0 = True
                    elif not touch_sensor_0.is_pressed() and running_ts_0:
                        running_ts_0 = False
                        break
                        

                    elif touch_sensor_1.is_pressed() and not running_ts_1:
                        # if running_ts_0:
                        #     print("Aborting input")
                        #     exit()
                        print("1", end=" ")
                        row.append("1")
                        running_ts_1 = True
                    elif not touch_sensor_1.is_pressed() and running_ts_1:
                        running_ts_1 = False
                        break
            print(row)
            grid.append(row)

                        
            print("\n", end="")
        print("\n", end="")

    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException as e:
        print(e)
        exit()