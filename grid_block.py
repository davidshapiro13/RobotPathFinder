#Defines a grid block of the graph
#Written by David Shapiro, October 2025
from constants import GRID_HEIGHT, GRID_WIDTH, HIGH_COST, ROBOT_W, ROBOT_H
from helpers import get_shape_from_center, not_overlapping, get_pixel_from_index

class Grid_Block():
    def __init__(self, x_loc, y_loc, curr_cost):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.curr_cost = curr_cost
        self.path = []
    
    def getY(self):
        return self.y_loc
    def getX(self):
        return self.x_loc
    
    def get_loc(self):
        return (self.getX(), self.getY())

    #Finds all nodes around it(left, right, up, down)
    def get_surrounding_nodes(self, obstacles, obstructions):
        avoid = obstacles + obstructions
        collection = []
        if self.x_loc > 1:
            collection.append(Grid_Block(self.x_loc - 1, self.y_loc, self.calc_cost(self.x_loc - 1, self.y_loc, avoid)))
        if self.y_loc > 1:
            collection.append(Grid_Block(self.x_loc, self.y_loc - 1, self.calc_cost(self.x_loc, self.y_loc - 1, avoid)))
        if self.y_loc < GRID_HEIGHT :
            collection.append(Grid_Block(self.x_loc, self.y_loc + 1, self.calc_cost(self.x_loc, self.y_loc + 1, avoid)))
        if self.x_loc < GRID_WIDTH:
            collection.append(Grid_Block(self.x_loc + 1, self.y_loc, self.calc_cost(self.x_loc + 1, self.y_loc, avoid)))
        return collection
    
    #updates path
    def set_path(self, new_path):
        self.path = new_path

    def get_path(self):
        return self.path
    
    #How far is the goal from current node (manhattan distance)
    def get_heuristic(self, goal_node):
        manhattan = abs(self.x_loc - goal_node.x_loc) + \
                    abs(self.y_loc - goal_node.y_loc)
        return manhattan
    
    #How much will moving to a given node cost
    def calc_cost(self, new_x, new_y, avoid):
        total_cost = self.curr_cost + 1 #increase by one for normal move
        curr_x_center_loc = get_pixel_from_index(self.x_loc)
        new_x_center_loc = get_pixel_from_index(new_x)
        curr_y_center_loc = get_pixel_from_index(self.y_loc)
        new_y_center_loc = get_pixel_from_index(new_y)

        curr_x_loc, curr_y_loc, _, _ = get_shape_from_center(curr_x_center_loc, curr_y_center_loc, ROBOT_W, ROBOT_H)
        new_x_loc, new_y_loc, _, _ = get_shape_from_center(new_x_center_loc, new_y_center_loc, ROBOT_W, ROBOT_H)

        high_x = max(curr_x_loc+ROBOT_W, new_x_loc+ROBOT_W)
        high_y = max(curr_y_loc+ROBOT_H, new_y_loc+ROBOT_H)
        low_x  = min(curr_x_loc, new_x_loc)
        low_y  = min(curr_y_loc, new_y_loc)

        if not not_overlapping(low_x, low_y, high_x, high_y, avoid):
            total_cost += HIGH_COST
        return total_cost

    #Predicted total cost given movement
    def get_pred_total_cost(self, goal_node):
        heuristic_cost = self.get_heuristic(goal_node)
        return self.curr_cost + heuristic_cost
    
    def get_path(self):
        return self.path