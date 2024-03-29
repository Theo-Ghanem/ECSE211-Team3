#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor, reset_brick
from time import sleep


COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"
SENSOR_POLL = 0.05

# complete this based on your hardware setup
sw = EV3ColorSensor(1)
touch = TouchSensor(3)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    try:
        # f = open(COLOR_SENSOR_DATA_FILE, "w")
        running = False
        while True:
            sleep(0.01)
            if touch.is_pressed() and not running:
                print("pressed")
                sd = sw.get_value()
                print('{:d},{:d},{:d},{:d}\n'.format(sd[0],sd[1],sd[2],sd[3]))
                sleep(SENSOR_POLL)
                running = True
            elif not touch.is_pressed() :
                running = False


    # capture all exceptions including KeyboardInterrupt (Ctrl-C)
    except BaseException:
        pass
    finally:
        print("Done collecting color sensor")
        # f.close()
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()


if __name__ == "__main__":
    collect_color_sensor_data()
