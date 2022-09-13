from random import gammavariate
import pygame as pg
from settings import *

class SpriteObject:
    def __init__(self, game, path='resources/sprites/static_sprites/shroom.png', pos=(10.5, 3.5)):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha().set_colorkey(WHITE)
        self.IMAGE_WIDTH = self.image.get_width()

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

    def update(self):
        self.get_sprite()