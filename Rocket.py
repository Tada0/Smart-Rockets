import pygame
import math
from DNA import DNA
from Vector import Vector, get_random_unit_vector


class Rocket:
    def __init__(self, x, y, lifespan, dna):
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.image = pygame.image.load('images/rocket.png')
        if dna is not None:
            self.dna = dna
        else:
            self.dna = DNA(lifespan, None)
        self.fitness = 0
        self.completed = False
        self.crashed = False

    def apply_force(self, force):
        self.acceleration.add(force)

    def update(self, count, target, obstacle):

        d = math.sqrt(math.fabs(self.position.x - target.position.x + 32) + math.fabs(self.position.y - target.position.y + 32))
        if d < 5:
            self.completed = True

        if obstacle.rect.collidepoint((self.position.x, self.position.y)):
            self.crashed = True

        if self.position.x == 0 or self.position.x == 1280:
            self.crashed = True

        self.apply_force(self.dna.genes[count])

        if not self.completed and not self.crashed:
            self.velocity.add(self.acceleration)
            self.position.add(self.velocity)
            self.acceleration.multiply(0)

    def show(self, screen):
        rocket = pygame.transform.rotate(self.image, self.velocity.heading())
        screen.blit(rocket, (self.position.x - 32, self.position.y))

    def calculate_fitness(self, target):
        d = math.sqrt(math.fabs(self.position.x - target.position.x) + math.fabs(self.position.y - target.position.y))
        self.fitness = 1 / d

        if self.completed:
            self.fitness *= 10

        if self.crashed:
            self.fitness = 0
