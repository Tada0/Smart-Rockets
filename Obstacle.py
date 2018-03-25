import pygame

class Obstacle:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def show(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)