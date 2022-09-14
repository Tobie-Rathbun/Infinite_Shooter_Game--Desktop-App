from random import gammavariate
from secrets import choice
import pygame as pg
from settings import *
import os
import sys
from collections import deque

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

img_dir = resource_path("resources/sprites/animated_sprites")
sprite_dir = resource_path("resources/sprites/static_sprites")

class SpriteObject:
    def __init__(self, game, pos=(5, 3.5), scale = 0.75, shift = 0.4):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(os.path.join(sprite_dir, "shroom.png")).convert()
        self.image.set_colorkey(WHITE)
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift

    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height))

        self.sprite_half_width = proj_width // 2
        height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 + height_shift

        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()

def get_image(sheet, frame, width, height):
        image = pg.Surface((width, height))
        image.set_colorkey(BLACK)
        image.blit(sheet, (0, 0), (frame * width, 0, width, height))
        return image

class AnimatedSprite(SpriteObject):
    def __init__(self, game, pos=(6, 4.5), scale=0.25, shift=0.4, animation_time=120):
        super().__init__(game, pos, scale, shift)
        self.animation_time = animation_time
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False

        self.spritesheet = pg.image.load(os.path.join(img_dir, "animated_torch.png")).convert()
        self.torch0 = get_image(self.spritesheet, 0, 32, 64)
        self.torch1 = get_image(self.spritesheet, 1, 32, 64)
        self.torch2 = get_image(self.spritesheet, 2, 32, 64)
        self.torch3 = get_image(self.spritesheet, 3, 32, 64)
        self.torch4 = get_image(self.spritesheet, 4, 32, 64)
        self.torch5 = get_image(self.spritesheet, 5, 32, 64)
        self.torch6 = get_image(self.spritesheet, 6, 32, 64)
        self.torch7 = get_image(self.spritesheet, 7, 32, 64)
        self.list = [self.torch0, self.torch1, self.torch2, self.torch3, self.torch4, self.torch5, self.torch6, self.torch7]
        self.images = self.get_images()

    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger:
            self.images.rotate(-1)
            self.image = self.images[0]

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    def get_images(self):
        images = deque()
        for item in self.list:
            images.append(item)
        return images
    