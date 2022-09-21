import pygame as pg
from collections import deque
from map_generator import *





_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, _, 2, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, _, 3, _, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, _, 2, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, _, 3, _, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, _, 2, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, _, 3, _, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5],
    [1, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, 1],
    [1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = self.game.map_generator.generate_map()
        print(self.mini_map)
        #self.dq = deque()
        #self.portal = [2, 3, 4, 5]
        #for num in self.portal:
        #    self.dq.append(num)
        #self.f = self.dq[0]
        self.world_map = {}
        self.get_map()
        

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    #if value == 5:
                    #    self.world_map[(i, j)] = self.f
                    self.world_map[(i, j)] = value

    def update(self):
        self.mini_map = self.game.map_generator.generate_map()
        self.world_map = {}
        self.get_map()

    def draw(self):
        #self.dq.rotate(-1)
        #self.f = self.dq[0]
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
        for pos in self.world_map]



