#Simple Robot Class to initialize from
#Written by David Shapiro, October 2025
from helpers import get_shape_from_center
from constants import SCALE, ROBOT_W, ROBOT_H
class Robot():
    def __init__(self, payload=False):
        width = ROBOT_W
        height = ROBOT_H
        if payload:
            width = ROBOT_W + SCALE/2
            height = ROBOT_H + SCALE/2
        self.start_x, self.start_y, self.width, self.height = \
        get_shape_from_center(SCALE, SCALE, width, height)