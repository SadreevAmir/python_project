import pygame
from constants import *
from hero import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, a, b):
        pygame.sprite.Sprite.__init__(self)
        self.color = DARK_GREEN
        self.image = pygame.Surface((a, b))
        self.rect = pygame.Rect(x, y, a, b)
        self.lives = PLATFORMS_LIVES

    def update(self, screen):
        if 0 <= self.lives < PLATFORMS_LIVES:
            self.color = [RED[0]*(1 - (self.lives - 1)/(PLATFORMS_LIVES - 1)), 0, 0]
        self.image.fill(self.color)
        screen.blit(self.image, (self.rect.x, self.rect.y))


    

platforms = []


def create_platforms(num_field):
    platforms.clear()
    for i in range(NUMBER_OF_VERTICAL_BLOCKS):
        for j in range(NUMBER_OF_HORIZONTAL_BLOCKS):
            if num_field[i][j] != 0:
                platform = Platform(j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                platforms.append(platform)


