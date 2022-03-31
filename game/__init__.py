import pygame
from .wallpaper import Wallpaper
from .apple import Apple
from .snake import Snake
from .globals import SIZE
import time


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface = pygame.display.set_mode((400, 400))
        self.wallpaper = Wallpaper(self.surface)
        self.image = pygame.image.load('./assets/coverpage.jpg').convert()
        self.surface.blit(self.image, (0, 0))

        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def restart(self):

        self.snake = Snake(self.surface, 1)

        self.apple = Apple(self.surface)

    def score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"score:{self.snake.length}", True, (255, 0, 0))
        self.surface.blit(score, (300, 10))

    def show_gameover(self):
        self.surface.blit(self.image, (0, 0))
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(
            f'Game is over,Your score:{self.snake.length}', True, (200, 200, 200))
        self.surface.blit(line1, (50, 100))
        font = pygame.font.SysFont('arial', 30)
        line2 = font.render('press Enter to play again', True, (200, 200, 200))
        self.surface.blit(line2, (50, 150))

        pygame.display.flip()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2+SIZE:
            if y1 >= y2 and y1 < y2+SIZE:
                return True

        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        # snake collition with Apple

        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.apple.x, self.apple.y):

                self.snake.increase_length()
                self.apple.move()

        if not ((0 <= self.snake.x[0] <= 399) and (0 <= self.snake.y[0] <= 399)):
            raise "hit the wall game over"
        self.score()
        pygame.display.flip()

        # snake collision with itself
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "GAME OVER"

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RETURN:
                        pause = False
                        self.restart()
                    if not pause:
                        if event.key == pygame.K_RIGHT:

                            self.snake.move_right()
                        elif event.key == pygame.K_LEFT:

                            self.snake.move_left()
                        elif event.key == pygame.K_UP:

                            self.snake.move_up()
                        elif event.key == pygame.K_DOWN:

                            self.snake.move_down()

                if event.type == pygame.QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_gameover()
                pause = True

            time.sleep(0.1)
