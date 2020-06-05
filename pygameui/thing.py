class thing(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("*.png").convert()
        self.rect = self.image.get_rect()
    
    def update(self):
        pass