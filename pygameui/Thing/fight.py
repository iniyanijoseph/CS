class fight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("*.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 110
        self.rect.y = 380
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
                self.rect.x += 5
        if keys[pygame.K_UP]:
                allobjects.add(projectile(self.rect.x + 5, self.rect.y + 5))