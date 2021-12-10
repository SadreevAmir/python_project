import pygame
from constants import *
from hero import *



class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, a, b):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((a, b))
        self.image.fill([0, 0, 0])
        self.rect = pygame.Rect(x, y, a, b)

    def update(self, platforms, characters, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

platforms = []

def create_platforms(number_field):
    for i in range(NUMBER_OF_VERTICAL_BLOCKS):
        for j in range(NUMBER_OF_HORIZONTAL_BLOCKS):
            if number_field[i][j] != 0:
                platform = Platform(j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                platforms.append(platform)