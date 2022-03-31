import pygame
import random
from .globals import SIZE


class Apple:

    def __init__(self, surface):
        self.parent_screen = surface
        self.image = pygame.image.load('assets/apple4.png').convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 9) * SIZE
        self.y = random.randint(1, 9) * SIZE
