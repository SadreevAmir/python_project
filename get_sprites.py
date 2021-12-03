import pygame


class Sprites:
    def __init__(self, name_file, directory='sprites/'):
        self.filename = directory + name_file
        self.image = pygame.image.load(self.filename)
        self.numbers_image = 0
        self.size_x = 0
        self.size_y = 0
        self.currentFrame = -1
        self.delay_counter = 1
        self.data_search(name_file)
        self.sprite = self.get_sprite()

    def data_search(self, search_object, search_location='sprites/Monsta_notes.txt'):
        with open(search_location, 'r') as f:
            for line in f:
                str = line[:-1]
                if str == search_object:
                    break
            line = f.readline()[:-1]
            data = [int(s) for s in line.split() if s.isdigit()]
            self.numbers_image = data[0]
            self.size_x = data[1]
            self.size_y = data[2]

    def get_sprite(self, mirroring=False):
        self.animation()
        sprite = pygame.Surface((self.size_x, self.size_y), pygame.SRCALPHA)
        sprite.blit(self.image, (-self.size_x * self.currentFrame, 0))
        sprite = pygame.transform.flip(sprite, mirroring, False)
        return sprite

    def animation(self):
        if self.delay_counter == 3:
            self.currentFrame = (self.currentFrame + 1) % self.numbers_image
            self.delay_counter = 0
        else:
            self.delay_counter += 1
