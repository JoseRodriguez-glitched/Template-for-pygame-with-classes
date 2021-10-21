import pygame as pg
from pygame.locals import *

class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pg.Surface([30,50])
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.center = (300,200)
        self.moving = {
            "right": False,
            "left": False,
            "up": False,
            "down": False,
        }
    def update(self):
        if self.moving["right"]:
            self.rect.x += 5
        if self.moving["left"]:
            self.rect.x -= 5
    def move(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.moving["right"] = True
            elif event.key == K_LEFT:
                self.moving["left"] = True
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                self.moving["right"] = False
            elif event.key == K_LEFT:
                self.moving["left"] = False
    def draw(self, display):
        display.blit(self.image, self.rect)