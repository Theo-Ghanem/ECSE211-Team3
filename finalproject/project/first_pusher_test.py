from time import sleep
from utils.brick import Motor



distances = [300, 400, 530, 635, 745]  # first pusher #new



def push_motor_distance(motor, distance, delay=3):
    motor_start_position = motor.get_position()
    motor.set_position(motor_start_position + distance)
    # motor.set_position_relative(distance)
    while motor.is_moving():
        sleep(0.1)
    sleep(delay)
    motor.set_position(motor_start_position)
    while motor.is_moving():
        sleep(0.1)
    # print("retraction should be done",-distance)
    sleep(delay)

if __name__ == "__main__":
    motor_row = Motor("B")  # Motor for the row pusher is in port B
    motor_row.set_limits(dps=360)
    for distance in distances.reverse():
        push_motor_distance(motor_row,distance)
    
