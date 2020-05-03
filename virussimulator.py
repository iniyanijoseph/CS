lineindex = 0
populationindex = 0
population = []
for element in range(6):
    population.append([])


def printnice():
    resultlist = []
    for line in range(len(population)):
        resultlist.append([])
        for person in population[line]:
            resultlist[line].append(person.health)
    for line in resultlist:
        print(line)


class Person(object):
    def __init__(self):
        self.health = 0
        self.spread = True
        self.new = True
        self.yindex = 0
        self.xindex = 0

    def kill(self):
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

    def spreadit(self, y, x):
        if 0 <= y < len(population) and 0 <= x < len(population):
            case = population[y][x]
            if self.spread and case.health == 0:
                case.spread = False
                case.health += 1


for line in population:
    for element in range(6):
        line.append(Person())

for line in population:
    for element in line:
        element.yindex = population.index(line)
        element.xindex = line.index(element)

middle = 0
population[middle][middle].health = 1
population[middle][middle].new = False

for element in range(int(input("Generations:"))):
    for line in population:
        for person in line:
            person.spread = True
    for line in population:
        for person in line:
            person.kill()
    printnice()
    print("_______________________________________________________")
