from pygame import *

def read_file(input_file, info):

    info = info + ":" #info in settings.txt should be formatted info_name: info. E.g resolution_x: 100
    start = len(info) + 1 #accounts for space in formatting
    
    with open(input_file, "r") as file: #sets file = open(input_file, "r") but closes it when operations are done
        for line in file.readlines():
            line = line.strip()
            if info in line:
                return int(line[start:])

screen_res_x = read_file("settings.txt", "resolution_x")
screen_res_y = read_file("settings.txt", "resolution_y")
screen_res = (screen_res_x, screen_res_y)