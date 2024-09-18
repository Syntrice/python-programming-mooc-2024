# WRITE YOUR SOLUTION HERE:

import pygame, random

WINDOW_WIDTH, WINDOOW_HEIGHT, FPS = 640, 420, 60


class Application:
    def __init__(self, window_width: int, window_height: int, fps: int) -> None:
        pygame.init()
        self.window_width = window_width
        self.window_height = window_height
        self.fps = fps

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Asteroids")

        self.setup_images()
        self.setup_objects()
        
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.score = 0

        self.deltaclock = pygame.time.Clock()
        self.run()

    def setup_images(self) -> None:
        self.images: dict[str, pygame.Surface] = {
            "rock": pygame.image.load("rock.png"),
            "robot": pygame.image.load("robot.png"),
        }

    def setup_objects(self) -> None:
        self.asteroids: list[Asteroid] = []
        self.player = Player(
            self.images["robot"],
            self.window_width // 2 - self.images["robot"].get_width() // 2,
            self.window_height - self.images["robot"].get_height(),
            speed=4,
        )

    def spawn_asteroid(self) -> None:
        self.asteroids.append(
            Asteroid(
                self.images["rock"],
                random.randrange(
                    0, self.window_width - self.images["rock"].get_width()
                ),
                -self.images["rock"].get_height(),
                speed=1,
            )
        )

    def render(self) -> None:
        self.window.fill((0, 0, 0))

        self.window.blit(self.player.image, (self.player.x_pos, self.player.y_pos))

        for asteroid in self.asteroids:
            self.window.blit(asteroid.image, (asteroid.x_pos, asteroid.y_pos))

        # draw text
        text = self.game_font.render(f"Points: {self.score}", True, (255, 0, 0))
        self.window.blit(text, (WINDOW_WIDTH - text.get_width() - 20, 20))
        
        pygame.display.flip()

    def update(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            self.player.move_left = True
                        case pygame.K_RIGHT:
                            self.player.move_right = True
                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_LEFT:
                            self.player.move_left = False
                        case pygame.K_RIGHT:
                            self.player.move_right = False

        # check if player in bounds, only update if true
        if self.player.move_left and self.player.x_pos > 0:
            self.player.update()

        if (
            self.player.move_right
            and self.player.x_pos < self.window_width - self.player.image.get_width()
        ):
            self.player.update()

        # need to create a new list every update as some asteroids will go out of scope
        asteroids = []
        for asteroid in self.asteroids:

            # if asteroid hits ground, quit game
            if asteroid.y_pos > self.window_height - asteroid.image.get_height():
                exit()

            # if asteroid hits player
            x_hit = (
                asteroid.x_pos > self.player.x_pos - asteroid.image.get_width() and
                asteroid.x_pos < self.player.x_pos + self.player.image.get_width()
            )
            y_hit = (
                asteroid.y_pos > self.player.y_pos - asteroid.image.get_height() and
                asteroid.y_pos < self.player.y_pos + self.player.image.get_height()
            )

            if x_hit and y_hit:
                self.score += 1
                continue
            
            asteroid.update()

            asteroids.append(asteroid)

        self.asteroids = asteroids

        # attempt to spawn asteroid
        if random.random() < 0.005:
            self.spawn_asteroid()

    def run(self) -> None:
        while True:
            self.render()
            self.update()
            self.deltaclock.tick(self.fps)


class Entity:
    def __init__(self, image: pygame.Surface, x_pos: int, y_pos: int) -> None:
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos


class Player(Entity):
    def __init__(
        self, image: pygame.Surface, x_pos: int, y_pos: int, speed: int = 1
    ) -> None:
        self.speed = speed
        self.move_left = False
        self.move_right = False
        super().__init__(image, x_pos, y_pos)

    def update(self) -> None:
        self.x_pos += self.speed * (-1 * self.move_left + 1 * self.move_right)


class Asteroid(Entity):
    def __init__(
        self, image: pygame.Surface, x_pos: int, y_pos: int, speed: int = 1
    ) -> None:
        self.speed = speed
        super().__init__(image, x_pos, y_pos)

    def update(self) -> None:
        self.y_pos += self.speed


if __name__ == "__main__":
    application = Application(WINDOW_WIDTH, WINDOOW_HEIGHT, FPS)
