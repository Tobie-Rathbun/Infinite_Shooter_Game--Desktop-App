from sprite_object import *
from npc import *
from map_generator import *

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
        self.map_xs, self.map_ys = self.game.map_generator.map_x, self.game.map_generator.map_y
        #self.shroom_pos = (5, 4) # debug for shroom positioning
        self.shroom_pos = self.map_xs - 2, self.map_ys - 2

        #sprite map
            #shroom
        add_sprite(SpriteObject(game, pos=self.shroom_pos))

            #torches
        for x in range(self.map_xs - 1):
            add_sprite(AnimatedSprite(game, pos=(x + .05, 1.05)))
        for x in range(self.map_xs - 1):
            add_sprite(AnimatedSprite(game, pos=(x + .05, self.map_ys - 1.05)))

        for y in range(self.map_ys - 1):
            add_sprite(AnimatedSprite(game, pos=(1.05, y + .05)))
        for y in range(self.map_ys - 1):
            add_sprite(AnimatedSprite(game, pos=(self.map_xs - 1.05, y + .05)))

            #corners
        add_sprite(AnimatedSprite(game, pos=(self.map_xs - 1.05, self.map_ys - 1.05)))
        add_sprite(AnimatedSprite(game, pos=(self.map_xs - 1.05, 1.05)))
        add_sprite(AnimatedSprite(game, pos=(1.05, self.map_ys - 1.05)))
        add_sprite(AnimatedSprite(game, pos=(1.05, 1.05)))
        
        #add_sprite(AnimatedSprite(game, pos=(3.0, 1.05)))
        #add_sprite(AnimatedSprite(game, pos=(1.05, 3.0)))
        #add_sprite(AnimatedSprite(game, pos=(5, 1.05)))
        #add_sprite(AnimatedSprite(game, pos=(1.05, 5)))
        #add_sprite(AnimatedSprite(game, pos=(6.5, 6.5)))
        
        #npc map
        for i in range(int(self.map_xs / 5)):
            add_npc(CacoDemonNPC(game, pos=(int(self.map_xs - 2 - i), int(self.map_ys - 2))))

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