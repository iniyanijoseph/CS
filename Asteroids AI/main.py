import pygame
pygame.init()
width = 380
height = 300


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Bullet.png")
        self.rect = self.image.get_rect()

    def collide(self, bullets, astroids):
        for a in astroids:
            if pygame.sprite.collide_rect(self, a):
                self.remove(bullets)

    def fire(self):
        self.rect.x -= 5
        self.rect.y -= 5

    def update(self, bullets, astroids):
        self.collide(bullets, astroids)
        self.fire()


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.original_image = self.image
        self.angle = 0
        self.x = 0
        self.y = 0
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shootcool = 5
        self.rect.x = (width // 2) - (self.rect.width // 2)
        self.rect.y = (height // 2) - (self.rect.height // 2)

    def right(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle -= 5 % 360
        self.x, self.y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def left(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle += 5 % 360
        self.x, self.y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def up(self):
        self.rect.x += 2
        self.rect.y += 2

    def shoot(self):
        if self.shootcool == 0:
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x, self.rect.y
            self.bullets.add(bullet)
            self.shootcool = 5
        self.shootcool -= 1

    def update(self, win):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.right()
        if keys[pygame.K_LEFT]:
            self.left()
        if keys[pygame.K_UP]:
            self.up()
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.bullets.draw(win)
        self.bullets.update(self.bullets, self.asteroids)


def main():
    ships = pygame.sprite.Group()
    for i in range(1):
        ships.add(Ship())
    win = pygame.display.set_mode((width, height))
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill((0, 0, 0))
        ships.draw(win)
        ships.update(win)
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
