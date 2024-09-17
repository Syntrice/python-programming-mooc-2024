import pygame
import random as rand

WINDOW_WIDTH, WINDOOW_HEIGHT = 640, 420
FPS = 60


class GameApplication:

    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.game_objects: list[Object] = []
        self.game_images: dict[str, pygame.Surface] = {}

        self.load_images()
        #self.create_objects()

        self.run()

    def load_images(self) -> None:
        self.game_images["robot"] = pygame.image.load("robot.png")

    #def create_objects(self) -> None:
    #   pass
    
    def attempt_spawn_robot(self):
        if rand.random() < 0.01:
            self.game_objects.append(Robot(self.game_images["robot"]))
        

    def update(self) -> None:

        # monitor for exit command
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        self.attempt_spawn_robot()
        
        # update objects
        for obj in self.game_objects:
            obj.update_position()
        
        # delete objects as required. probably a very bad way to do this
        self.game_objects = [obj for obj in self.game_objects if not obj.to_delete]

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
        self.to_delete = False

    def update_position(self) -> None:
        self.x += self.x_vel
        self.y += self.y_vel
        
class Robot(Object):
    
    def __init__(self, image: pygame.Surface, speed: int = 2) -> None:
        x_pos = rand.randint(0, WINDOOW_HEIGHT - image.get_width())
        y_pos = -1 * image.get_height()
        
        self.speed = speed
        
        super().__init__(image, x_pos, y_pos, 0, speed)
        
    def update_position(self) -> None:
        self.x += self.x_vel
        self.y += self.y_vel
        
        # check if landed
        if self.y_vel > 0 and self.y + self.image.get_height() > WINDOOW_HEIGHT:
            self.y = WINDOOW_HEIGHT - self.image.get_height()
            self.y_vel = 0
            self.x_vel = self.speed * rand.choice([-1,1])
        
        # check to delete object once off screen to avoid memory leak
        if self.x < 0 - self.image.get_width() or self.x > WINDOW_WIDTH:
            self.to_delete = True

if __name__ == "__main__":
    game = GameApplication()
