import pygame
import random
pygame.init()
pygame.mixer.init()
width = 500
height = 300
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("TERRARIA")
fps = pygame.time.Clock()
players = pygame.sprite.Group()
defpix = [pygame.image.load("leftface.png"), pygame.image.load("rightface.png")]
soilland = pygame.sprite.Group()


class terrarian(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = defpix[1]
        self.rect = self.image.get_rect()
        self.vel = 30
        self.rect.center = (100, 100)

    def update(self):  # Movement Logic
        pass


class surface(pygame.sprite.Sprite):
    def __init__(self, center, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tile.png")
        self.rect = self.image.get_rect()
        self.vel = 10
        self.rect.center = center

    def update(self):  # Movement Logic
        keys = pygame.key.get_pressed()
        if not pygame.sprite.groupcollide(players, soilland, False, False):
            self.rect.y -= self.vel + 5
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x += self.vel
            self.image = defpix[0]
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x -= self.vel
            self.image = defpix[1]
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            # jump logic
            self.rect.y += self.vel
        if self.rect.center[0] > width:
            self.rect.center = (0, self.rect.center[1])
        if self.rect.center[0] <= 0:
            self.rect.center = (width, self.rect.center[1])


ter = terrarian()
players.add(ter)

for element in range(width + 20):
    for ele in range(280, height + 20):
        place = random.randint(1, 255)
        if place != 1:
            lan = surface((element, ele), place)
            soilland.add(lan)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))
    players.update()
    players.draw(win)
    soilland.update()
    soilland.draw(win)
    pygame.display.update()
    pygame.display.flip()


pygame.quit()