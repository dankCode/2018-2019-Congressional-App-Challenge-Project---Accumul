
import tkinter as tk
import pygame as pyg
import sys
from random import randint
from pygame.sprite import Group
from Bullet import Bullet
from Player_Settings import Player
from Benefits import Benefits

# initialize
menu = tk.Tk()
menu.geometry("360x200")


def main_game():
    # initialize pygames
    pyg.init()
    SCREEN_SIZE = (750, 750)
    SCREEN = pyg.display.set_mode(SCREEN_SIZE)
    pyg.display.set_caption("Accumul")

    p = Player(SCREEN, 'Arrow.png', 5)
    ammunition = Group()
    benefits = Group()

    # For mouse clicks
    LEFT = 1

    # data exclusive to the 'benefits' in the game
    benefits_min_gen = 1
    benefits_max_gen = 5
    benefits_max_pop = 20

    score_count = 0
    game_over = False


    while not game_over:

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                sys.exit()
            if event.type == pyg.MOUSEBUTTONDOWN and (event.button == LEFT):
                bullet = Bullet(SCREEN, p)
                ammunition.add(bullet)
            if event.type == pyg.MOUSEBUTTONUP and (event.button == LEFT):
                pass
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_a or event.key == pyg.K_RIGHT:
                    p.go_left = True
                elif event.key == pyg.K_d or event.key == pyg.K_LEFT:
                    p.go_right = True  # move right
                elif event.key == pyg.K_s or event.key == pyg.K_DOWN:
                    p.go_down = True  # move down
                elif event.key == pyg.K_w or event.key == pyg.K_UP:
                    p.go_up = True  # move upd
            if event.type == pyg.KEYUP:
                if event.key == pyg.K_a or event.key == pyg.K_LEFT:
                    p.go_left = False
                elif event.key == pyg.K_d or event.key == pyg.K_RIGHT:
                    p.go_right = False  # move right
                elif event.key == pyg.K_s or event.key == pyg.K_DOWN:
                    p.go_down = False  # move down
                elif event.key == pyg.K_w or event.key == pyg.K_UP:
                    p.go_up = False  # move up

        SCREEN.fill((0, 0, 0))  # the background is completely black
        ammunition.update()
        benefits.update()
        p.update_position()
        p.blit_player()  # Shows the update image of the player


        # update the bullets
        for bullet in ammunition.copy():
            if bullet.rect.y <= 0:
                ammunition.remove(bullet)

        for bullet in ammunition.sprites():
            bullet.show_bullet()


        # update benefits
        if len(benefits) < benefits_max_pop:
            for x in range(randint(benefits_min_gen, benefits_max_gen)):
                benefits.add(
                    Benefits(SCREEN, randint(0, SCREEN_SIZE[0]), randint(0, SCREEN_SIZE[1] - (SCREEN_SIZE[1] * 0.90))))

        for benefit in benefits.sprites():
            benefit.benefits_show()

        for benefit in benefits.copy():
            if benefit.rect.y > SCREEN_SIZE[1]:
                benefits.remove(benefit)

        if pyg.sprite.spritecollideany(p, benefits):
            endtxt = pyg.font.SysFont("none", 25)
            endlabel = endtxt.render("Game Over! Score: " + str(score_count), 1, (0, 255, 255))
            SCREEN.blit(endlabel, (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2))
            game_over = True

        if pyg.sprite.groupcollide(ammunition, benefits, True, True):
            score_count += 1

        pyg.display.flip()


var = tk.StringVar()
title = tk.Label(menu, textvariable=var).grid(row=0)
start_button = tk.Button(menu, text="start", command=main_game).grid(row=1)
close_button = tk.Button(menu, text="Exit", command=menu.destroy).grid(row=2)
var.set('Welcome to Accumul - "Award winning User Interface"')
tk.mainloop()
