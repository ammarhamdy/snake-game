import pygame
from pygame.sprite import Sprite
from .setting import tile_size
from . import color
from .color import black


class Tile(Sprite):

    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.color = color.current
        self.rect = pygame.Rect((-10, -10), (tile_size, tile_size))

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
