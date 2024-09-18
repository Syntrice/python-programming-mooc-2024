# gone back to simpler code for this exercise

import pygame, random

WINDOW_WIDTH, WINDOOW_HEIGHT = 640, 420
FPS = 60

def set_random_position():
    robot_x = random.randrange(0, WINDOOW_HEIGHT - robot.get_width()) 
    robot_y = random.randrange(0, WINDOOW_HEIGHT - robot.get_height())
    
    return robot_x, robot_y

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOOW_HEIGHT))
robot = pygame.image.load("robot.png")
clock = pygame.time.Clock()

robot_x, robot_y = set_random_position()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.pos[0] > robot_x and event.pos[0] < robot_x + robot.get_width() and event.pos[1] > robot_y and event.pos[1] < robot_y + robot.get_height():
                robot_x, robot_y = set_random_position()

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)