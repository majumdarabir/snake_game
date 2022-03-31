import pygame
import time
import os


class Wallpaper:

    def __init__(self, surface):

        self.surface = surface
        self.pic = pygame.image.load('./assets/coverpage.jpg').convert()
        self.surface.blit(self.pic, (0, 0))

        pygame.display.flip()
        time.sleep(0.5)
