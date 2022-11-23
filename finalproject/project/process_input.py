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
            if cell == 1:
                count_1 += 1
                count_total += 1
            elif cell == 0:
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
            if cell == 1:
                print(f"| X ", end="")
            else:
                print(f"|   ", end="")
        print("|\n", end="")
        print("+---+---+---+---+---+")
    print("\n")


def collect_grid_terminal_input(grid):
    valid_input = False
    grid_input = ""
    input_array = []
    input_lines = 0
    total_ones = 0

    print("\nEnter a list of 25 binary inputs with spaces as delimiters: ")
    print("  v v v v v")
    while input_lines < 5:
        while not valid_input:
            ones_before_input = total_ones
            num_inputs = 0

            grid_input = input("> ")
            grid_input = grid_input.strip()
            input_array = grid_input.split(" ")

            for i in range(len(input_array)):
                if input_array[i] == "1":
                    total_ones += 1
                    num_inputs += 1
                    input_array[i] = 1  # type: ignore
                elif input_array[i] == "0":
                    num_inputs += 1
                    input_array[i] = 0  # type: ignore

            if num_inputs != 5:
                total_ones = ones_before_input
                valid_input = False
                print("Invalid input. Please enter a list of 5 binary inputs with spaces as delimiters.\n")
                reprint_partial_grid(grid)
                continue

            if total_ones > 15:
                total_ones = ones_before_input
                valid_input = False
                print("Invalid grid. Please enter a grid with at most 15 1's.\n")
                reprint_partial_grid(grid)
                continue

            valid_input = True

        input_lines += 1
        valid_input = False

        grid.append(input_array)
    print("\n")


def collect_grid_touch_sensor_input(
    grid, touch_sensor_0: TouchSensor, touch_sensor_1: TouchSensor, verbose
):
    try:
        print("  v v v v v")
        for i in range(5):
            print("> ", end="")
            row = []
            for j in range(5):
                running_ts_0 = False
                running_ts_1 = False
                while True:
                    sleep(0.01)
                    if (
                        touch_sensor_0.is_pressed()
                        and not running_ts_0
                        and not running_ts_1
                    ):
                        print("0", end=" ", flush=True)
                        row.append(0)
                        running_ts_0 = True
                    elif not touch_sensor_0.is_pressed() and running_ts_0:
                        running_ts_0 = False
                        break

                    elif (
                        touch_sensor_1.is_pressed()
                        and not running_ts_0
                        and not running_ts_1
                    ):
                        print("1", end=" ", flush=True)
                        row.append(1)
                        running_ts_1 = True
                    elif not touch_sensor_1.is_pressed() and running_ts_1:
                        running_ts_1 = False
                        break
            grid.append(row)

            print("\n", end="")
        print("\n", end="")

    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException as e:
        print(e)
        exit()
