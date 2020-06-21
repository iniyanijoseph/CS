import pygame
import random
pygame.init()

win = pygame.display.set_mode((280, 400))
pygame.display.set_caption("First Game")


class fight(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel

    def draw(self, win):
        win.blit(pygame.image.load("a.png"), (self.x, self.y))


class enemy(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel

    def draw(self, win):
        win.blit(pygame.image.load("b.png"), (self.x, self.y))


class projectile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 3
        self.vel = 20

    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.radius)


player = fight(110, 380, 10)
enemies = []
bullets = []
num = 5
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for per in enemies:
        for bul in bullets:
            if per.x == bul.x:
                bullets.remove(bul)
                enemies.remove(per)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player.vel

    if keys[pygame.K_RIGHT]:
        player.x += player.vel
    if keys[pygame.K_UP]:
        bullets.append(projectile(player.x + 25, player.y))
    if num % 10 == 0:
        enemies.append(enemy(random.randint(20, 260), random.randint(10, 200), 10))
    num += 1
    if len(enemies) > 5:
        enemies.remove(enemies[0])
    if len(bullets) > 5:
        bullets.remove(bullets[0])
    win.fill((0, 0, 0))
    player.draw(win)

    for each in enemies:
        each.draw(win)
    for each in bullets:
        each.y -= each.vel
        each.draw(win)
    pygame.display.update()

pygame.quit()
