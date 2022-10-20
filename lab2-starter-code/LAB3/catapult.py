# from utils.brick import Motor
# import time

# motor_left = Motor("A")

# # Set target speed first, 360 deg/sec
# # Reset power limit to limitless with 0, default values:(power=0, dps=0)
# motor_left.set_limits(dps=360)

# # set current position to absolute pos 0deg
# motor_left.reset_encoder()

# # command to rotate 60deg away from current position
# motor_left.set_position_relative(60)
# while motor_left.is_moving():
#     time.sleep(0.1)
# print("motor_left.set_position_relative(60)")
# input("Press any key to continue...")

##############################
### Position-based Control ###
##############################

from utils.brick import Motor
import time

motor_left = Motor("A")

# Set target speed first, 360 deg/sec
# Reset power limit to limitless with 0, default values:(power=0, dps=0)
motor_left.set_limits(dps=360)

# set current position to absolute pos 0deg
motor_left.reset_encoder()

# command to move to absolute pos 270deg
motor_left.set_position(270)
print("motor_left.set_position(270)")
input("# Press any key to continue...")

# command to rotate 90deg away from current position
motor_left.set_position_relative(90)
print("motor_left.set_position_relative(90)")
input("Press any key to continue...")

"""Tests 3 different speeds. set_dps overrides set_limits.
dps=180, rotation_dist=720
dps=360, rotation_dist=1080
dps=540, rotation_dist=1440
"""
for i, speed in enumerate([180, 360, 180*3]):
    # overrides previous limits. Use limits or set_dps
    motor_left.set_dps(speed)
    motor_left.set_position_relative(360 * (i+2))
    motor_left.wait_is_moving()
    while motor_left.is_moving():
        time.sleep(0.1)
        print("actual speed=", motor_left.get_dps(), "actual power=",
              motor_left.get_power(), "status=", motor_left.get_status())
