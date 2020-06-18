import pygame  # Import the module for use
import random

pygame.init()  # Initialize the video system for output

configlist = [(0.0, 0.0, 0.0), 'Space Invaders', (280, 400)]
win = pygame.display.set_mode(configlist[2])  # Create a window to which we can draw onto
pygame.display.set_caption(configlist[1])
allobjects = pygame.sprite.Group()


# Classes
class fight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Iniyan\\CS\\invaders\\a.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 110
        self.rect.y = 380

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            allobjects.add(projectile(self.rect.x + 5, self.rect.y + 5))


class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Iniyan\\CS\\invaders\\b.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 260)
        self.rect.y = random.randint(10, 200)

    def update(self):
        pygame.sprite.groupcollide(allobjects, allobjects, True, True)


class projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("C:\\Users\\Iniyan\\CS\\invaders\\a.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.rect.y += 10


for element in range(1):
    allobjects.add(fight())
for element in range(20):
    allobjects.add(enemy())

run = True  # Variable we can use to end the window
while run:
    win.fill(configlist[0])
    allobjects.update()
    allobjects.draw(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    pygame.time.delay(100)
pygame.quit()
