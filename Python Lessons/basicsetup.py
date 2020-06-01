import pygame  # Import the module for use

pygame.init()  # Initialize the video system for output

win = pygame.display.set_mode((280, 400))  # Create a window to which we can draw onto
pygame.display.set_caption("First Game")  # Name the window


class Player(pygame.sprite.Sprite):  # Player class
    def __init__(self, x, y):  # Init Function
        super().__init__()  # Init everything from parent class
        self.image = pygame.image.load("playerpic.png")  # Load in the image
        self.x = x
        self.y = y


class Player():  # Player class
    def __init__(self, x, y):  # Init Function
        self.image = pygame.image.load("playerpic.png")  # Load in the image
        self.x = x  # x Coordinate
        self.y = y  # y Coordinate

    def draw(self):  # Draw Function
        win.blit(self.image, (self.x, self.y))  # Display Image

playerlist = []
playerlist.append(Player(0, 0))

run = True  # Variable we can use to end the window
while run:
    pygame.time.delay(100)
    win.fill((0, 0, 0))  # Provide Solid Colour Background
    # win.blit("backgroundpic.png")  # Provide Art Background or image
    for element in playerlist:
        element.draw()
    pygame.display.update()  # Update the screen
pygame.display.quit()  # Stop using Pygame

