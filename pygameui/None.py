import pygame  # Import the module for use
pygame.init()  # Initialize the video system for output

win = pygame.display.set_mode((750, 500))  # Create a window to which we can draw onto
configlist = [(255, 255, 255), 'Pygame Project']
pygame.display.set_caption(configlist[1]) 
allobjects = pygame.sprite.Group()

# Classes
class thing(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Iniyan\\CS\\Terraria\\blackblock.png").convert()
        self.rect = self.image.get_rect()
    
    def update(self):
        for element in range(5):
            self.rect.x += 1
            self.rect.y += 1



allobjects.add(thing())

run = True  # Variable we can use to end the window
while run:
    win.fill(configlist[0])
    allobjects.update()
    allobjects.draw(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
    pygame.time.delay(100)
