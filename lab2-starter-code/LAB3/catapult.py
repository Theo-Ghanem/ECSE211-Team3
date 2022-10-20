from utils.brick import Motor
import time

motor_left = Motor("A")

# Set target speed first, 360 deg/sec
# Reset power limit to limitless with 0, default values:(power=0, dps=0)
motor_left.set_limits(dps=360)

# set current position to absolute pos 0deg
motor_left.reset_encoder()

# command to rotate 60deg away from current position
motor_left.set_position_relative(-160)
while motor_left.is_moving():
    time.sleep(0.1)
print("motor_left.set_position_relative(-160)")
input("Press any key to continue...")

# command to rotate 60deg away from current position
motor_left.set_position_relative(160)
while motor_left.is_moving():
    time.sleep(0.1)
print("motor_left.set_position_relative(160)")
input("Press any key to continue...")
