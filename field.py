from constants import *
import random
from perlin_noise import PerlinNoise


class NumField:
    """
    класс, отвечающий за создание начальной конфигурации поля
    blocks - список, содержащий всю инофрмацию об изначаьлном поле
    """

    def __init__(self):
        self.blocks = []

    def create_vertical_borders(self):
        """
        заполняет левый и првый столбец списка значениями -2
        :return:
        self.blocks:list
        """
        for i in range(NUMBER_OF_VERTICAL_BLOCKS):
            self.blocks[i][0], self.blocks[i][NUMBER_OF_HORIZONTAL_BLOCKS - 1] = -2, -2

    def create_horizontal_borders(self):
        """
        заполняет левый и првый столбец списка значениями -2
        :return:
        self.blocks:list
        """
        self.blocks[0] = [-2] * NUMBER_OF_HORIZONTAL_BLOCKS
        self.blocks[NUMBER_OF_VERTICAL_BLOCKS - 1] = [-2] * NUMBER_OF_HORIZONTAL_BLOCKS

    def create_special_box(self):
        """
        создает в левом верхнем и првом нижнем углах поля пустые области, где изначально появляется перосонаж
        """
        for i in range(1, NUMBER_OF_VERTICAL_BLOCKS // 10):
            for j in range(1, NUMBER_OF_HORIZONTAL_BLOCKS // 5):
                self.blocks[i][j] = 0

        for i in range(NUMBER_OF_VERTICAL_BLOCKS - NUMBER_OF_VERTICAL_BLOCKS // 10, NUMBER_OF_VERTICAL_BLOCKS - 1):
            for j in range(NUMBER_OF_HORIZONTAL_BLOCKS - NUMBER_OF_HORIZONTAL_BLOCKS // 5,
                           NUMBER_OF_HORIZONTAL_BLOCKS - 1):
                self.blocks[i][j] = 0

    def make_special_tunnel(self):
        """
        добавляет нули в список таким обзразом,
        что игроки могут дойти друг до друга, не ломая блоки
        :return:
        self.blocks:list
        """
        a = 0.0001
        b = random.uniform(-0.026, -0.01)
        k = HERO_SiZE_X // BLOCK_SIZE - 1
        c = -a * NUMBER_OF_HORIZONTAL_BLOCKS ** 2 + NUMBER_OF_VERTICAL_BLOCKS / \
            NUMBER_OF_HORIZONTAL_BLOCKS - b * NUMBER_OF_HORIZONTAL_BLOCKS
        change = False
        changes = 0
        for j in range(5):
            for i in range(4, NUMBER_OF_HORIZONTAL_BLOCKS - 4):
                if round(a * i ** 3 + b * i ** 2 + c * i) <= 2 or round(
                        a * i ** 3 + b * i ** 2 + c * i) >= NUMBER_OF_VERTICAL_BLOCKS - 2:
                    change = True
            if change:
                b = b / 2
                changes += 1
                change = False
        if changes == 5:
            a = 0
            b = 0
            c = -a * NUMBER_OF_HORIZONTAL_BLOCKS ** 2 + NUMBER_OF_VERTICAL_BLOCKS / \
                NUMBER_OF_HORIZONTAL_BLOCKS - b * NUMBER_OF_HORIZONTAL_BLOCKS

        for i in range(4, NUMBER_OF_HORIZONTAL_BLOCKS - 4):
            y = round(a * i ** 3 + b * i ** 2 + c * i)
            for j in range(i - k - 1, i + k):
                for p in range(y - k - 1, y + k):
                    self.blocks[p][j] = 0

    def create_number_field(self):
        """
        создает основную случайную часть поля
        :return:
        self.blocks:list
        """
        noise = PerlinNoise(octaves=10, seed=random.randint(0, 10 ^ 4))
        x_pix = NUMBER_OF_HORIZONTAL_BLOCKS
        y_pix = NUMBER_OF_VERTICAL_BLOCKS
        self.blocks = [[noise([i / x_pix, j / y_pix])
                        for j in range(x_pix)] for i in range(y_pix)]
        for i in range(NUMBER_OF_VERTICAL_BLOCKS):
            for j in range(NUMBER_OF_HORIZONTAL_BLOCKS):
                if self.blocks[i][j] >= 0.1:
                    self.blocks[i][j] = PLATFORMS_LIVES
                else:
                    self.blocks[i][j] = 0

        self.make_special_tunnel()
        self.create_vertical_borders()
        self.create_horizontal_borders()
        self.create_special_box()


def create_field():
    number_field = NumField()
    number_field.create_number_field()
    return number_field.blocks
