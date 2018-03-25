import pygame
from Vector import Vector

class Target:
    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.image = pygame.image.load('images/target.png')

    def show(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))
