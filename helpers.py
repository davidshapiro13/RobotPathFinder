#Helper functions
#Written by David Shapiro, October 2025
from dataclasses import dataclass, field
from typing import Any
from constants import SCALE

#code borrowed from https://docs.python.org/3/library/queue.html
#to allow me to put a object in their priority queue
@dataclass(order=True)
class PrioritizedItem:
    cost: int
    fiducial: Any=field(compare=False)
#end of code from website


#Finds start x and start y based on center of shape
def get_shape_from_center(center_x, center_y, width, height):
    return (center_x - width/2, center_y - height/2, width, height)

#Finds actual pixel coordinate from fiducial index
def get_pixel_from_index(index):
    return (2 * index-1) * SCALE

#Checks if an item overlaps with an obstacle
def not_overlapping(low_x, low_y, high_x, high_y, obstacles):
    for obstacle in obstacles:
        ob_low_x, ob_low_y, ob_w, ob_h = obstacle
        ob_high_x =  ob_low_x + ob_w
        ob_high_y =  ob_low_y + ob_h
        if ob_low_y > high_y or ob_high_y < low_y or \
               ob_low_x > high_x or ob_high_x < low_x:
            pass
        else:
            return False
    return True