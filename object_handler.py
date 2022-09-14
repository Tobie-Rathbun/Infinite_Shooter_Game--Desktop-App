from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = ''
        self.static_sprite_path = ''
        self.anim_sprite_path = ''
        add_sprite = self.add_sprite
        add_npc = self.add_npc

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game, pos=(2.99, 1.99)))
        add_sprite(AnimatedSprite(game, pos=(2.99, 3.5)))
        add_sprite(AnimatedSprite(game, pos=(2.99, 5.01)))
        add_sprite(AnimatedSprite(game, pos=(4.05, 3.05)))
        add_sprite(AnimatedSprite(game, pos=(4.01, 5.01)))
        #add_sprite(AnimatedSprite(game, pos=(6.5, 6.5)))
        
        #npc map
        add_npc(NPC(game))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self, npc):
        self.npc_list.append(npc)