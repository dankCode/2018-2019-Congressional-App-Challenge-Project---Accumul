

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, screen, player):
        super(Bullet, self).__init__()
        self.bullet_speed = 6.4
        self.bullet_width = 4
        self.bullet_height = 7
        self.bullet_color = (255, 255, 255)
        self.screen = screen

        # create Bullet from where the player's location
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

        self.bullet_y = float(self.rect.y)

    def update(self):
        self.bullet_y -= self.bullet_speed
        self.rect.y = self.bullet_y

    def show_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
