import pygame
import keyboard
pygame.init()
win = pygame.display.set_mode((500,300))
pygame.display.set_caption("ANGRY")

body = ["C:/Users/Iniyan/workspace/Game/angrify/face1.png", "C:/Users/Iniyan/workspace/Game/angrify/face2.png", "C:/Users/Iniyan/workspace/Game/angrify/face3.png", "C:/Users/Iniyan/workspace/Game/angrify/face4.png"]
pic = 0

run = True
while run:
    pygame.time.delay(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        pic += 1
    
    win.fill((255,255,255))
    win.blit(pygame.image.load(body[pic]), (0, 0)) 
    pygame.display.update()

pygame.quit()    