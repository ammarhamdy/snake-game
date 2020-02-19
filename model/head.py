import pygame
from pygame.sprite import Sprite
from . import setting
from .setting import speed_factor, surface_size, tile_size
from .color import white


class Head(Sprite):

    def __init__(self, surface, xy=(surface_size[0]//2, surface_size[1]//2)):
        super().__init__()
        self.surface = surface
        self.rect = pygame.Rect(xy, (tile_size, tile_size))
        self.direction = 1
        self.speed_factor = speed_factor
        # plash event.
        self.on_hit_event = None
        # direction,0: top, 1:right, 2: bottom, 3: left, (4, -1): stop
        self.go_to = (self.up, self.right, self.down, self.left)

    def play(self):
        pygame.draw.rect(self.surface, white, self.rect)
        self.go_to[self.direction]()

    def up(self):
        self.rect.y -= self.speed_factor
        if self.rect.y < setting.play_size[0]:
            self.on_hit_event()

    def right(self):
        self.rect.x += self.speed_factor
        if self.rect.right > setting.play_size[1]:
            self.on_hit_event()

    def down(self):
        self.rect.y += self.speed_factor
        if self.rect.bottom > setting.play_size[2]:
            self.on_hit_event()

    def left(self):
        self.rect.x -= self.speed_factor
        if self.rect.x < setting.play_size[3]:
            self.on_hit_event()
