import pygame as pg

def load_map(path):
    f = open(path+".txt","r")
    data = f.read()
    f.close()
    data = data.split("\n")
    mapa = []
    for row in data:
        mapa.append(list(row))
    return mapa

class Level():
    def __init__(self) -> None:
        self.map = load_map("level")
    def draw(self,display):
        y = 0
        for layer in self.map:
            x = 0
            for tile in layer:
                if tile == '1':
                    pg.draw.rect(display,(255,255,255),(x*32,y*32,32,32))
                x += 1
            y += 1