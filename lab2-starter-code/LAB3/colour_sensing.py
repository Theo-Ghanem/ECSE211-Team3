#!/usr/bin/env python3

from this import d
from utils.brick import Motor, TouchSensor, wait_ready_sensors
from utils.sound import Sound
from time import sleep
import math

colors = (("red",(0.792319061, 0.09501644, 0.112664499)),("green",(0.145115189, 0.619367559, 0.235517252)), ("blue", (0.16760212, 0.27903289, 0.553365)), ("purple", (0.33923691, 0.206862466, 0.453900624)))
#target will be in the form of a tuple 
async def play_note(color_sensor, tone1, tone2, tone3, tone4):
    sleep(1)
    print("doing things")
    data_point = color_sensor.get_value()
    normalizePoint(data_point)
    closest_color = distance(data_point)
    print(data_point,closest_color)
    if closest_color == "red":
        tone1.play()
        tone1.wait_done()
    elif closest_color == "blue":
        tone2.play()
        tone2.wait_done()
    elif closest_color == "green":
        tone3.play()
        tone3.wait_done()
    else:
        tone4.play()
        tone4.wait_done()
    return None


def normalizePoint(data_point): 
    added_colors = data_point[0] + data_point[1] + data_point[2]
    for i in range(3): 
        data_point[i] = data_point[i]/added_colors 


def getColorDistance(color,target):
    return math.sqrt((color[0]-target[0])**2+(color[1]-target[1])**2+(color[2]-target[2])**2)

def distance(color): 
    return sorted(colors,key=lambda x:getColorDistance(color,x[1]))[0][0]
    