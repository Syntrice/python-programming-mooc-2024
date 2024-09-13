
# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

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
window.fill((0,0,0))

# draw the robot images onto the window surface
window.blit(robot, (0,0))
window.blit(robot, (WINDOW_WIDTH - robot_width, 0))
window.blit(robot, (WINDOW_WIDTH - robot_width, WINDOW_HEIGHT - robot_height))
window.blit(robot, (0,WINDOW_HEIGHT - robot_height))

# flip updates the contents of the window
pygame.display.flip()

# main game loop
while True:
    
    # return a list of events collected since previous iteration, iterates
    for event in pygame.event.get():
        
        # quit event causes program to exit through the exit function
        if event.type == pygame.QUIT:
            exit()