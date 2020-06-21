import random
import neat
import pygame
import os
import sys
pygame.init()

players = pygame.sprite.Group()
bars = pygame.sprite.Group()
generation = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("b.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 260)
        self.rect.y = random.randint(10, 200)
        self.countdown = 500

    def update(self):
        if self.countdown == 0:
            self.rect.x = random.randint(20, 260)
            self.rect.y = random.randint(10, 200)
            self.countdown = 500
        self.countdown -= 1
        for e in enemies:
            if pygame.sprite.collide_rect(self, e) and e != self:
                self.rect.x = random.randint(20, 260)
                self.rect.y = random.randint(10, 200)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()
        self.distance = 0
        self.rect.x = x + 25
        self.rect.y = players.sprites()[0].rect.y

    def update(self):
        self.hitenemy()
        self.rect.y -= 5

    def hitenemy(self):
        for enemy in enemies:
            if pygame.sprite.collide_rect(self, enemy):
                enemies.remove(enemy)
                return True
        return False


class Bar(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load("bar.png")
        self.rect = self.image.get_rect()
        self.rect.x = x + 15
        self.rect.y = 0
        self.distance = 0

    def update(self):
        self.checkdist()
        if self.rect.x < 15:
            self.rect.x = 15
        if self.rect.x > 265:
            self.rect.x = 265

    def checkdist(self):
        for enemy in enemies:
            if pygame.sprite.collide_rect(self, enemy):
                self.distance = enemy.rect.x
            else:
                self.distance = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("a.png")
        self.rect = self.image.get_rect()
        self.rect.x = 110
        self.rect.y = 380
        self.seebar = Bar(self.rect.x)
        self.bullets = pygame.sprite.Group()
        bars.add(self.seebar)
        self.index = 0
        self.score = 0
        self.countdown = 200
        self.enemies = pygame.sprite.Group()
        for element in range(20):
            self.enemies.add(Enemy())

    def moveright(self, g):
        self.rect.x += 5
        self.seebar.rect.x += 5
        g[self.index][1].fitness += 1

    def moveleft(self, g):
        self.rect.x -= 5
        self.seebar.rect.x -= 5
        g[self.index][1].fitness += 1

    def shoot(self, g):
        self.bullets.add(Bullet(self.rect.x))
        g[self.index][1].fitness += 1

    def update(self, win, genomes):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.moveright(genomes)
        if keys[pygame.K_LEFT]:
            self.moveleft(genomes)
        if keys[pygame.K_UP]:
            self.shoot(genomes)

        if self.rect.x < 0:
            self.rect.x = 0
            genomes[self.index][1].fitness -= 2

        if self.rect.x > 250:
            self.rect.x = 250
            genomes[self.index][1].fitness -= 2
        for b in self.bullets:
            if b.hitenemy:
                b.remove()
                self.score += 1
                genomes[self.index][1].fitness += 5
        self.bullets.update()
        self.bullets.draw(win)

        if self.countdown == 0:
            players.remove(self)
        self.countdown -= 1


def main(genomes, config):
    nets = []
    global players
    global enemies
    global bars
    enemies = pygame.sprite.Group()
    bars = pygame.sprite.Group()
    players = pygame.sprite.Group()

    for genomid, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        players.add(Player())

    win = pygame.display.set_mode((280, 400))
    pygame.display.set_caption("Space Invaders AI")
    for i, player in enumerate(players.sprites()):
        player.index = i

    run = True
    for num in range(100):
        enemies.add(Enemy())

    global generation
    generation += 1
    while run:
        pygame.time.delay(100)
        if len(players) == 0 or len(enemies) == 0:
            break
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        if len(players.sprites()) == 0:
            break

        for index, g in enumerate(players.sprites()):
            output = nets[index].activate((g.rect.x, g.seebar.distance, g.seebar.rect.x))
            if output[0] > 0.5:
                g.moveright(genomes)
            if output[1] > 0.5:
                g.moveleft(genomes)
            if output[2] > 0:
                g.shoot(genomes)

        win.fill((0, 0, 0))
        players.update(win, genomes)
        players.draw(win)
        enemies.update()
        enemies.draw(win)
        bars.update()
        pygame.display.update()


def run(configfile):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                configfile)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(main, 10000)
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == "__main__":
    localdir = os.path.dirname(__file__)
    configpath = os.path.join(localdir, "config.txt")
    run(configpath)
