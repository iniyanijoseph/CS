import os
import neat
import pygame

pygame.init()

guys = pygame.sprite.Group()
foods = pygame.sprite.Group()
ge = []
nets = []
output = []


class Guy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.image = pygame.image.load("walking.png")
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 50
        self.fat = 0
        self.carbs = 0
        self.protein = 0  #
        self.calories = 0  # 2000
        self.amounteaten = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if self.amounteaten == 3 and self.calories < 1500:
            self.reducefitness(10)
        if keys[pygame.K_RIGHT]:
            self.move()

        if keys[pygame.K_LEFT] and self.rect.x != 5:
            self.rect.x -= 100
        if self.rect.x < 4 or self.rect.x > 700:
            self.rect.x = 5
            if len(foods) == 6:
                self.reducefitness(5)

        if self.amounteaten == 3 and 2000 > self.calories > 1500:
            guys.sprites().pop(self.index)
            ge.pop(self.index)
            nets.pop(self.index)

    def eat(self):
        if self.fat > 50 or self.carbs > 225 or self.protein > 50 or self.calories > 2000:
            self.reducefitness(5)
        for food in foods:
            if pygame.sprite.collide_rect(self, food):
                try:
                    ge[self.index].fitness += 5
                    self.fat += food.fat
                    self.carbs += food.carbs
                    self.protein += food.protein
                    self.calories += food.calories
                    foods.remove(food)
                    self.amounteaten += 1
                    pygame.time.delay(200)
                except IndexError:
                    pass

    def move(self):
        self.rect.x += 100

    def reducefitness(self, amount):
        self.index = guys.sprites().index(self)
        try:
            ge[self.index].fitness -= amount
            guys.sprites().pop(self.index)
            ge.pop(self.index)
            nets.pop(self.index)
        except IndexError:
            pass


class Food(pygame.sprite.Sprite):
    def __init__(self, img, fat, carbs, protein, calories):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 60
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.calories = calories


def main(genomes, config):
    global ge
    global nets
    global guys
    global foods
    global output

    guys = pygame.sprite.Group()
    foods = pygame.sprite.Group()
    ge = []
    nets = []
    output = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        ge.append(genome)
    guys.add(Guy())

    for each in guys:
        burrito = Food("burrito.png", 30, 60, 22, 600)
        pizza = Food("Pizza.png", 24, 54, 20, 530)
        burger = Food("Burger.png", 18, 69, 24, 544)
        salad = Food("salad.png", 18, 69, 24, 544)
        rice = Food("rice.png", 18, 69, 24, 544)
        pasta = Food("pasta.png", 18, 69, 24, 544)
        foods.add(burrito)
        foods.add(pizza)
        foods.add(burger)
        foods.add(salad)
        foods.add(rice)
        foods.add(pasta)
        for index in range(len(foods)):
            foods.sprites()[index].rect.x = index * 100 + 100
    win = pygame.display.set_mode((700, 250))
    pygame.display.set_caption("Obesity Awareness AI")
    pygame.display.set_icon(pygame.image.load("cornucopia.png"))
    dorun = True
    while dorun:
        if len(guys) == 0 or len(foods) == 0:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dorun = False

        for g in guys:
            for f in foods:
                try:
                    output = nets[g.index].activate((f.fat, f.carbs, f.protein, f.calories))
                except IndexError:
                    pass
            if output[0] > 0.5:
                g.eat()
            else:
                g.reducefitness(0.5)

            if output[1] > 0.3:
                g.move()
            else:
                g.reducefitness(0.3)

        win.fill((255, 255, 255))
        guys.update()
        guys.draw(win)
        foods.update()
        foods.draw(win)
        pygame.display.update()


if __name__ == "__main__":
    # Set configuration file
    config_path = "./config-feedforward.txt"
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Create core evolution algorithm class
    p = neat.Population(config)

    # Add reporter for fancy statistical result
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run NEAT
    p.run(main, 1000)
