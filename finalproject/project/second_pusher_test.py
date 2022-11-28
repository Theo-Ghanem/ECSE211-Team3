from time import sleep
from utils.brick import Motor



distances = [-120, -138, -158, -175, -205]

def push_motor_distance(motor, distance, delay=3):
    motor_start_position = motor.get_position()
    motor.set_position(motor_start_position + distance)
    # motor.set_position_relative(distance)
    while motor.is_moving():
        sleep(0.1)
    sleep(delay)
    motor.set_position(motor_start_position-1)
    while motor.is_moving():
        sleep(0.1)
    # print("retraction should be done",-distance)
    sleep(delay)

if __name__ == "__main__":
    motor = Motor("D")  # Motor for the row pusher is in port B
    motor.set_limits(dps=70)
    rev_distances = distances
    rev_distances.reverse()
    for distance in rev_distances:
        push_motor_distance(motor,distance)
    
