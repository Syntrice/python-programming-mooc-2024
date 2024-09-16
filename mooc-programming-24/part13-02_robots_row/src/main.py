# WRITE YOUR SOLUTION HERE:

import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480

# initializes the pygame modules
pygame.init()

# create a window, set the width and height to 640 x 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# load image from path
robot = pygame.image.load("robot.png")

# get the width and height of the robot image
robot_width = robot.get_width()
robot_height = robot.get_height()

# fill the window with rgb color tuple (black)
window.fill((0, 0, 0))

# variables
num_robots = 10
left_offset = (WINDOW_WIDTH - num_robots * robot_width) / 2
vertical_center = (WINDOW_HEIGHT - robot_height) / 2

# draw the robot images onto the window surface
for i in range(num_robots):
    window.blit(robot, (left_offset + robot_width * i, vertical_center))

# flip updates the contents of the window
pygame.display.flip()

# main game loop
while True:

    # return a list of events collected since previous iteration, iterates
    for event in pygame.event.get():

        # quit event causes program to exit through the exit function
        if event.type == pygame.QUIT:
            exit()
