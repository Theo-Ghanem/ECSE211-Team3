#!/usr/bin/env python3

from asyncio import sleep
import sys

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
    count = 0
    for row in grid:
        for cell in row:
            if cell == "1" :
                count += 1
    if count != 15:
        print("Invalid grid. Please enter a grid with 15 1's and 10 0's.")
        exit()
    elif verbose:
        print("Grid is valid.\n")
    return count == 15

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

def collect_grid_touch_sensor_input(grid, touch_sensor_0, touch_sensor_1, verbose):
    try:
        for i in range(0, 4):
            for j in range(0, 4):

                running = False
                while True:
                    sleep(0.01)
                    if touch_sensor_0.is_pressed() and not running:
                        if (verbose):
                            print("Touch sensor 0 pressed")
                        grid[i][j] = "0"
                        running = True
                    elif not touch_sensor_0.is_pressed():
                        break

                    elif touch_sensor_1.is_pressed() and not running:
                        if (verbose):
                            print("Touch sensor 1 pressed")
                        grid[i][j] = "1"
                        running = True
                    elif not touch_sensor_1.is_pressed():
                        break

    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException:
        exit()