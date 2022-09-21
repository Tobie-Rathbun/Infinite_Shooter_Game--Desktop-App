from settings import *
import pygame as pg
import math
from object_handler import *
from map_generator import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False
        self.health = PLAYER_MAX_HEALTH
        self.round_number = STARTING_ROUND
        self.rel = 0
        self.health_recovery_delay = 700
        self.time_prev = pg.time.get_ticks()
        self.progress_lvl = False

    def recover_health(self):
        if self.check_health_recovery_delay() and self.health < PLAYER_MAX_HEALTH:
            self.health += 1

    def check_health_recovery_delay(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True

    def check_game_over(self):
        if self.health < 1:
            self.game.object_renderer.game_over()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def get_damage(self, damage):
        self.health -= damage
        self.game.object_renderer.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over()

    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED *self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)
        self.check_shroom_collision()

        #if keys[pg.K_LEFT]:
        #    self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        #if keys[pg.K_RIGHT]:
        #    self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau #tau is 2*pi

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def next_round(self):
        if self.progress_lvl:
            self.progress_lvl = False
            self.x, self.y = PLAYER_POS
            self.round_number += 1
            self.game.new_map(self.round_number)
            self.angle = PLAYER_ANGLE

    def check_shroom(self, x, y):
        self.shroom_x, self.shroom_y = self.game.object_handler.shroom_pos
        diff_x = abs(x - self.shroom_x)
        diff_y = abs(y - self.shroom_y)
        #print(diff_x, diff_y) #debug
        if diff_x < 1.15 and diff_y  < 1.15:
            #print('shroom!')
            #success screen, next level
            self.progress_lvl = True
            #return (x, y)        

    def check_shroom_collision(self):
        self.check_shroom(int(self.x), int(self.y))
        

    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.x *100, self.y * 100),
                    (self.x * 100 + WIDTH * math.cos(self.angle),
                    self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()
        self.recover_health()
        self.next_round()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)