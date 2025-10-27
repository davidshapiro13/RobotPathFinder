#class for Barriers (obstacles and obstructions)
#Written by David Shapiro, October 2025

from constants import OBSTACLE_COST, OBSTRUCTION_COST
class Barrier():
    def __init__(self, start_x, start_y, width, height, type):
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height
        self.type = type
    def get_shape_values(self):
        return (self.start_x, self.start_y, self.width, self.height)
    def cost(self):
        if self.type == "obstacle":
            return OBSTACLE_COST
        else:
            return OBSTRUCTION_COST