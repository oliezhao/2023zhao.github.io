import json
from math import atan2, degrees

def write():
    with open("settings.txt", "w") as file:
        json.dump(data, file)
        
with open("settings.txt") as file:
    data = json.load(file)
    
    screenx = data["screenx"]
    screeny = data["screeny"]
    resolution = (screenx, screeny)
    scale = screenx/256

def get_angle(cords1, cords2):
    dy = -(cords2[1] - cords1[1])
    dx = cords2[0] - cords1[0]
    
    angle = atan2(dy, dx)

    return round(degrees(angle))