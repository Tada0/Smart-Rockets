import random
from Rocket import Rocket


class Population:
    def __init__(self, x, y, lifespan, size):
        self.rockets = []
        self.size = size
        self.start_x = x
        self.start_y = y
        self.mating_pool = []
        self.lifespan = lifespan

        for rocket in range(self.size):
            self.rockets.append(Rocket(self.start_x, self.start_y, lifespan, None))

    def run(self, screen, count, target, obstacle):
        for rocket in self.rockets:
            rocket.update(count, target, obstacle)
            rocket.show(screen)

    def evaluate(self, target):

        max_fitness = 0

        for rocket in self.rockets:
            rocket.calculate_fitness(target)
            if rocket.fitness > max_fitness:
                max_fitness = rocket.fitness

        for rocket in self.rockets:
            rocket.fitness /= max_fitness

        self.mating_pool = []

        for rocket in self.rockets:
            n = int(rocket.fitness * 100)
            for j in range(n):
                self.mating_pool.append(rocket)

    def selection(self):

        new_rockets = []
        i = 0
        for rocket in self.rockets:
            dad = self.mating_pool[random.randint(0, len(self.mating_pool) - 1)].dna
            mom = self.mating_pool[random.randint(0, len(self.mating_pool) - 1)].dna
            child = dad.crossover(mom, self.lifespan)
            child.mutation()
            new_rockets.append(Rocket(self.start_x, self.start_y, self.lifespan, child))

        self.rockets = new_rockets