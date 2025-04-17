import pygame
from player import *
from enemies import *
from world import *

# Learn to create a class for sprite and animated sprites this should add complicity and organization to the code


class Game:
    def __init__(self):
        # sprites
        self.all_sprite = pygame.sprite.Group()

        # player
        self.player = Player(self.all_sprite)

        # Add enemies at random and a specific time of the day
        self.enemies = []
         # Maybe create all this in a class World that make all of this when you have a word

        # Items
        self.items = []


    def update(self):
        pass

    def craft(self):
        pass

    def game_over(self):
        pass

    def reset(self):
        pass

