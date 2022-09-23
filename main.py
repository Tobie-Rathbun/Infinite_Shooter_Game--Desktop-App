# imports
import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

#game constructor class
class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((RES), pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event =  pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 80)
        self.new_game()

    def new_game(self):
        self.map_generator = MapGenerator(self)
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        #self.static_sprite = SpriteObject(self)
        #self.animated_sprite = AnimatedSprite(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self, self.map.mini_map)

    def update(self):
        self.map_generator.update()
        self.map.update()
        self.player.update()
        self.raycasting.update()
        #self.static_sprite.update()
        #self.animated_sprite.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def new_map(self, round):
        self.map_generator.increase_map_size(round)
        self.map_generator.update()
        self.map.update()
        self.pathfinding = PathFinding(self, self.map.mini_map)
        self.object_handler = ObjectHandler(self)

    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()
            #3D Draw Set
        #self.screen.fill(BLACK)
        #self.map.draw()
        #self.player.draw()
            #2D Draw Set (Debug)

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        self.game_running = True
        while self.game_running:
            self.check_events()
            self.update()
            self.draw()

    def pre_game(self):
        self.game_running = False
        self.new_game()
        self.basicFont = pg.font.SysFont(None, 48)
        self.screen.fill(BLACK)
        self.text = self.basicFont.render("WSAD to walk, click to shoot!", True, WHITE)
        self.text2 = self.basicFont.render("Get to the mushroom to make it to the next round", True, WHITE)
        self.text3 = self.basicFont.render("Press SPACE to play!", True, WHITE)
        self.textRect, self.textRect2, self.textRect3 = self.text.get_rect(), self.text2.get_rect(), self.text3.get_rect()
        self.textRect.centerx, self.textRect2.centerx, self.textRect3.centerx = self.screen.get_rect().centerx, self.screen.get_rect().centerx, self.screen.get_rect().centerx
        self.textRect.centery, self.textRect2.centery, self.textRect3.centery = self.screen.get_rect().centery / 3, self.screen.get_rect().centery / 2, self.screen.get_rect().centery / 1.5 
        self.pregame = True
        while self.pregame:
            self.screen.blit(self.text,self.textRect)
            self.screen.blit(self.text2,self.textRect2)
            self.screen.blit(self.text3,self.textRect3)
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.run()
            pg.display.flip()

    def post_game(self):
        self.game_running = False
        self.screen.fill(BLACK)
        self.text = self.basicFont.render("You made it to round: ", True, WHITE)
        self.text2 = self.basicFont.render(str(self.player.round_number), True, WHITE)
        self.text3 = self.basicFont.render("Press SPACE to play!", True, WHITE)
        self.textRect, self.textRect2, self.textRect3 = self.text.get_rect(), self.text2.get_rect(), self.text3.get_rect()
        self.textRect.centerx, self.textRect2.centerx, self.textRect3.centerx = self.screen.get_rect().centerx, self.screen.get_rect().centerx, self.screen.get_rect().centerx
        self.textRect.centery, self.textRect2.centery, self.textRect3.centery = self.screen.get_rect().centery / 3, self.screen.get_rect().centery / 2, self.screen.get_rect().centery / 1.5 
        self.pregame = True
        while self.pregame:
            self.screen.blit(self.text,self.textRect)
            self.screen.blit(self.text2,self.textRect2)
            self.screen.blit(self.text3,self.textRect3)
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.pre_game()
            pg.display.flip()

if __name__ == '__main__':
    game = Game()
    game.pre_game()