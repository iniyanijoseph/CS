import pygame
pygame.init()
#pyganim
win = pygame.display.set_mode((500, 500))
blocks = pygame.sprite.Group()
players = pygame.sprite.Group()
speed = 5


class blockclass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("blackblock.png").convert()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= speed
        if self.rect.x <= 0:
            self.rect.x = 500
        for player in players:
            if len(pygame.sprite.spritecollide(player, blocks, False)) > 0:
                player.health -= 2


class user(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("jetpacker.png").convert()
        self.rect = self.image.get_rect()
        self.health = 10
        self.rect.x = 300
        self.rect.y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed


for ycor in range(350, 500, 10):
    for element in range(0, 500, 9):
        newblock = blockclass()
        newblock.rect.x = element
        newblock.rect.y = ycor
        blocks.add(newblock)

players.add(user())
run = True
while run:
    print(speed)
    pygame.time.delay(100)
    win.fill((255, 255, 255))
    blocks.update()
    blocks.draw(win)
    players.update()
    players.draw(win)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
pygame.display.quit()

