import sys
from time import sleep

from process_input import (collect_grid_terminal_input,
                           collect_grid_touch_sensor_input,
                           convert_grid_to_int, print_grid, validate_grid)
from utils.brick import Motor, TouchSensor, wait_ready_sensors

# preloaded_grid = [
#     [1, 0, 1, 0, 0],
#     [0, 1, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 1, 0],
#     [0, 0, 1, 0, 1]
# ]

preloaded_grid = [  # test column
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# preloaded_grid = [  # test row
#     [1, 1, 1, 1, 1],
#     [1, 1, 0, 0, 0],
#     [1, 0, 1, 0, 0],
#     [1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 1]
# ]


row_distances = [44, 57, 69, 84, 100]  # second pusher
# col_distances = [70, 82, 92, 105, 128]  # first pusher #old
# col_distances = [88, 100, 110, 128, 150]  # first pusher #new
col_distances = [-50, -58, -65, -73, -82]  # first pusher #new


def push_motor_distance(motor, distance, delay=3):
    motor_start_position = motor.get_position()
    motor.set_position(motor_start_position + distance)
    # motor.set_position_relative(distance)
    while motor.is_moving():
        sleep(0.1)
    # print("push should be done",distance)
    sleep(delay)
    motor.set_position(motor_start_position)
    # motor.set_position_relative(-distance)
    while motor.is_moving():
        sleep(0.1)
    # print("retraction should be done",-distance)
    sleep(delay)


def dispense_cube(motor):
    motor_dispenser.set_limits(dps=150)
    motor.set_position_relative(80)
    while motor.is_moving():
        sleep(0.1)
    # print("push should be done")
    sleep(1.25)
    motor_dispenser.set_limits(dps=250)
    motor.set_position_relative(-80)
    while motor.is_moving():
        sleep(0.1)
    # print("retraction should be done",-distance)
    sleep(1.25)


def run_dispensing(grid, dispenser_motor, col_motor, row_motor):
    for i in range(4, -1, -1):
        cube_dispensed = False
        for j in range(4, -1, -1):
            if grid[i][j] == 1:
                if debug:
                    input("About to dispense cube "+str(i)+" "+str(j))
                cube_dispensed = True
                # push_motor_distance(dispenser_motor,180,1.25)
                dispense_cube(dispenser_motor)
                if debug:
                    input("About to push cube "+str(i)+" "+str(j))
                push_motor_distance(col_motor, -col_distances[j])
        if cube_dispensed:
            if debug:
                input("About to push row "+str(i))
            push_motor_distance(row_motor, -row_distances[i], 4)


def get_grid(touch_sensor_0, touch_sensor_1, verbose, preload_grid):
    if not preload_grid:
        grid = []

        if debug:
            collect_grid_terminal_input(grid)
        else:
            collect_grid_touch_sensor_input(
                grid, touch_sensor_0, touch_sensor_1, verbose)

        grid = convert_grid_to_int(grid)

    else:
        grid = preloaded_grid
    validate_grid(grid, verbose)
    print_grid(grid)
    return grid


if __name__ == '__main__':
    debug = '-d' in sys.argv
    verbose = '-v' in sys.argv
    preload_grid = '-p' in sys.argv
    touch_sensor_0 = TouchSensor(3)
    touch_sensor_1 = TouchSensor(4)
    motor_row = Motor("D")  # Motor for the row pusher is in port D
    motor_row.set_limits(dps=70)  # speed of motor
    motor_column = Motor("B")  # Motor for the column pusher is in port B
    motor_column.set_limits(dps=80)
    motor_dispenser = Motor("C")  # Motor for the dispensor is in port C
    motor_dispenser.set_limits(dps=250)  # speed of motor
    wait_ready_sensors(verbose)

    grid = get_grid(touch_sensor_0, touch_sensor_1, verbose, preload_grid)

    if debug:
        input("Press enter to proceed...")
    # Run the program
    if verbose:
        print("\nStarting pistons...\n")
    # print(motor_column.get_position())
    run_dispensing(grid, motor_dispenser, motor_column, motor_row)
