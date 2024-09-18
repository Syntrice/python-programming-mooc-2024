# WRITE YOUR SOLUTION HERE:
import pygame

WINDOW_WIDTH, WINDOOW_HEIGHT = 640, 420
FPS = 60
import math


class GameApplication:

    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.game_objects: list[Object] = []
        self.game_images: dict[str, pygame.Surface] = {}
        self.player: Player

        self.load_images()
        self.create_objects()

        self.run()

    def load_images(self) -> None:
        self.game_images["robot"] = pygame.image.load("robot.png")

    def create_objects(self) -> None:
        
        self.player = Player(self.game_images["robot"], x = 20, y = 20, speed=5)
        self.game_objects.append(self.player)

    def update(self) -> None:

        # monitor for exit command
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            self.player.x_vel = -1 * self.player.speed
                        case pygame.K_RIGHT:
                            self.player.x_vel = 1 * self.player.speed
                        case pygame.K_UP:
                            self.player.y_vel = -1 * self.player.speed
                        case pygame.K_DOWN:
                            self.player.y_vel = 1 * self.player.speed
                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_LEFT:
                            self.player.x_vel = 0
                        case pygame.K_RIGHT:
                            self.player.x_vel = 0
                        case pygame.K_UP:
                            self.player.y_vel = 0
                        case pygame.K_DOWN:
                            self.player.y_vel = 0
        

        # update objects
        for obj in self.game_objects:
             obj.update_position()

    def render(self) -> None:

        # clear window
        self.window.fill((0, 0, 0))

        # render objects
        for obj in self.game_objects:
            self.window.blit(obj.image, (obj.x, obj.y))

        # render display
        pygame.display.flip()

    def run(self) -> None:
        while True:
            self.render()
            self.update()
            self.clock.tick(FPS)


class Object:

    def __init__(
        self,
        image: pygame.Surface,
        x: int = 0,
        y: int = 0,
        x_vel: int = 0,
        y_vel: int = 0,
    ) -> None:
        self.image = image
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel

    def update_position(self) -> None:
        self.x += self.x_vel
        self.y += self.y_vel
        
class Player(Object):
    
    def __init__(self, image: pygame.Surface, x: int = 0, y: int = 0, speed: int = 1) -> None:
        self.speed = speed
        super().__init__(image, x, y, 0, 0)
        
    def update_position(self) -> None:
        if self.x_vel > 0 and self.x < WINDOW_WIDTH - self.image.get_width():
            self.x += self.x_vel
        elif self.x_vel < 0 and self.x > 0:
            self.x += self.x_vel
        
        if self.y_vel > 0 and self.y < WINDOOW_HEIGHT - self.image.get_height():
            self.y += self.y_vel
        elif self.y_vel < 0 and self.y > 0:
            self.y += self.y_vel


if __name__ == "__main__":
    game = GameApplication()
