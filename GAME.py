import pygame
import sys
import random
import time

pygame.init()

scr_width = 1200
scr_height = 450

pygame.font.init()

you_win_text = pygame.font.SysFont("Times New Roman", 18, False, True)
you_lose_text = pygame.font.SysFont("Times New Roman", 18, True)



gameDisplay = pygame.display.set_mode((scr_width, scr_height))
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()
fps = 60

background = pygame.image.load("TUES.jpg")
gun = pygame.image.load("gun.png")
cursor = pygame.image.load("cursor.png")
dead = pygame.image.load("dead.png")

class Enemy:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = (pos_x, pos_y)
        self.image = pygame.image.load("sashi.png")

    def display_sashi(self):
        gameDisplay.blit(self.image, self.pos)

    def die(self):
        self.image = pygame.image.load("dead.png")
        gameDisplay.blit(self.image, self.pos)
        time.sleep(1)

    def detect_collision(self):
        if self.pos_x >= scr_width:
            self.pos_x -= 3
        if self.pos_y >= scr_height:
            self.pos_x -= 3
        if self.pos_x <= 0:
            self.pos_x += 3
        if self.pos_y <= 0:
            self.pos_y += 3

    def move(self):
        offset_x = random.choice((-3, 3))
        offset_y = random.choice((-3, 3))
        self.pos_x += offset_x
        self.pos_y += offset_y
        self.pos = (self.pos_x, self.pos_y)

enemy_pos_x = scr_width/2
enemy_pos_y = scr_height/2

num_sashis = 7
ammo = 14


while num_sashis > 0:

    sashi = Enemy(enemy_pos_x, enemy_pos_y)

    sashi_dead = False

    while not sashi_dead:
        pygame.display.flip()
        cursor_pos = pygame.mouse.get_pos()
        gameDisplay.blit(background, (0, 0))
        sashi.display_sashi()
        sashi.move()
        sashi.detect_collision()
        gameDisplay.blit(gun, (scr_width/2, scr_height/2))
        gameDisplay.blit(cursor, cursor_pos)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ammo -= 1
                if cursor_pos[0] > sashi.pos_x and cursor_pos[0] < sashi.pos_x + 60 and cursor_pos[1] > sashi.pos_y and cursor_pos[1] < sashi.pos_y + 78:
                    sashi.die()
                    sashi_dead = True
        if ammo == 0:
            break
        clock.tick(fps)

    num_sashis -= 1
if num_sashis == 0:
    print("You win...")
else:
    print("You lose...")
