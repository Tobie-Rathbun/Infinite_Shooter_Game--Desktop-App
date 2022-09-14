from sprite_object import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

wpn_dir = resource_path("resources/sprites/weapon/shotgun")



class Weapon(AnimatedSprite):
    def __init__(self, game, scale=1, shift=0.4, animation_time=120):
        super().__init__(game=game, scale=scale, shift=shift, animation_time=animation_time)
            #loads other classes init and runs
        self.gun0 = pg.image.load(os.path.join(wpn_dir, "0.png"))
        print(self.gun0.get_at((0,0)))
        self.gun0.set_colorkey(WHITE)
        self.gun1 = pg.image.load(os.path.join(wpn_dir, "1.png")).convert()
        self.gun2 = pg.image.load(os.path.join(wpn_dir, "2.png")).convert()
        self.gun3 = pg.image.load(os.path.join(wpn_dir, "3.png")).convert()
        self.gun4 = pg.image.load(os.path.join(wpn_dir, "4.png")).convert()
        self.gun5 = pg.image.load(os.path.join(wpn_dir, "5.png")).convert()
            #loads images for shotgun
        self.list = [self.gun0, self.gun1, self.gun2, self.gun3, self.gun4, self.gun5]
            #list of all shotgun images
        self.images = self.get_images()
            #switches torches with shotgun
        
            
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
            for img in self.images])
            #scales shotgun image?
        
        

        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)


    def update(self):
        pass