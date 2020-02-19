import pygame
import pygame.display as window
from pygame import KEYDOWN, QUIT, K_UP, K_RIGHT, K_DOWN, K_LEFT, K_LSHIFT, K_SPACE, K_q
from sys import exit
from model.eventHandler import EventHandler
from model.snake import Snake
from model.food import Food
from model.monster import Monster
from model.setting import surface_size, stroke_width, borders_position, max_num_border
from model.color import white, black, current_palette as cp


class SnakeGame:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.main_clock = pygame.time.Clock()
        window.set_caption('snake game')
        self.surface = window.set_mode(surface_size)
        self.snake = Snake(self.surface)
        self.food = Food(self.surface, self.snake.head)
        self.monster = Monster(self.surface, self.snake.head)
        self.food.on_collide_event = self.snake.grow_up
        self.eventHandler = EventHandler(pygame.KEYDOWN)
        self.add_events()

    def add_events(self):
        # exit.
        self.eventHandler.add_event(QUIT, lambda event: exit(0))
        self.eventHandler.add_subevent(KEYDOWN, K_q, exit)
        # movement.
        self.eventHandler.add_subevent(KEYDOWN, K_UP, self.snake.go_up)
        self.eventHandler.add_subevent(KEYDOWN, K_RIGHT, self.snake.go_right)
        self.eventHandler.add_subevent(KEYDOWN, K_DOWN, self.snake.go_down)
        self.eventHandler.add_subevent(KEYDOWN, K_LEFT, self.snake.go_left)
        self.eventHandler.add_subevent(KEYDOWN, K_LSHIFT, self.snake.speed_up)
        self.eventHandler.add_subevent(KEYDOWN, K_SPACE, self.snake.shrink)
        # self.eventHandler.add_subevent(KEYDOWN, pygame.K_a, self.snake.grow_down_head)

    def update_screen(self):
        self.surface.fill(white)
        pygame.draw.rect(self.surface, black, (0, 0, surface_size[0], surface_size[1]), stroke_width)
        # draw borders.
        self.food.draw()
        self.snake.play()
        self.monster.play()
        self.food.check_collision()
        for i in range(self.food.fixed_counter):
            pygame.draw.rect(self.surface, cp[i % 4], borders_position[i], stroke_width)
        pygame.display.flip()

    def start(self):
        while True:
            self.eventHandler.check_events()
            self.update_screen()
            self.main_clock.tick(50)
