from collections import deque
from pygame import draw
from .tile import Tile
from .head import Head
from .color import black


class Snake:
    def __init__(self, surface):
        self.surface = surface
        self.head = Head(self.surface)
        self.body = deque()
        self.on_die_event = lambda: None
        self.is_speed_up = True
        self.head.on_hit_event = self.grow_down_head
        # add first tile after the head.
        self.grow_up()

    def play(self):
        self.head.play()
        self.play_body()

    def speed_up(self):
        self.head.speed_factor += 5
        for i in range(len(self.body) // 2):
            self.head.play()
            self.play_body()
        self.head.speed_factor -= 5

    def shrink(self):
        self.head.play()
        for i in range(len(self.body) // 2):
            self.play_body()

    def play_body(self):
        length = len(self.body)
        # from tail to the head each tile follow the next of it.
        for i in range(1, length):
            self.body[length - i].draw()
            self.body[length - i].rect.x = self.body[length - i - 1].rect.x
            self.body[length - i].rect.y = self.body[length - i - 1].rect.y
        self.body[0].draw()
        self.body[0].rect.x = self.head.rect.x
        self.body[0].rect.y = self.head.rect.y

    def go_up(self):
        self.head.direction = 0

    def go_right(self):
        self.head.direction = 1

    def go_down(self):
        self.head.direction = 2

    def go_left(self):
        self.head.direction = 3

    def grow_up(self):
        self.body.append(Tile(self.surface))

    def grow_down_tail(self):
        """kill the tail"""
        self.body.pop()
        if not self.body:
            self.play_body = lambda: None
            self.play = self.on_die_event

    def grow_down_head(self):
        """kill the head"""
        self.body.popleft()
        if not self.body:
            self.play_body = lambda: None
            self.play = self.on_die_event
