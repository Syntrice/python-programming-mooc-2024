import pygame, math, time
from datetime import datetime

WINDOW_WIDTH, WINDOOW_HEIGHT, FPS = 640, 420, 60


class Application:
    def __init__(self, window_width: int, window_height: int, fps: int) -> None:
        self.window_width = window_width
        self.window_height = window_height
        self.fps = fps

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.deltaclock = pygame.time.Clock()
        self.clock = TimeClock(
            self.window_width // 2, self.window_height // 2, 175, datetime.now()
        )
        self.run()

    def render(self) -> None:
        self.window.fill((0, 0, 0))
        self.clock.render(self.window)
        pygame.display.flip()

    def update(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    exit()
        time_now = datetime.now()

        self.clock.update(time_now)
        pygame.display.set_caption(time_now.strftime("%H:%M:%S"))

    def run(self) -> None:
        while True:
            self.render()
            self.update()
            self.deltaclock.tick(self.fps)


class TimeClock:
    def __init__(self, x_pos: int, y_pos: int, radius: float, time: datetime) -> None:
        self.update(time)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius

    def update(self, time: datetime) -> None:
        self._hour = time.hour % 12
        self._minute = time.minute
        self._second = time.second

    # this method is quite complex and I would ideally handle rendering somewhere else.
    # I would perhaps use objects to represent shapes, then offload the drawing of these shapes to the application object.
    # But this method works fine.

    def render(self, display: pygame.surface.Surface):

        pygame.draw.circle(
            display, (255, 0, 0), (self.x_pos, self.y_pos), 0.05 * self.radius
        )
        pygame.draw.circle(
            display,
            (255, 0, 0),
            (self.x_pos, self.y_pos),
            self.radius,
            width=int(self.radius * 0.03),
        )

        hour_angle = 2 * math.pi * (self._hour / 12) - 0.5 * math.pi
        minute_angle = 2 * math.pi * (self._minute / 60) - 0.5 * math.pi
        second_angle = 2 * math.pi * (self._second / 60) - 0.5 * math.pi

        hour_pos = (
            self.x_pos + self.radius * 0.75 * math.cos(hour_angle),
            self.y_pos + self.radius * 0.70 * math.sin(hour_angle),
        )

        minute_pos = (
            self.x_pos + self.radius * 0.80 * math.cos(minute_angle),
            self.y_pos + self.radius * 0.80 * math.sin(minute_angle),
        )

        second_pos = (
            self.x_pos + self.radius * 0.95 * math.cos(second_angle),
            self.y_pos + self.radius * 0.90 * math.sin(second_angle),
        )

        pygame.draw.line(display, (0, 0, 255), hour_pos, (self.x_pos, self.y_pos), int(0.03 * self.radius))

        pygame.draw.line(display, (0, 0, 255), minute_pos, (self.x_pos, self.y_pos), int(0.02 * self.radius))

        pygame.draw.line(display, (0, 0, 255), second_pos, (self.x_pos, self.y_pos), int(0.01 * self.radius))


if __name__ == "__main__":
    application = Application(WINDOW_WIDTH, WINDOOW_HEIGHT, FPS)
