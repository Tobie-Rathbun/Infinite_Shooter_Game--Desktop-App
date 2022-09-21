from telnetlib import WONT
import pygame as pg
from settings import *
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

txt_dir = resource_path("resources/textures")
dig_dir = resource_path("resources/textures/digits")

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

        self.wall_textures = self.load_wall_textures()

        self.sky = pg.image.load(os.path.join(txt_dir, "sky.png"))
        self.sky_image = self.scale_texture(self.sky, (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0

        self.blood = pg.image.load(os.path.join(txt_dir, "blood_screen.png"))
        self.blood_screen = self.scale_texture(self.blood, RES)
        self.digit_size = 90
        self.all_digits = [pg.image.load(os.path.join(dig_dir, "{}.png".format(x))) for x in range(11)]
        self.digit_images = []
        for dig in self.all_digits:
            digit = self.scale_texture(dig, [self.digit_size] * 2)
            self.digit_images.append(digit)
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_img = pg.image.load(os.path.join(txt_dir, "game_over.png"))
        self.game_over_image = self.scale_texture(self.game_over_img, RES)

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, 0))
        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size, 0))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        #floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

        #loads the texture from the specified path and returns a scaled image
    @staticmethod
    def scale_texture(txtr, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = txtr
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.scale_texture(pg.image.load(os.path.join(txt_dir, "1.png"))),
            2: self.scale_texture(pg.image.load(os.path.join(txt_dir, "2.png"))),
            3: self.scale_texture(pg.image.load(os.path.join(txt_dir, "3.png"))),
            4: self.scale_texture(pg.image.load(os.path.join(txt_dir, "4.png"))),
            5: self.scale_texture(pg.image.load(os.path.join(txt_dir, "5.png"))),
        }
