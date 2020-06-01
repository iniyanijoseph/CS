import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
topblocks = pygame.sprite.Group()
grndblocks = pygame.sprite.Group()

class Person(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("jetpacker.png").convert()
        self.rect = self.image.get_rect()
        self.vel = 10

    def gravity(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.rect.y += self.vel
        elif not keys[pygame.K_SPACE]:
            topblockshit = pygame.sprite.spritecollide(self, topblocks, True)
            if len(topblockshit) != 0:
                self.rect.y -= self.vel
            gbh = pygame.sprite.spritecollide(self, grndblocks, True)
            if len(gbh) != 0:
                self.rect.y += self.vel


run = True
while run:
    pygame.time.delay(100)
    win.fill((0, 0, 0))
    for element in playerlist:
        element.draw()
    pygame.display.update()  # Update the screen
pygame.display.quit()

