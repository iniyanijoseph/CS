import keyboard
from random_word import RandomWords
import pygame
pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((280, 430))
pygame.display.set_caption("GuillotineMan")
pygame.display.set_icon(pygame.image.load("4.png"))
music = pygame.mixer.music.load('epic.mp3')
winsound = pygame.mixer.Sound("win.wav")
losesound = pygame.mixer.Sound("lose.wav")
pygame.mixer.music.play(-1)
piclist = [pygame.image.load("start.png"), pygame.image.load("1.png"), pygame.image.load("2.png"), pygame.image.load("3.png"), pygame.image.load("4.png")]
alphabet = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
all_fonts = pygame.font.get_fonts()
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 25)
wordlist = RandomWords()
wronglet = []
word = wordlist.get_random_word()
objectlist = []
displaytext = ""
numwrong = 0
pressed = []
clock = pygame.time.Clock()


class letter(object):
    def __init__(self, letter):
        self.letter = letter
        self.display = "_"

    def ispressed(self):
        if keyboard.is_pressed(self.letter) and element not in pressed:
            self.display = self.letter
            pressed.append(pressed)


for element in word:
    objectlist.append(letter(element))


def displaytxt(x, y, text):
    text = font.render(text, True, (0, 0, 0), (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (x, y)
    win.blit(text, textRect)


def main(numwrong):
    run = True
    while run:
        clock.tick(5)
        displaytext = ""

        for obj in objectlist:
            obj.ispressed()

        for letter in alphabet:
            if keyboard.is_pressed(letter):
                if letter not in word and letter not in pressed:
                    numwrong += 1
                    pressed.append(letter)
                    wronglet.append(letter)

        for obj in objectlist:
            displaytext += obj.display

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keyboard.is_pressed("esc"):
                run = False

        if numwrong == (len(piclist) - 1):
            displaytext = "Lose"
            win.fill((255, 255, 255))
            win.blit(piclist[numwrong], (0, 0))
            displaytxt(150, 400, displaytext)
            displaytxt(150, 400, word)
            pygame.time.delay(1000)
            run = False

        if displaytext == word:
            displaytext = "Win"
            win.fill((255, 255, 255))
            win.blit(piclist[numwrong], (0, 0))
            displaytxt(150, 350, displaytext)
            displaytxt(150, 400, word)
            pygame.time.delay(1000)
            run = False

        if keyboard.is_pressed("`"):
            displaytext = word
        win.fill((255, 255, 255))
        win.blit(piclist[numwrong], (0, 0))
        displaytxt(140, 350, displaytext)
        displaytext = "".join(wronglet)
        displaytxt(150, 400, displaytext)
        pygame.display.update()


main(numwrong)
