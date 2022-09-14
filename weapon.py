from sprite_object import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

wpn_dir = resource_path("resources/sprites/weapon/shotgun")



class Weapon(AnimatedSprite):
    def __init__(self, game, scale=0.9, shift=0.6, animation_time=120):
        super().__init__(game=game, scale=scale, shift=shift, animation_time=animation_time)
            #loads other classes init and runs
        self.gun0 = pg.image.load(os.path.join(wpn_dir, "0.png"))
        print(self.gun0.get_at((0,0)))
        self.gun0.set_colorkey(WHITE)
        self.gun1 = pg.image.load(os.path.join(wpn_dir, "1.png"))
        self.gun1.set_colorkey(WHITE)
        self.gun2 = pg.image.load(os.path.join(wpn_dir, "2.png"))
        self.gun2.set_colorkey(WHITE)
        self.gun3 = pg.image.load(os.path.join(wpn_dir, "3.png"))
        self.gun3.set_colorkey(WHITE)
        self.gun4 = pg.image.load(os.path.join(wpn_dir, "4.png"))
        self.gun4.set_colorkey(WHITE)
        self.gun5 = pg.image.load(os.path.join(wpn_dir, "5.png"))
        self.gun5.set_colorkey(WHITE)
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

        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 50

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)


    def update(self):
        self.check_animation_time()
        self.animate_shot()