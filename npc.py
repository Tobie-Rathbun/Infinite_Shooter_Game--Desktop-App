from sprite_object import *
from random import randint, random, choice

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

sol_dir = resource_path("resources/sprites/npc/soldier")
att_dir = resource_path("resources/sprites/npc/soldier/attack")
att_dir = resource_path("resources/sprites/npc/soldier/death")
att_dir = resource_path("resources/sprites/npc/soldier/idle")
att_dir = resource_path("resources/sprites/npc/soldier/pain")
att_dir = resource_path("resources/sprites/npc/soldier/walk")

class NPC(AnimatedSprite):
    def __init__(self, game, pos=(6,3.5), scale=.66, shift=0.4, animation_time=120):
        super().__init__(game, pos, scale, shift, animation_time)
        self.image = pg.image.load(os.path.join(sol_dir, "0.png"))
        #2 attack, 9 death, 8 idle, 1 pain, 4 walk
        #self.attack_images = []

        self.attack_dist = randint(3, 6)
        self.speed = 0.03
        self.size = 10
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.15
        self.alive = True
        self.pain = False
    
    def update(self):
        self.check_animation_time()
        self.get_sprite()
