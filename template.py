import pygame
from pygame.locals import *

pygame.init()
class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode([600, 400], 0, 32)
        pygame.display.set_caption('Plantilla de juego')
        self.clock = pygame.time.Clock()
    def update(self):
        self.clock.tick(60)
        pygame.display.update()
    def draw(self):
        while done := not False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    done = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        done = True
            self.screen.fill([60,60,60])
            self.update()

if __name__ == "__main__":
    game = Game()
    game.draw()
