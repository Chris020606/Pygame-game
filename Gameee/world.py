
import pygame
import random
from settings import *

class Three(pygame.sprite.Sprite):
    def __init__(self, surf, pos, group):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_frect(center= pos )

class World(pygame.sprite.Sprite):
    def __init__(self, surf, group):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_frect(center = (random.randint(0, WIDTH), random.randint(0, HEIGHT)))


    def create_world(self):
        pass

class Rocks(World):
    pass

class River(World):
    pass