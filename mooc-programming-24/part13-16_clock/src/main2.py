import pygame

WINDOW_WIDTH = 640
WINDOOW_HEIGHT = 420
FPS = 60

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOOW_HEIGHT))
pygame.display.set_caption("A test pygame")
game_font = pygame.font.SysFont("Arial", 24)
text = game_font.render("Hello World!", True, (255, 0, 0))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    
    pygame.draw.rect(window, (0, 255, 0), (50, 100, 200, 250))
    pygame.draw.circle(window, (255, 0, 0), (200, 150), 40)
    pygame.draw.line(window, (0, 0, 255), (80, 120), (300, 160), 2)
    window.blit(text, (100, 50))
    
    pygame.display.flip()
    clock.tick(FPS)
