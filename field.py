from random import randint, choice, random
from constants import *
import random
import pygame


class NumberField:
    """
    Уровень в виде двумерного массива
    :param
    number_of_horizontal_blocks - количиство блоков по горизонтали
    number_of_vertical_blocks - количество блоков по вертикали
    number_of_obstacles - количество препятствий на уровне (представляют собой цепочку блоков)
    obstacles_length_max - максимальная длина препятствий
    """
    def __init__(self, number_of_horizontal_blocks, number_of_vertical_blocks,
                 number_of_obstacles, obstacles_length_max):
        self.NUMBER_OF_HORIZONTAL_BLOCKS = number_of_horizontal_blocks
        self.NUMBER_OF_VERTICAL_BLOCKS = number_of_vertical_blocks
        self.NUMBER_OF_OBSTACLES = number_of_obstacles
        self.OBSTACLES_LENGTH = obstacles_length_max

        self.blocks = [[0] * self.NUMBER_OF_HORIZONTAL_BLOCKS for i in range(self.NUMBER_OF_VERTICAL_BLOCKS)]

    def create_vertical_borders(self):
        for i in range(self.NUMBER_OF_VERTICAL_BLOCKS):
            self.blocks[i][0], self.blocks[i][self.NUMBER_OF_HORIZONTAL_BLOCKS-1] = 1, 1

    def create_horizontal_borders(self):
        self.blocks[0] = [1] * self.NUMBER_OF_HORIZONTAL_BLOCKS
        self.blocks[self.NUMBER_OF_VERTICAL_BLOCKS-1] = [1] * self.NUMBER_OF_HORIZONTAL_BLOCKS

    def create_obstacles(self):
        for i in range(self.NUMBER_OF_OBSTACLES):
            x = randint(0, self.NUMBER_OF_HORIZONTAL_BLOCKS-1)
            y = randint(0, self.NUMBER_OF_VERTICAL_BLOCKS-1)
            obstacle_length = randint(0, OBSTACLES_LENGTH_MAXIMUM)
            for j in range(obstacle_length):
                if (0 <= x < self.NUMBER_OF_HORIZONTAL_BLOCKS) and (0 <= y < self.NUMBER_OF_VERTICAL_BLOCKS):
                    self.blocks[y][x] = 1
                a = choice((-1, 1))
                b = randint(0, 1)
                x += a*b
                y += a*(1-b)

    def create_special_box(self):
        for i in range(1, NUMBER_OF_VERTICAL_BLOCKS//10):
            for j in range(1, NUMBER_OF_HORIZONTAL_BLOCKS//5):
                self.blocks[i][j] = 0

        for i in range(NUMBER_OF_VERTICAL_BLOCKS - NUMBER_OF_VERTICAL_BLOCKS//10, NUMBER_OF_VERTICAL_BLOCKS - 1):
            for j in range(NUMBER_OF_HORIZONTAL_BLOCKS - NUMBER_OF_HORIZONTAL_BLOCKS//5, NUMBER_OF_HORIZONTAL_BLOCKS - 1):
                self.blocks[i][j] = 0

    def create_special_tunnel(self, y, x):
        for i in range(NUMBER_OF_HORIZONTAL_BLOCKS*NUMBER_OF_VERTICAL_BLOCKS):
            x += random.randint(0, 1)
            if x >= NUMBER_OF_HORIZONTAL_BLOCKS - 3:
                x = NUMBER_OF_HORIZONTAL_BLOCKS - 3
            y += random.randint(0, 1)
            if y >= NUMBER_OF_VERTICAL_BLOCKS - 3:
                y = NUMBER_OF_VERTICAL_BLOCKS - 3 
            self.blocks[y + 1][x] = 0
            self.blocks[y + 1][x + 1] = 0
            self.blocks[y + 1][x - 1] = 0
            self.blocks[y][x] = 0
            self.blocks[y][x + 1] = 0
            self.blocks[y][x - 1] = 0
            self.blocks[y - 1][x] = 0
            self.blocks[y - 1][x + 1] = 0
            self.blocks[y - 1][x - 1] = 0

                
           
            
            
        
    



    


class Field:
    """
    Графическая интерпретация созданного уровня
    :param
    screen - поверхность для отрисовки
    number_field - уровень в виде массива
    """
    def __init__(self, screen, number_field):
        self.SCREEN = screen
        self.BLOCK_SIZE = BLOCK_SIZE
        self.number_field = number_field


num_field = NumberField(NUMBER_OF_HORIZONTAL_BLOCKS, NUMBER_OF_VERTICAL_BLOCKS,
                        NUMBER_OF_OBSTACLES, OBSTACLES_LENGTH_MAXIMUM)


def create_field(num_field):
    num_field.create_vertical_borders()
    num_field.create_horizontal_borders()
    num_field.create_obstacles()
    num_field.create_special_box()
    num_field.create_special_tunnel(3, 3)






