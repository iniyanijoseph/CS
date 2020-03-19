from setuptools import setup
import pygame


class BASEBOT(pygame.sprite.Sprite):
    def __init__(self, weapona, weaponb, image):
        pygame.sprite.Sprite.__init__(self)
        self.weapona = weapona
        self.weaponb = weaponb
        self.health = 100
        self.image = pygame.image.load(image)
        self.image.get_rect()
        self.vel = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x += self.vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x -= self.vel
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y += self.vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y -= self.vel
        self.weapona.update()
        self.weaponb.update()


project = "CodeWars"
version = "0.0.1"
description = "Fight your coded creations"
packages = ["basebot"]
author = "Iniyan Joseph"
authoremail = "iniyanijoseph@gmail.com"
classifiers = [
    "Development Status :: 3 - Beta",
    "Intended Audience :: Education / Fun",
    "Programming Language :: Python :: 3"
]
keywords = ["Fight", "Pygame", "Python Fun"]
requires = ["pygame"]
setup(
    name=project,
    version=version,
    description=description,
    packages=packages,
    author=author,
    author_email=authoremail,
    classifiers=classifiers,
    keywords=keywords,
    requires=requires
)
