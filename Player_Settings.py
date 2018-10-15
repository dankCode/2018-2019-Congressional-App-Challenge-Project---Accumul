

import pygame
import os


class Player:

    def __init__(self, screen, image, player_move_rate):
        self.screen = screen
        self.player_move_rate = player_move_rate
        image_folder = os.path.dirname(os.path.realpath(__file__))
        self.image = pygame.image.load(os.path.join(image_folder, image)).convert()
        self.rect = self.image.get_rect()
        self.scr_rect = screen.get_rect()
        # player's starting coordinates is at the center of the screen
        self.rect.centerx = float(self.scr_rect.centerx)
        self.rect.centery = float(self.scr_rect.centery)

        # for allowed continuous movement, a boolean variables are needed
        self.go_right = False
        self.go_left = False
        self.go_up = False
        self.go_down = False

    def update_position(self):
        if self.go_right and self.rect.right < self.scr_rect.right:
            self.rect.centerx += self.player_move_rate
        if self.go_left and self.rect.left > self.scr_rect.left:
            self.rect.centerx -= self.player_move_rate

        if self.go_up and self.rect.centery > 0:
            self.rect.centery -= self.player_move_rate
        if self.go_down and self.rect.bottom < self.scr_rect.h:
            self.rect.centery += self.player_move_rate

    def blit_player(self):
        self.screen.blit(self.image, self.rect)
