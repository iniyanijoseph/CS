import pygame
import math
import random
import os

xpos = 100
ypos = 60

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (xpos, ypos)

pygame.init()
width = 760
height = 600


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.size = size
        if self.size == 1:
            self.image = pygame.image.load("Asteroid.png")
        elif self.size == 2:
            self.image = pygame.image.load("Masteroid.png")
        elif self.size == 3:
            self.image = pygame.image.load("Sasteroid.png")
        self.rect = self.image.get_rect()
        while 260 < x < 460 and self.size == 1:
            x = random.randint(0, width)
        while 200 < y < 400 and self.size == 1:
            y = random.randint(0, height)
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.direction = [0, -1]
        self.change_x = 0
        self.change_y = 0
        self.angle = random.randint(0, 360)

    def collide(self, bullets, asteroids, ship):
        for b in bullets:
            if pygame.sprite.collide_circle(self, b):
                self.size += 1
                if self.size == 4:
                    asteroids.remove(self)
                else:
                    for element in range(self.size):
                        asteroids.add(Asteroid(self.size, self.rect.x, self.rect.y))
                        self.remove(asteroids)
        if pygame.sprite.collide_circle(self, ship):
            ships.remove(ship)
            return True

    def fly(self):
        self.rect.x += int(self.change_x)
        self.rect.y -= int(self.change_y)

    def update(self, bullets, asteroids, ship):
        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        self.fly()

        if self.size == 4:
            asteroids.remove(self)

        if self.rect.x < (0 - self.rect.width):
            self.rect.x = width
        if self.rect.x > width:
            self.rect.x = 0 - self.rect.width
        if self.rect.y > height:
            self.rect.y = 0 - self.rect.height
        if self.rect.y < (0 - self.rect.height):
            self.rect.y = height

        self.collide(bullets, asteroids, ship)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, change_x, change_y):
        super().__init__()
        self.image = pygame.image.load("Bullet.png")
        self.rect = self.image.get_rect()
        self.speed = 10
        self.countdown = 50
        self.change_x = change_x
        self.change_y = change_y

    def collide(self, bullets, asteroids):
        for a in asteroids:
            if pygame.sprite.collide_circle(self, a):
                self.remove(bullets)

    def fire(self):
        self.rect.x += int(self.change_x) * 2
        self.rect.y -= int(self.change_y) * 2

    def destroy(self, bullets):
        if self.countdown == 0:
            bullets.remove(self)
        self.countdown -= 1

    def update(self, bullets, asteroids, ship):
        if self.rect.x < (0 - self.rect.width):
            self.rect.x = width
        if self.rect.x > width:
            self.rect.x = 0 - self.rect.width
        if self.rect.y > height:
            self.rect.y = 0 - self.rect.height
        if self.rect.y < (0 - self.rect.height):
            self.rect.y = height

        self.destroy(bullets)
        self.collide(bullets, asteroids)
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
        self.shootcool = 1
        self.rect.x = (width // 2) - (self.rect.width // 2)
        self.rect.y = (height // 2) - (self.rect.height // 2)
        self.direction = [0, -1]
        self.change_x = 0
        self.change_y = 0
        self.speed = 5
        self.index = 0

        for element in range(10):
            self.asteroids.add(Asteroid(1, random.randint(0, width), random.randrange(0, height)))

    def right(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle -= 10 % 360
        self.x, self.y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def left(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle += 10 % 360
        self.x, self.y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def up(self):
        self.rect.x += int(self.change_x)
        self.rect.y -= int(self.change_y)

    def shoot(self):
        if self.shootcool == 0:
            bullet = Bullet(self.change_x, self.change_y)
            bullet.rect.x, bullet.rect.y = self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2
            self.bullets.add(bullet)
            self.shootcool = 20
        self.shootcool -= 1

    def update(self, win):
        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.right()
        if keys[pygame.K_LEFT]:
            self.left()
        if keys[pygame.K_UP]:
            self.up()
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.rect.x < (0 - self.rect.width):
            self.rect.x = width
        if self.rect.x > width:
            self.rect.x = 0 - self.rect.width
        if self.rect.y > height:
            self.rect.y = 0 - self.rect.height
        if self.rect.y < (0 - self.rect.height):
            self.rect.y = height

        self.asteroids.update(self.bullets, self.asteroids, self)
        self.asteroids.draw(win)

        self.bullets.draw(win)
        self.bullets.update(self.bullets, self.asteroids, self)


def main():
    global ships
    ships = pygame.sprite.Group()
    ships.add(Ship())
    win = pygame.display.set_mode((width, height))
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill((0, 0, 0))
        ships.update(win)
        ships.draw(win)
        pygame.display.flip()
        clock.tick(30)
        if len(ships) == 0:
            ships.add(Ship())


if __name__ == "__main__":
    main()
