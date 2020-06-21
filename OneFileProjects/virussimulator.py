import pygame
import time
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Community Spread")
lineindex = 0
populationindex = 0
population = []
for element in range(50):
    population.append([])


class Person(object):
    def __init__(self):
        self.health = 0
        self.spread = True
        self.new = True
        self.yindex = 0
        self.xindex = 0
        self.color = (71, 255, 139)
        self.x, self.y = self.xindex * 10, self.yindex * 10

    def kill(self):
        self.x, self.y = self.xindex * 10, self.yindex * 10
        if 0 < self.health <= 5:
            self.spreadit(self.yindex - 1, self.xindex)
            self.spreadit(self.yindex + 1, self.xindex)
            self.spreadit(self.yindex, self.xindex - 1)
            self.spreadit(self.yindex, self.xindex + 1)
            if self.spread:
                self.spread = False
            if self.new:
                self.new = False
            else:
                self.health += 1

            if self.health == 1:
                self.color = (160, 255, 71)
            if self.health == 2:
                self.color = (227, 255, 71)
            if self.health == 3:
                self.color = (255, 249, 71)
            if self.health == 4:
                self.color = (255, 172, 71)
            if self.health == 5:
                self.color = (255, 71, 71)

    def spreadit(self, y, x):
        if 0 <= y < len(population) and 0 <= x < len(population):
            case = population[y][x]
            if self.spread and case.health == 0:
                case.spread = False
                case.health += 1

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, 10, 10))


for line in population:
    for element in range(50):
        line.append(Person())

for line in population:
    for element in line:
        element.yindex = population.index(line)
        element.xindex = line.index(element)

middle = 25
population[middle][middle].health = 1
population[middle][middle].new = False

for element in range(int(input("Generations:"))):
    win.fill((255, 255, 255))
    for line in population:
        for person in line:
            person.spread = True
    for line in population:
        for person in line:
            person.kill()
    for line in population:
        for person in line:
            person.kill()
    for line in population:
        for person in line:
            person.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
    time.sleep(0.5)
    print("_______________________________________________________")
while True:
    win.fill((255, 255, 255))
    for line in population:
        for person in line:
            person.draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
