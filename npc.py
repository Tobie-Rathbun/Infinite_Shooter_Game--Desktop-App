from sprite_object import *
from random import randint, random, choice

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

sol_dir = resource_path("resources/sprites/npc/soldier")
att_dir = resource_path("resources/sprites/npc/soldier/attack")
dth_dir = resource_path("resources/sprites/npc/soldier/death")
idle_dir = resource_path("resources/sprites/npc/soldier/idle")
pain_dir = resource_path("resources/sprites/npc/soldier/pain")
walk_dir = resource_path("resources/sprites/npc/soldier/walk")

class NPC(AnimatedSprite):
    def __init__(self, game, pos=(6,3.5), scale=.66, shift=0.4, animation_time=420):
        super().__init__(game, pos, scale, shift, animation_time)
        self.image = pg.image.load(os.path.join(sol_dir, "0.png"))
        #2 attack, 9 death, 8 idle, 1 pain, 4 walk
        #self.attack_images = []
        self.list = []
        for x in range(8):
            idle_img = pg.image.load(os.path.join(idle_dir, "{}.png".format(x)))
            self.list.append(idle_img)
        self.idle_images = self.get_images()
        self.list = [pg.image.load(os.path.join(pain_dir, "0.png"))]
        self.pain_images = self.get_images()
        self.list = []
        for x in range(9):
            dth_img = pg.image.load(os.path.join(dth_dir, "{}.png".format(x)))
            self.list.append(dth_img)
        self.pain_images = self.get_images()


        self.attack_dist = randint(3, 6)
        self.speed = 0.03
        self.size = 10
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.15
        self.alive = True
        self.pain = False
        self.ray_cast_value = False
        self.frame_counter = 0
    
    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()
        #self.draw_ray_cast()

    def animate_death(self):
        if not self.alive:
            if self.animation_trigger and self.frame_counter < len(self.death_images) - 1:
                self.death_images.rotate(-1)
                self.image = self.death_images[0]
                self.frame_counter += 1

    def animate_pain(self):
        self.animate(self.pain_images)
        if self.animation_trigger:
            self.pain = False


    def check_hit_in_npc(self):
        if self.ray_cast_value and self.game.player.shot:
            if HALF_WIDTH - self.sprite_half_width < self.screen_x < HALF_WIDTH + self.sprite_half_width:
                self.game.sound.npc_pain.play()
                self.game.player.shot = False
                self.pain = True
                self.health -= self.game.weapon.damage
                self.check_health()

    def check_health(self):
        if self.health < 1:
            self.alive = False
            self.game.sound.npc_death.play()

    def run_logic(self):
        if self.alive:
            self.ray_cast_value = self.ray_cast_player_npc()
            self.check_hit_in_npc()
            if self.pain:
                self.animate_pain()
            else:    
                self.animate(self.idle_images)
        else:
            self.animate_death()

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    def ray_cast_player_npc(self):
        if self.game.player.map_pos == self.map_pos:
            return True

        wall_dist_v, wall_dist_h = 0, 0
        player_dist_v, player_dist_h = 0, 0

        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos


        ray_angle = self.theta
       
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        #horizontal lines across the screen to calculate ray points
        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a

        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        for i in range(MAX_DEPTH):
            tile_hor = int(x_hor), int(y_hor)
            if tile_hor == self.map_pos:
                player_dist_h = depth_hor
                break
            if tile_hor in self.game.map.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

            

            #vertical lines
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert == self.map_pos:
                    player_dist_v = depth_vert
                    break
                if tile_vert in self.game.map.world_map:
                    wall_dist_v = depth_vert
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False

    def draw_ray_cast(self):
        pg.draw.circle(self.game.screen, 'red', (100 * self.x, 100 * self.y), 15)
        if self.ray_cast_player_npc():
            pg.draw.line(self.game.screen, 'orange', (100 * self.game.player.x, 100 * self.game.player.y),
                            (100 * self.x, 100 * self.y), 2)