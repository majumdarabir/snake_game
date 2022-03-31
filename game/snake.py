import pygame


class Snake:
    def __init__(self, surface, length):
        self.parent_screen = surface
        pygame.display.set_caption("@created by Abir!")
        self.block = pygame.image.load('resources/block4.png').convert()
        self.length = length
        self.x = [40]*length
        self.y = [40]*length
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == 'left':
            self.x[0] -= 40
        elif self.direction == 'right':
            self.x[0] += 40
        elif self.direction == 'up':
            self.y[0] -= 40
        elif self.direction == 'down':
            self.y[0] += 40
        self.draw()

    def draw(self):
        self.image = pygame.image.load('resources/background6.jpg').convert()
        self.parent_screen.blit(self.image, (0, 0))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()
