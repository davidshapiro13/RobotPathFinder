# Draws the grpahics for the A* Robot Path Planner
#By David Shapiro, October 2025
from tkinter import *
from tkinter import messagebox
from constants import WAREHOUSE_HEIGHT, WAREHOUSE_WIDTH, GRID_WIDTH, GRID_HEIGHT, SCALE, ROBOT_W, ROBOT_H
from helpers import get_shape_from_center, get_pixel_from_index

#Learned how to do animation from
# https://www.w3resource.com/python-exercises/tkinter/python-tkinter-canvas-and-graphics-exercise-6.php

class Graphics():

    #Initializes Canvas
    def __init__(self, robot, path):
        self.root = Tk()
        self.robot = robot
        self.path = path
        self.carry_load = False
        self.canvas = Canvas(self.root, width=WAREHOUSE_WIDTH, height=WAREHOUSE_HEIGHT)
        self.robot_rect = self.canvas.create_rectangle(robot.start_x, robot.start_y, robot.start_x+robot.width, robot.start_y+robot.height, fill='red')
    
    #Optional grid, mainly for debugging
    def draw_grid(self):
        for i in range(GRID_WIDTH*SCALE + 1):
            y_start = WAREHOUSE_HEIGHT
            y_end = 0
            x = i * SCALE
            self.canvas.create_line(x, y_start, x, y_end, fill="gray")
        for i in range(GRID_HEIGHT * SCALE + 1):
            y = i * SCALE
            x_start = 0
            x_end = WAREHOUSE_WIDTH 
            self.canvas.create_line(x_start, y, x_end, y, fill="gray")

    def draw_fiducials(self):
        for i in range(1, GRID_WIDTH*SCALE + 1, 2):
            for j in range(1, GRID_HEIGHT*SCALE + 1, 2):
                x_start, y_start, w, h = get_shape_from_center(i*SCALE, j*SCALE, SCALE/4, SCALE/4)
                self.canvas.create_rectangle(x_start, y_start, x_start+w, y_start+h)
                
    def draw_goal(self, goalBlock):
        center_x = get_pixel_from_index(goalBlock.getX())
        center_y = get_pixel_from_index(goalBlock.getY())
        start_x, start_y, width, height = get_shape_from_center(center_x, center_y, ROBOT_W, ROBOT_H)
        self.canvas.create_rectangle(start_x, start_y, start_x+width, start_y+height, fill="blue")

    def draw_obstacles(self, obstacles, color):
        for obstacle in obstacles:
            start_x, start_y, width, height = obstacle.get_shape_values()
            self.canvas.create_rectangle(start_x, start_y, start_x+width, start_y+height, fill=color)
   
    def run(self, goal, obstacles, obstructions):
        self.goal = goal
        #self.draw_grid() uncomment if grid is helpful for you
        self.draw_fiducials()
        self.draw_goal(goal)
        self.draw_obstacles(obstacles, "white")
        self.draw_obstacles(obstructions, "pink")
        self.canvas.pack()

        start_button = Button(self.root,
                   text="Run Path Finder",
                   command=self.animate,
                   activebackground="white",
                   activeforeground="black",
                   anchor="center",
                   font=("Arial", 12),
                   padx=10,
                   pady=5)
        start_button.pack(padx=20, pady=20)
        mainloop()

    def animate(self):  
        if len(self.path) != 0:
            fiducial_x_center = get_pixel_from_index(self.path[0].getX())
            fiducial_y_center = get_pixel_from_index(self.path[0].getY())
            f_x, f_y, _, _ = get_shape_from_center(fiducial_x_center, fiducial_y_center, self.robot.width, self.robot.height)
            dx = f_x - self.robot.start_x
            dy = f_y - self.robot.start_y
            self.canvas.move(self.robot_rect, dx, dy)
            self.robot.start_x = f_x
            self.robot.start_y = f_y
            del self.path[0]
            if self.path != 0:
                self.root.after(800, self.animate)
        else:
            messagebox.showinfo("Success!", "Path was successfully found!") 
