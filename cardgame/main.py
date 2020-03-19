import pygame
import random
import keyboard
pygame.init()
win = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Wassap")
enelist = pygame.sprite.Group()
threshold = 5


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 10
        self.weapon = 3
        self.image = pygame.image.load("hero.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def deal(self, enemy):
        enemy.health -= self.weapon
        if enemy.health <= 0:
            enelist.remove(enemy)

    def update(self):
        pass


class Enemy(object):
    def __init__(self):
        self.health = random.randint(threshold - 2, threshold + 2)
        self.weapon = random.randint(5, 7)

    def deal(self, player):
        player.health -= self.weapon

    def update(self):
        pass


p = Player()
e = Enemy()
enelist.add(e)
run = True
while run:
    if keyboard.is_pressed("esc"):
        run = False
    enelist.draw()

pygame.quit()
