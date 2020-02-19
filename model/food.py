import pygame
from pygame.sprite import Sprite
from random import randint
from . import setting
from . import color
from .setting import tile_size, tile_region, food_speed_factor, play_size, update_play_size, max_num_border


class Food(Sprite):

    def __init__(self, surface, s_head):
        super().__init__()
        self.surface = surface
        self.rect = pygame.Rect(
            randint(play_size[-1], play_size[1] - tile_size),
            randint(play_size[0], play_size[2] - tile_size),
            tile_size, tile_size
        )
        self.s_head = s_head
        self.fixed_counter = 0
        self.on_collide_event = None
        self.check_collision = self.check_collision_e
        self.go_to = (self.up, self.right, self.down, self.left)

    def draw(self):
        """draw the rect."""
        pygame.draw.rect(self.surface, color.current, self.rect)
        pygame.draw.line(self.surface, color.black,
                         (self.s_head.rect.x, self.s_head.rect.y),
                         (self.rect.x, self.rect.y))

    def new(self):
        # update color, play size.
        color.update()
        self.rect.x = randint(setting.play_size[-1], setting.play_size[1] - tile_size)
        self.rect.y = randint(setting.play_size[0], setting.play_size[2] - tile_size)
        update_play_size(self.fixed_counter)
        self.fixed_counter += 1
        if self.fixed_counter == max_num_border:
            self.new = self.new1

    def new1(self):
        # update color, play size.
        color.update()
        self.rect.x = randint(setting.play_size[-1], setting.play_size[1] - tile_size)
        self.rect.y = randint(setting.play_size[0], setting.play_size[2] - tile_size)

    def run_away(self):
        """snake direction +2 = ~direction (negation of  direction)"""
        self.direction = ((self.s_head.direction + 2) % 4 + randint(1, 3)) % 4
        for i in range(20):
            self.go_to[self.direction]()

    def check_collision_e(self):
        if abs(self.s_head.rect.centerx - self.rect.centerx) < tile_size \
                and \
                abs(self.s_head.rect.centery - self.rect.centery) < tile_size:
            self.on_collide_event()
            self.new()
            if randint(0, 5) % 5:
                self.check_collision = self.except_collision_e

    def except_collision_e(self):
        if abs(self.s_head.rect.centerx - self.rect.centerx) < tile_region \
                and \
                abs(self.s_head.rect.centery - self.rect.centery) < tile_region:
            self.run_away()
            if randint(0, 3) % 3:
                self.check_collision = self.check_collision_e

    def up(self):
        if self.rect.y < setting.play_size[0]:
            # self.direction = randint(1, 3)
            return
        self.rect.y -= food_speed_factor

    def right(self):
        if self.rect.right > setting.play_size[1]:
            # self.direction = randint(2, 4) % 4
            return
        self.rect.x += food_speed_factor

    def down(self):
        if self.rect.bottom > setting.play_size[2]:
            # self.direction = randint(3, 5) % 4
            return
        self.rect.y += food_speed_factor

    def left(self):
        if self.rect.x < setting.play_size[3]:
            # self.direction = randint(0, 2)
            return
        self.rect.x -= food_speed_factor
