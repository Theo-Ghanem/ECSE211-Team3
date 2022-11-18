import sys
from time import sleep
from utils.brick import TouchSensor, Motor, wait_ready_sensors

from process_input import (collect_grid_terminal_input,
                           collect_grid_touch_sensor_input, print_grid,
                           validate_grid, convert_grid_to_int)
preloaded_grid = [
    [1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1]
]
row_distances = [75.5, 80, 90, 110, 125]#second pusher
col_distances = [75.5, 80, 90, 110, 125]#first pusher


def push_motor_distance(motor, distance,delay=3):
    motor.set_position_relative(distance)
    while motor.is_moving():
        sleep(0.1)
    # print("push should be done",distance)
    sleep(delay)
    motor.set_position_relative(-distance)
    while motor.is_moving():
        sleep(0.1)
    # print("retraction should be done",-distance)
    sleep(delay)
def dispense_cube(motor):
    motor_dispenser.set_limits(dps=400) 
    motor.set_position_relative(180)
    while motor.is_moving():
        sleep(0.1)
    # print("push should be done")
    sleep(1.25)
    motor_dispenser.set_limits(dps=250) 
    motor.set_position_relative(-180)
    while motor.is_moving():
        sleep(0.1)
    # print("retraction should be done",-distance)
    sleep(1.25)
def run_dispensing(grid,dispenser_motor,col_motor,row_motor):
    for i in range(4,-1,-1):
        cube_dispensed = False
        for j in range(4,-1,-1):
            if grid[i][j] == 1:
                if debug:
                    input("About to dispense cube "+str(i)+" "+str(j))
                cube_dispensed = True
                # push_motor_distance(dispenser_motor,180,1.25)
                dispense_cube(dispenser_motor)
                if debug:
                    input("About to push cube "+str(i)+" "+str(j))
                push_motor_distance(col_motor,-col_distances[j])
        if cube_dispensed:
            if debug:
                input("About to push row "+str(i))
            push_motor_distance(row_motor,row_distances[i],4)

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
    touch_sensor_0 = TouchSensor(1)
    touch_sensor_1 = TouchSensor(2)
    motor_row = Motor("A")  # Motor for the row pusher is in port A
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
    
    run_dispensing(grid,motor_dispenser,motor_column,motor_row)