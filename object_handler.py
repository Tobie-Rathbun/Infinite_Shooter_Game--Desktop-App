from sprite_object import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = ''
        self.anim_sprite_path = ''
        add_sprite = self.add_sprite

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(2.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(3.5, 3.5)))
        add_sprite(AnimatedSprite(game, pos=(4.5, 4.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(6.5, 6.5)))
        

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)