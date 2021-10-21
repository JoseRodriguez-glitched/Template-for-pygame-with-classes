import pygame, json
from pygame.locals import *
from player import Player
from level import Level

pygame.init()
class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode([600, 400], 0, 32)
        pygame.display.set_caption("Prueba")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.level = Level()
    def update(self):
        self.clock.tick(60)
        pygame.display.update()
        self.player.update()
    def draw(self):
        while done := not False:
            for ev in pygame.event.get():
                self.player.move(event=ev)
                if ev.type == QUIT:
                    pygame.quit()
                    done = True
                elif ev.type == KEYDOWN:
                    if ev.key == K_ESCAPE:
                        pygame.quit()
                        done = True
            self.screen.fill([60,60,60])
            self.level.draw(self.screen)
            self.player.draw(self.screen)
            self.update()

if __name__ == "__main__":
    game = Game()
    game.draw()