import math
import sys
from time import sleep

from process_input import (
    collect_grid_terminal_input,
    collect_grid_touch_sensor_input,
    print_grid,
)
from utils.brick import EV3ColorSensor, Motor, TouchSensor, wait_ready_sensors

from utils.sound import Sound
import simpleaudio as sa


preloaded_grid = [  # test arrow
    [1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
]


column_distances = [120, 136, 154, 175, 206]  # second pusher
row_distances = [254, 374, 479, 604, 734]


def push_motor_distance(motor, distance, delay=2):
    """
    Pushes the motor a certain distance and waits for it to finish and then returns to the original position.

    Args:
        motor: The motor to push
        distance: The distance to push the motor
        delay: The delay the motor should wait for extending and returning
    """
    motor_start_position = motor.get_position()
    motor.set_position(motor_start_position + distance)
    sleep(delay)
    motor.set_position(motor_start_position)
    sleep(delay)


def dispense_cube(motor, verbose):
    """
    Dispenses a cube from the dispenser. It is assumed that the dispenser is already in the correct position and will push a cube out.

    Args:
        motor: The motor to dispense the cube
    """
    motor.set_limits(dps=100)
    motor.set_position_relative(160)
    sleep(1.75)
    if verbose:
        print("push should be done")
    motor.set_position_relative(-160)
    sleep(1.75)
    if verbose:
        print("retraction should be done")
    motor.set_power(0)


def run_dispensing(grid, dispenser_motor, row_motor, column_motor, verbose):
    """
    Runs the dispensing of the cubes. It will push from the far corner to the near corner of the grid. 
    It will push the cubes out of the dispenser and then push the row motor to the correct position. 
    This will repeat until the all cubes in a row are dispensed and then the column motor will push them to their final position.

    Args:
        grid: The grid to dispense the cubes from
        dispenser_motor: The motor to dispense the cubes
        row_motor: The motor that pushes cubes coming from the dispenser
        column_motor: The motor to push a set of 5 cubes
    """
    row_motor.set_position_relative(-100)
    for i in range(4, -1, -1):
        cube_dispensed = False
        for j in range(4, -1, -1):
            if grid[i][j] == 1:
                if verbose:
                    print("About to dispense cube " + str(i) + " " + str(j))
                cube_dispensed = True
                # push_motor_distance(dispenser_motor,180,1.25)
                dispense_cube(dispenser_motor, verbose)
                if verbose:
                    print("About to push cube " + str(i) + " " + str(j))
                push_motor_distance(row_motor, row_distances[j])
        if cube_dispensed:
            if verbose:
                print("About to push column " + str(i))
            push_motor_distance(column_motor, -column_distances[i], 4)



def get_grid(touch_sensor_0, touch_sensor_1, verbose, preload_grid):
    """
    Collects the grid from the user. It will either use the preloaded grid or collect 
    the grid from the user using the touch sensors or the terminal.
    """
    if not preload_grid:
        grid = []

        if debug:
            collect_grid_terminal_input(grid)
        else:
            collect_grid_touch_sensor_input(
                grid, touch_sensor_0, touch_sensor_1, verbose
            )
    else:
        grid = preloaded_grid

    print_grid(grid)
    return grid


def check_loaded(color_sensor, verbose):
    """
    This function checks if the dispenser is loaded. It will continuously check if 
    the color sensor detects a color brighter than 25 and when it does it will return.
    """
    if verbose:
        print("Checking for 15 cubes in the dispenser")
    loaded = False
    count = 0
    while not loaded:
        sd = color_sensor.get_value()
        dist = math.sqrt(sd[0] ** 2 + sd[1] ** 2 + sd[2] ** 2)
        if verbose:
            print("{:d},{:d},{:d},{:d}\n".format(sd[0], sd[1], sd[2], sd[3]))
            print(dist)
        if dist > 25:
            count += 1
            if count >= 16:
                return
            else:
                sleep(0.25)
        else:
            count = 0
            if verbose:
                print("waiting for all cubes")
            sleep(0.25)
    return None


if __name__ == "__main__":
    """
    The main function that runs the program. It will initialize all the motoros and sensors, 
    wait for the cubes to be loaded, collect the grid from the user and then run the dispensing.
    """
    debug = "-d" in sys.argv
    verbose = "-v" in sys.argv
    preload_grid = "-p" in sys.argv
    if(debug):
        wave_object = sa.WaveObject.from_wave_file(
                    './utils/wav/terminal_input_mode.wav')
    else:
        wave_object = sa.WaveObject.from_wave_file(
                    './utils/wav/touch_sensor_input_mode.wav')
    
    play_object = wave_object.play()
    play_object.wait_done()

    touch_sensor_0 = TouchSensor(3)
    touch_sensor_1 = TouchSensor(4)
    colour_sensor = EV3ColorSensor(2)
    motor_column = Motor("D")  # Motor for the column pusher is in port D
    motor_column.set_limits(dps=100)  # speed of motor
    motor_row = Motor("B")  # Motor for the row pusher is in port B
    motor_row.set_limits(dps=500)
    motor_dispenser = Motor("C")  # Motor for the dispenser is in port C
    motor_dispenser.set_limits(dps=60)  # speed of motor
    wait_ready_sensors(verbose)

    wave_object = sa.WaveObject.from_wave_file('./utils/wav/loadcubes.wav')

    play_object = wave_object.play()
    play_object.wait_done()

    check_loaded(colour_sensor, verbose)
    wave_object = sa.WaveObject.from_wave_file(
                    './utils/wav/please_input_mosaic.wav')
    play_object = wave_object.play()
    play_object.wait_done()
    grid = get_grid(touch_sensor_0, touch_sensor_1, verbose, preload_grid)
    wave_object = sa.WaveObject.from_wave_file(
                    './utils/wav/about_to_start_placing.wav')
    play_object = wave_object.play()
    play_object.wait_done()
    # Run the program
    if verbose:
        print("\nStarting pistons...\n")
    run_dispensing(grid, motor_dispenser, motor_row, motor_column, verbose)

    wave_object = sa.WaveObject.from_wave_file('./utils/wav/mosaic_ready.wav')

    play_object = wave_object.play()
    play_object.wait_done()
