import pygame as pg
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

snd_dir = resource_path("resources/sound")

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.shotgun = pg.mixer.Sound(os.path.join(snd_dir, "shotgun.wav"))
        self.npc_pain = pg.mixer.Sound(os.path.join(snd_dir, "npc_pain.wav"))
        self.npc_death = pg.mixer.Sound(os.path.join(snd_dir, "npc_death.wav"))
        self.npc_shot = pg.mixer.Sound(os.path.join(snd_dir, "npc_attack.wav"))
        self.player_pain = pg.mixer.Sound(os.path.join(snd_dir, "player_pain.wav"))
        self.theme = pg.mixer.Sound(os.path.join(snd_dir, "theme.mp3"))
        