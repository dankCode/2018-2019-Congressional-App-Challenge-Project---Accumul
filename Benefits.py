

from random import randint
import pygame
from pygame.sprite import Sprite


class Benefits(Sprite):

    def __init__(self, screen, start_pos_x, start_pos_y):
        super(Benefits, self).__init__()
        self.ben_width = 22
        self.ben_height = 22
        self.screen = screen
        self.max_gen_value = 255
        self.min_gen_value = 60
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y

        # The 3 values to be determined by a number generator for the remaining variables underneath.
        # the purpose of this is so that functions from the 'random' library will not be called on repeatedly,
        # to save performance
        self.factors = [randint(self.min_gen_value, self.max_gen_value) for i in range(3)]

        self.benefit_move_rate_y = float(self.factors[1]/51.0)
        self.color = (self.factors[0], self.factors[1], self.factors[2])
        self.hit_points = (self.factors[0] + self.factors[1] + self.factors[2])/85  # dependent on the color chosen

        self.rect = pygame.Rect(self.start_pos_x, self.start_pos_y, self.ben_width, self.ben_height)
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

    def update(self):
        self.y += self.benefit_move_rate_y
        self.rect.centery = self.y

    def benefits_show(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
