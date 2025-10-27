# Main program for Robot Path Planner
#By David Shapiro, October 2025
import random
import numpy as np
from graphics import Graphics
from constants import SCALE, WAREHOUSE_WIDTH, WAREHOUSE_HEIGHT
from queue import PriorityQueue
import tkinter as tk
from helpers import PrioritizedItem, not_overlapping
from grid_block import Grid_Block
from robot import Robot

NUM_OBSTRUCTIONS = 10
#random.seed(325)

print("Welcome to the Robot Path Planner")
response = ""
while response != "y" and response != "n":
    response = input("Would you like the robot to have a payload? (y/n): ")
if response == "y":
    robot = Robot(payload=True)
else:
    robot = Robot()

#Generate obstacles
#start x, start y, w, h
obstacles = [(80, 60, 100, 20), (200, 125, 40, 75), (400, 15, 20, 50),
             (100, 275, 80, 100), (350, 275, 25, 50), (450, 300, 150, 20)]

#Generate obstructions
obstructions = []
while len(obstructions) < NUM_OBSTRUCTIONS:
    rand_w = random.randint(10, 50)
    rand_h = random.randint(10, 50)
    rand_x_start = random.randint(0, WAREHOUSE_WIDTH-rand_w)
    rand_y_start = random.randint(0, WAREHOUSE_HEIGHT-rand_h)
    if not_overlapping(rand_x_start, rand_y_start, rand_x_start+rand_w, rand_y_start+rand_h, obstacles+obstructions):
        obstructions.append((rand_x_start, rand_y_start, rand_w, rand_h))

#Checks if child is in frontier
def not_in_frontier(child, in_frontier):
    for item in in_frontier:
        if child.get_loc() == item.get_loc():
            return False
    return True

#A* Algorithm
def A_star(start_fiducial, goal_fiducial):

    #Intialize
    floor_map = np.zeros((WAREHOUSE_HEIGHT//(SCALE*2), WAREHOUSE_WIDTH//(SCALE*2)))
    frontier = PriorityQueue()
    frontier.put(PrioritizedItem(0, start_fiducial))
    in_frontier = [start_fiducial]

    while not frontier.empty():
        curr_node = frontier.get()
        curr_fiducial = curr_node.fiducial
        floor_map[curr_fiducial.getY()-1, curr_fiducial.getX()-1] = 1 #Visited

        if curr_fiducial.get_loc() == goal_fiducial.get_loc():
            return curr_fiducial.get_path()
        
        children = curr_fiducial.get_surrounding_nodes(obstacles, obstructions)
        for child in children:
            if not_in_frontier(child, in_frontier) and floor_map[child.getY()-1, child.getX()-1] != 1:
                new_path = curr_fiducial.get_path().copy()
                new_path.append(child)
                child.set_path(new_path)
                frontier.put(PrioritizedItem(child.get_pred_total_cost(goal_fiducial), child))
                in_frontier.append(child)


goal_node = Grid_Block(15, 10, 0)
path = A_star(Grid_Block(1, 1, 0), goal_node)

#Writes file with full path plan
with open('path.txt', 'w') as file:
    for item in path:
        file.write("X: " + str(item.getX()) + " Y:" + str(item.getY()) + " Curr Cost: " + str(item.curr_cost) + "\n")

#Runs Graphics
graphics = Graphics(robot, path)
graphics.run(goal_node, obstacles, obstructions)