import pygame
from constants import HERO_SiZE_X, HERO_SIZE_Y


class Sprites:
    """
    Класс Sprites используется для обслуживания анимации чего-либо.

    Note:
        Описание спрайта должно содержаться в Monsta_notes
        (сколько картинок и сколько пикселей каждая через пробел, а строчкой выше название файла)

    Attributes:
        image - общий спрайт(все изображения на одном)
        sprite - картинка на данный момент
        остальные пораметры обслуживают анимацию(задержка прокрута, общее количество изображений,
        номер текущего, размер отдельно изображения)
    """
    def __init__(self, name_file, delay=50, t=1, real_size=False, directory='sprites/'):
        """
        Конструктор класса
        :param name_file: имя файла
        :param delay: задержка прокрута
        :param t: масштаб
        :param real_size: нужно ли оставить реальный размер или использовать константный размер
        :param directory: директория(по-умолчанию все в папке sprites
        """
        self.filename = directory + name_file
        self.image = pygame.image.load(self.filename)
        self.numbers_image = 0
        self.size_x = 0
        self.size_y = 0
        self.currentFrame = -1
        self.delay = delay
        self.last_update = 0
        self.data_search(name_file, real_size)
        self.size_x *= t
        self.size_y *= t
        self.image = pygame.transform.scale(self.image, (self.size_x * self.numbers_image, self.size_y))
        self.sprite = self.get_sprite()

    def data_search(self, search_object, real_size, search_location='sprites/Monsta_notes.txt'):
        """
        Поиск данных в Monsta_notes
        :param search_object: Какой файл ищем
        :param real_size: нужно ли подтянуть реальный масштаб
        :param search_location: место где ищем файл с описанием
        """
        with open(search_location, 'r') as f:
            for line in f:
                string = line[:-1]
                if string == search_object:
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
        """
        Получение картинки
        :param mirroring: нужно ли отзеркалить
        :return: картинка
        """
        self.animation()
        self.sprite = pygame.Surface((self.size_x, self.size_y), pygame.SRCALPHA)
        self.sprite.blit(self.image, (-self.size_x * self.currentFrame, 0))
        self.sprite = pygame.transform.flip(self.sprite, mirroring, False)
        return self.sprite

    def animation(self):
        """
        Прокрут анимации с задержкой(смена номера текущего изображения)
        """
        now = pygame.time.get_ticks()
        if now - self.last_update > self.delay:
            self.currentFrame = (self.currentFrame + 1) % self.numbers_image
            self.last_update = now
