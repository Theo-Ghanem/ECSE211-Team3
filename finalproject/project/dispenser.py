

from utils.brick import Motor
from time import sleep

def dispense_cube(motor):
    motor.set_limits(dps=80)
    motor.set_position_relative(170)
    while motor.is_moving():
        sleep(0.1)
    # print("push should be done")
    sleep(1.5)
    motor.set_limits(dps=80)
    motor.set_position_relative(-170)
    while motor.is_moving():
        sleep(0.1)
    # print("retraction should be done",-distance)
    sleep(1.5)

motor_dispenser = Motor("C")  # Motor for the dispenser is in port C
motor_dispenser.set_limits(dps=60)  # speed of motor
dispense_cube(motor_dispenser)