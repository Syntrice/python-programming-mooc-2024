"""

For this exercise, I created some boilerplate code to allow easy complition of the future 
exercises. That's why it might seem a bit over the top for this particular exercise.
Might be good to make some of the attributes private or protected.
"""

import pygame


WINDOW_WIDTH, WINDOOW_HEIGHT = 640, 420
FPS = 60


class Application:
    def __init__(self) -> None:

        pygame.init()

        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.objects: list[Object] = []

        self.load_sprites()
        self.create_objects()
        self.run()

    def load_sprites(self) -> None:
        self.robotSprite = pygame.image.load("robot.png")

    def create_objects(self) -> None:
        self.objects.append(Object(self.robotSprite, x=0, y=0, xvel=1, yvel=0))

    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        for obj in self.objects:
            obj.update_position()

    def render(self) -> None:
        self.window.fill((0, 0, 0))
        for obj in self.objects:
            self.window.blit(obj.sprite, (obj.x, obj.y))
        pygame.display.flip()

    def run(self) -> None:
        while True:
            self.render()
            self.update()
            self.clock.tick(FPS)


class Object:
    def __init__(
        self,
        sprite: pygame.Surface,
        x: int = 0,
        y: int = 0,
        xvel: int = 0,
        yvel: int = 0,
    ) -> None:

        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.sprite = sprite

    def update_position(self):
        self.x += self.xvel
        self.y += self.yvel
        
        self.window_collison_follow_perimiter()


    def window_collision_bounce(self):
        if self.xvel > 0 and self.x + self.sprite.get_width() > WINDOW_WIDTH:
            self.xvel = -self.xvel
        elif self.xvel < 0 and self.x <= 0:
            self.xvel = -self.xvel

        if self.yvel > 0 and self.y + self.sprite.get_height() > WINDOOW_HEIGHT:
            self.yvel = -self.yvel
        elif self.yvel < 0 and self.y <= 0:
            self.yvel = -self.yvel
            
    def window_collison_follow_perimiter(self):
        # moves clockwise round the permiter once hit
        if self.xvel > 0 and self.x + self.sprite.get_width() > WINDOW_WIDTH:
            self.yvel = self.xvel
            self.xvel = 0
        elif self.xvel < 0 and self.x <= 0:
            self.yvel = self.xvel
            self.xvel = 0

        if self.yvel > 0 and self.y + self.sprite.get_height() > WINDOOW_HEIGHT:
            self.xvel = -self.yvel
            self.yvel = 0
        elif self.yvel < 0 and self.y <= 0:
            self.xvel = -self.yvel
            self.yvel = 0
        


if __name__ == "__main__":
    game = Application()
