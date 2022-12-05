from time import sleep

from utils.brick import TouchSensor
import sys, tty, termios


def get_char():
    """
    Reads a single character from standard input.  Does not echo to the screen.
    Note that this puts it in raw mode, therefore keyboard interrupts (ctrl-c) are not caught.

    This code was taken from:
    https://stackoverflow.com/questions/510357/how-to-read-a-single-character-from-the-user

    Returns:
        str : the character read
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def get_input_line():
    """
    Reads 5 binary inputs from the user, automatically spacing the inputs out on the screen, with input validation for only binary values.
    Keyboard interrupts (ctrl-c) are caught.

    Returns:
        int[5]: int array of length 5 holding the input 0s and 1s
    """
    input_line = []
    for _ in range(5):
        char = ""
        while char != "1" and char != "0":
            char = get_char()
            if ord(char) == 3:
                exit()
        print(char, end="", flush=True)
        input_line.append(int(char))
        print(" ", end="", flush=True)
    return input_line


def reprint_partial_grid(grid):
    """
    Reprints the grid that has been entered so far, with the cursor at the end of the last line.

    Args:
        grid (int[][]): grid that has been entered so far
    """
    print("Enter a list of 25 binary inputs:")
    print("  v v v v v")
    for row in grid:
        print("> ", end="")
        for cell in row:
            print(cell, end=" ")
        print("\n", end="")


def print_grid(grid):
    """
    Prints the grid to the screen in a use friendly format.

    Args:
        grid (int[][]): grid to print
    """
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
    """
    Collects the grid from the user in the terminal.  The user is prompted to enter 25 binary inputs.
    Input validation for binary values, maximum of 15 1s, and total of 25 inputs.

    Args:
        grid (int[][]): grid to fill with user input
    """
    valid_input = False
    input_array = []
    total_ones = 0

    print("\nEnter a list of 25 binary inputs:")
    print("  v v v v v")
    for _ in range(5):
        valid_input = False
        while not valid_input:
            print("> ", end="", flush=True)
            input_array = get_input_line()
            ones_in_line = sum(input_array)

            if ones_in_line + total_ones > 15:
                print(
                    "\033[31m"
                    + "-> Invalid line. Please enter a grid with at most 15 1's.\n"
                    + "\033[0;0m"
                )
                reprint_partial_grid(grid)
                continue

            total_ones += ones_in_line
            valid_input = True
            print("")

        grid.append(input_array)
    print("\n")


def collect_grid_touch_sensor_input(
    grid, touch_sensor_0: TouchSensor, touch_sensor_1: TouchSensor, verbose
):
    """
    Collects the grid from the user using the touch sensors.  The user is prompted to enter 25 binary inputs.
    Input validation for a maximum of 15 1s.

    Args:
        grid (int[][]): grid to fill with user input
        touch_sensor_0 (TouchSensor): touch sensor corresponding to input 0
        touch_sensor_1 (TouchSensor): touch sensor corresponding to input 1
        verbose (bool): whether to print extra information to the screen
    """

    try:
        total_ones = 0
        print("  v v v v v")
        for i in range(5):
            print("> ", end="", flush=True)
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
                        total_ones += 1
                        running_ts_1 = True
                    elif not touch_sensor_1.is_pressed() and running_ts_1:
                        running_ts_1 = False
                        break
            grid.append(row)

            print("")
        print("")

        if total_ones > 15:
            print(
                "\033[31m"
                + "Invalid grid. Please enter a grid with at most 15 1's.\n"
                + "\033[0;0m"
            )
            exit()

    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException as e:
        exit()
