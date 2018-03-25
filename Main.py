import pygame
from Population import Population
from Target import Target
from Obstacle import Obstacle

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
# Set game name
pygame.display.set_caption("Smart Rockets")

surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((0, 0, 0))
clock = pygame.time.Clock()

pygame.key.set_repeat(1, 250)
screen.blit(surface, (0, 0))

target = Target(SCREEN_WIDTH/2-32, 100)
obstacle = Obstacle(440, SCREEN_HEIGHT/2, 400, 20)
lifeSpan = 400

if __name__ == '__main__':

    population = Population(SCREEN_WIDTH/2, SCREEN_HEIGHT, lifeSpan)
    count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((0, 0, 0))
        target.show(screen)
        obstacle.show(screen)
        population.run(screen, count, target, obstacle)

        count += 1
        if count == lifeSpan:
            population.evaluate(target)
            population.selection()
            #population = Population(SCREEN_WIDTH/2, SCREEN_HEIGHT, lifeSpan)
            count = 0

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)