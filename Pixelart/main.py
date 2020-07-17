import pygame
import tkinter
import tkinter.colorchooser
width = 450
height = 483
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("asdfhkjldsh")
drawcolor = (0, 255, 255)


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.color = (255, 255, 255)

    def update(self):
        self.image.fill(self.color)
        if self.rect.x + self.rect.width > pygame.mouse.get_pos()[0] > self.rect.x:
            if self.rect.y + self.rect.height > pygame.mouse.get_pos()[1] > self.rect.y:
                if pygame.mouse.get_pressed()[0]:
                    self.color = drawcolor
                if pygame.mouse.get_pressed()[2]:
                    self.color = (255, 255, 255)


class Button(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("ColorButton.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.color = (255, 255, 255)

    def update(self):
        self.image.fill(self.color)
        if self.rect.x + self.rect.width > pygame.mouse.get_pos()[0] > self.rect.x:
            if self.rect.y + self.rect.height > pygame.mouse.get_pos()[1] > self.rect.y:
                if pygame.mouse.get_pressed()[0]:
                    #global drawcolor
                    #drawcolor = tkinter.colorchooser.askcolor()[0]


grid = pygame.sprite.Group()
for x in range(0, width, 11):
    for y in range(0, height-50, 11):
        block = Block()
        block.rect.x = x
        block.rect.y = y
        grid.add(block)

buttons = pygame.sprite.Group()
buttons.add(Button((5, height-50)))

clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0, 0, 0))
    grid.update()
    grid.draw(win)
    buttons.update()
    buttons.draw(win)
    pygame.display.flip()
    clock.tick(90)
