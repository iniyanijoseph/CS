import pygame
import random
# import neat
pygame.init()
wid = 225
height = 400
win = pygame.display.set_mode((wid, height))
pygame.display.set_caption("Flappy Bird")


class player(object):
    def __init__(self):
        self.x = 50
        self.y = height // 2
        self.vel = 15
        self.radius = 5
        self.jump = False
        self.color = (255, 255, 255)
        self.jumpnum = 0

    def move(self, keys):
        if keys[pygame.K_UP] and not self.jump and self.jumpnum < 10:
            self.jump = True
            self.y -= self.vel
            self.jump = False
            self.jumpnum = 0
        elif bird.y + 2 * bird.radius <= height:
            bird.y += bird.vel

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius, 0)


class pipe:
    def __init__(self):
        self.width = 50
        self.x = wid - self.width
        self.y = height // 4 + random.randint(1, height // 5)
        self.height = height - self.y
        self.vel = 5

    def draw(self):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, (255, 255, 255), (self.x, 0, self.width, height - self.height - random.randint(150, 250)))

    def scroll(self):
        self.x -= self.vel


bird = player()
pipes = [pipe()]

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    bird.move(keys)
    # background
    win.fill((0, 0, 0))
    pygame.display.flip()
    bird.draw(win)
    for p in pipes:
        p.draw()
        p.scroll()
    pygame.display.update()

pygame.quit()

