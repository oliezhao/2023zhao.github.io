aspect_ratio = (16,9)

screenx = 1920
screeny = screenx * (aspect_ratio[1]/aspect_ratio[0])

scale = int(screenx/256)

screen_resolution = (screenx, screeny)