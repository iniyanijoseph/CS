import pygame  # Import the module for use
pygame.init()  # Initialize the video system for output

configlist = [(255, 255, 255), 'Pygame Project', (500, 300)]
win = pygame.display.set_mode(configlist[2])  # Create a window to which we can draw onto
pygame.display.set_caption(configlist[1]) 
allobjects = pygame.sprite.Group()

# Classes




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
