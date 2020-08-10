import pygame
pygame.init()

win=pygame.display.set_mode((500,300))
players=pygame.sprite.Group()
ball=pygame.sprite.Group()

class LeftSide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Paddle.png")
        self.rect=self.image.get_rect()
        self.rect.x=10
        self.rect.y=10
        self.velocity=[0,0]
    def update(self):
        self.velocity=[0,0]
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y>0:
            self.velocity[1]-=4
        if keys[pygame.K_s] and self.rect.y+self.rect.height<300:
            self.velocity[1]+=4

        self.rect.x+=self.velocity[0]
        self.rect.y+=self.velocity[1]
class RightSide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Paddle.png")
        self.rect=self.image.get_rect()
        self.rect.x=420
        self.rect.y=10
        self.velocity=[0,0]
    def update(self):
        self.velocity=[0,0]
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y>0:
            self.velocity[1]-=4
        if keys[pygame.K_DOWN] and self.rect.y+self.rect.height<300:
            self.velocity[1]+=4

        self.rect.x+=self.velocity[0]
        self.rect.y+=self.velocity[1]
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Ball.png")
        self.rect=self.image.get_rect()
        self.rect.x=250
        self.rect.y=10
        self.velocity=[2,2]
    def update(self):
        for each in players:
            if pygame.sprite.collide_rect(self, each):
                self.velocity[0]*=-1
        if 500<self.rect.x or self.rect.x<0:
            exit()
        if self.rect.y>300-self.rect.height*2 or self.rect.y<0:
            self.velocity[1]*=-1
        self.rect.x+=self.velocity[0]
        self.rect.y+=self.velocity[1]

players.add(LeftSide())
players.add(RightSide())
ball.add(Ball())

clock=pygame.time.Clock()
run=True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    win.fill((0,0,0))
    players.update()
    players.draw(win)
    ball.update()
    ball.draw(win)
    pygame.display.update()
pygame.display.quit()