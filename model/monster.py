import pygame
from pygame.sprite import Sprite
from random import randint
from . import setting
from .color import red
from .setting import tile_size, monster_speed_factor, play_size
# from os import urandom


class Monster(Sprite):

    def __init__(self, surface, s_head):
        super().__init__()
        self.surface = surface
        self.rect = pygame.Rect(
            randint(play_size[-1], play_size[1] - tile_size),
            randint(play_size[0], play_size[2] - tile_size),
            tile_size, tile_size)
        self.s_head = s_head
        self.go_to = (self.up, self.right, self.down, self.left)

    def play(self):
        """draw the rect."""
        pygame.draw.rect(self.surface, red, self.rect)
        self.trace()

    def trace(self):
        if self.s_head.direction % 2:
            x = self.rect.x > self.s_head.rect.x
            self.go_to[3 * x + (not x)]()
        else:
            self.go_to[(self.rect.y < self.s_head.rect.y) * 2]()

    def hard_trace(self):
        x = self.rect.x > self.s_head.rect.x
        self.go_to[3 * x + (not x)]()
        self.go_to[(self.rect.y < self.s_head.rect.y) * 2]()
        # if self.rect.x > self.s_head.rect.x:
        #     self.go_to[3]()
        # else:
        #     self.go_to[1]()
        # if self.rect.y > self.s_head.rect.y:
        #     self.go_to[0]()
        # else:
        #     self.go_to[2]()

    def up(self):
        if self.rect.y > setting.play_size[0]:
            self.rect.y -= monster_speed_factor

    def right(self):
        if self.rect.right < setting.play_size[1]:
            self.rect.x += monster_speed_factor

    def down(self):
        if self.rect.bottom < setting.play_size[2]:
            self.rect.y += monster_speed_factor

    def left(self):
        if self.rect.x > setting.play_size[3]:
            self.rect.x -= monster_speed_factor

# self.go_to[int.from_bytes(urandom(1), 'little') >> 6]()
