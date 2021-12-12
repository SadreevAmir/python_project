import pygame
from constants import *


class Sprites:
    def __init__(self, name_file, delay=50, t=1, real_size=False, directory='sprites/'):
        self.filename = directory + name_file
        self.image = pygame.image.load(self.filename)
        self.numbers_image = 0
        self.size_x = 0
        self.size_y = 0
        self.currentFrame = -1
        self.delay = delay
        #self.delay_counter = 1
        self.last_update = 0
        self.data_search(name_file, real_size)
        self.size_x *= t
        self.size_y *= t
        self.image = pygame.transform.scale(self.image, (self.size_x * self.numbers_image, self.size_y))
        self.sprite = self.get_sprite()

    def data_search(self, search_object, real_size, search_location='sprites/Monsta_notes.txt'):
        with open(search_location, 'r') as f:
            for line in f:
                str = line[:-1]
                if str == search_object:
                    break
            line = f.readline()[:-1]
            data = [int(s) for s in line.split() if s.isdigit()]
            self.numbers_image = data[0]
            if real_size:
                self.size_x = data[1]
                self.size_y = data[2]
            else:
                self.size_x = HERO_SiZE_X
                self.size_y = HERO_SIZE_Y

    def get_sprite(self, mirroring=False):
        self.animation()
        self.sprite = pygame.Surface((self.size_x, self.size_y), pygame.SRCALPHA)
        self.sprite.blit(self.image, (-self.size_x * self.currentFrame, 0))
        self.sprite = pygame.transform.flip(self.sprite, mirroring, False)
        return self.sprite

    def animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.delay:
            self.currentFrame = (self.currentFrame + 1) % self.numbers_image
            self.last_update = now
        '''if self.delay_counter == 3:
            self.currentFrame = (self.currentFrame + 1) % self.numbers_image
            self.delay_counter = 0
        else:
            self.delay_counter += 1'''

'''
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill([55, 255, 255])

obj = Sprites('s_plyr_run_strip8.png', screen)

#obj.get_sprite(numbers)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    screen.fill([55, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    obj.animation(100, 0, True)
    pygame.display.update()

pygame.quit()'''