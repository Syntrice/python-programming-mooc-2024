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

        self.load_images()
        self.create_objects()

        self.run()

    def load_images(self) -> None:
        self.game_images["robot"] = pygame.image.load("robot.png")

    def create_objects(self) -> None:
        for i in range(10):
            self.game_objects.append(CircularRobot(self.game_images["robot"], WINDOW_WIDTH // 2, WINDOOW_HEIGHT // 2, 150, 0.01, math.radians(36 * i)))



    def update(self) -> None:

        # monitor for exit command
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

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


class CircularRobot(Object):

    def __init__(
        self,
        image: pygame.Surface,
        origin_x: int,
        origin_y: int,
        orbit_radius: int,
        angular_velocity: float,
        angular_displacement: float = 0,
    ) -> None:
        self.orbit_radius = orbit_radius
        self.origin_x = origin_x - image.get_width() // 2
        self.origin_y = origin_y - image.get_height() //2
        self.angular_velocity = angular_velocity
        self.angular_displacement = angular_displacement
        
        x = int(self.orbit_radius * math.cos(self.angular_displacement)) + self.origin_x
        y = int(self.orbit_radius * math.sin(self.angular_displacement)) + self.origin_y

        super().__init__(image, x, y, 0, 0)

    def update_position(self) -> None:
        self.angular_displacement += self.angular_velocity
        self.x = int(self.orbit_radius * math.cos(self.angular_displacement)) + self.origin_x
        self.y = int(self.orbit_radius * math.sin(self.angular_displacement)) + self.origin_y


if __name__ == "__main__":
    game = GameApplication()
