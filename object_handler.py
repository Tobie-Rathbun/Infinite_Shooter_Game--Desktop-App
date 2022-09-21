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
        self.npc_positions = {}

        #sprite map
        self.shroom_pos = (5, 4)
        add_sprite(SpriteObject(game, pos=self.shroom_pos))
        add_sprite(AnimatedSprite(game, pos=(2.99, 1.99)))
        add_sprite(AnimatedSprite(game, pos=(2.99, 3.5)))
        add_sprite(AnimatedSprite(game, pos=(2.99, 5.01)))
        add_sprite(AnimatedSprite(game, pos=(4.05, 3.05)))
        add_sprite(AnimatedSprite(game, pos=(4.01, 5.01)))
        #add_sprite(AnimatedSprite(game, pos=(6.5, 6.5)))
        
        #npc map
        #add_npc(NPC(game, pos=(6, 3.5)))
        #add_npc(NPC(game, pos=(11.5, 4.5)))
        #add_npc(CyberDemonNPC(game, pos=(8, 3.5)))
        #add_npc(CacoDemonNPC(game, pos=(9, 3.5)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self, npc):
        self.npc_list.append(npc)