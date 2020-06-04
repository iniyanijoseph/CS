class thing(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Iniyan\\CS\\Terraria\\blackblock.png").convert()
        self.rect = self.image.get_rect()
    
    def update(self):
        for element in range(5):
            self.rect.x += 1
            self.rect.y += 1