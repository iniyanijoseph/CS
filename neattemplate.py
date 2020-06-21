def main(genomes, config):
    nets = []
    samplegroup = pygame.group.Group()

    for id, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        samplegroup.add(car)


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if len(samplegroup.sprites()) == 0:
            break

        for index, g in enumerate(group):
            output = nets[index].activate(())
            i = output.index(max(output))
            if i == 0:
                pass
            else:
                pass
    
        for i, car in enumerate(cars):
            genomes[i][1].fitness += car.get_reward() # 1 becuase 0 position is ID of object
        
        samplegroup.update()
        samplgroup.draw()


if __name__ == "__main__":
    # Set configuration file
    config_path = "config.txt"
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Create core evolution algorithm class
    p = neat.Population(config)

    # Add reporter for fancy statistical result
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run NEAT
    p.run(main, 1000)
