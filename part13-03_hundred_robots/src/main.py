# WRITE YOUR SOLUTION HERE:

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
robot_height = robot.get_height() / 4

# fill the window with rgb color tuple (black)
window.fill((0, 0, 0))

# variables
rows, cols = 10, 10
stagger_magnitude = 10
horizontal_offset = (WINDOW_WIDTH - robot_width * cols) / 2 - (cols / 2) * stagger_magnitude
vertical_offset = (WINDOW_HEIGHT - robot_height * rows) / 2 - robot_height


# draw the robot images onto the window surface
for i in range(rows):
    for j in range(cols):
        window.blit(robot, (horizontal_offset + i * stagger_magnitude + robot_width * j, vertical_offset + robot_height * i))
        

# flip updates the contents of the window
pygame.display.flip()

# main game loop
while True:

    # return a list of events collected since previous iteration, iterates
    for event in pygame.event.get():

        # quit event causes program to exit through the exit function
        if event.type == pygame.QUIT:
            exit()
