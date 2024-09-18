# gone back to simpler code for this exercise

import pygame

WINDOW_WIDTH, WINDOOW_HEIGHT = 640, 420
FPS = 60

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOOW_HEIGHT))

robot = pygame.image.load("robot.png")

robot_x = WINDOW_WIDTH // 2 -robot.get_width()/2
robot_y = WINDOOW_HEIGHT // 2 -robot.get_height()/2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            robot_x = event.pos[0]-robot.get_width()/2
            robot_y = event.pos[1]-robot.get_height()/2

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)