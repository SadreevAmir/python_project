import pygame
from constants import *
from get_sprites import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, kind, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.kind = kind
        self.image = pygame.image.load('../python_project/sprites/Fireball.png')
        self.image = pygame.transform.scale(self.image, (40, 20))
        self.image = pygame.transform.flip(self.image, kind.FACING, False)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        if self.kind.FACING:
            self.speedy = -10
        else:
            self.speedy = 10

    def update(self, platforms, characters, screen):
        self.rect.x += self.speedy
        screen.blit(self.image, self.rect.topleft)
        self.collision(platforms, characters)
        print(1)
        # убить, если он заходит за верхнюю часть экрана

    def collision(self, platforms, characters):
        for p in platforms:
            if self.rect.colliderect(p):
                self.kill()
        for kind in characters:
            if self.rect.colliderect(kind) and not (kind is self.kind):
                kind.lives -= 1
                self.kill()
