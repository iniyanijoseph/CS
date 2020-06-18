class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("*.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 260)
        self.rect.y = random.randint(10, 200)
    def update(self):
        blocks_hit_list = pygame.sprite.spritecollide(allobjects, allobjects, True)
        for block in blocks_hit_list:
        score += 1
        print(score)