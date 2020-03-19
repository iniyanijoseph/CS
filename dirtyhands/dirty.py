import pygame
pygame.init()

width = 700
height = 350
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("")

bg = pygame.image.load("bg.png")


class person(object):
    def __init__(self, picture, x, y, width, height):
        self.picture = picture
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10

    def draw(self, win, picture):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))
        win.blit(picture, (self.x, self.y))




pac = person(pygame.image.load("pac2.png"), 20, 20, 55, 60)
gho = person(pygame.image.load("gho.png"), 100, 100, 65, 65)


def draw(win, pac, gho):
    win.blit(bg, (0, 0))
    pac.draw(win, pac.picture)
    gho.draw(win, gho.picture)
    pygame.display.update()


def main():
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            gho.y -= gho.vel

        if keys[pygame.K_DOWN]:
            gho.y += gho.vel

        if keys[pygame.K_RIGHT]:
            gho.x += gho.vel

        if keys[pygame.K_LEFT]:
            gho.x -= gho.vel

        if keys[pygame.K_w]:
            pac.y -= pac.vel
        if keys[pygame.K_s]:
            pac.y += pac.vel

        if keys[pygame.K_d]:
            pac.x += pac.vel

        if keys[pygame.K_a]:
            pac.x -= pac.vel

        if pac.x >= gho.x and pac.x <= gho.width + gho.x:
            if pac.y == gho.y:
                run = False
        draw(win, pac, gho)
    pygame.quit()


main()
