import pygame
from constants import *
from get_sprites import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, kind, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.kind = kind
        self.image = pygame.image.load('sprites/Fireball.png')
        self.image = pygame.transform.scale(self.image, (HERO_SIZE_Y//2, HERO_SIZE_Y//2))
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
        # убить, если он заходит за верхнюю часть экрана

    def collision(self, platforms, characters):
        for p in platforms:
            if self.rect.colliderect(p) and not (self.kind is p):
                p.lives -= 1
                if p.lives == 0:
                    platforms.remove(p)
                self.kill()
        for kind in characters:
            if self.rect.colliderect(kind) and not (kind is self.kind):
                kind.lives -= 1
                self.kill()
