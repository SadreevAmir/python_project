from pygame import draw
import pygame.draw
import random as rnd
from pygame.draw import polygon, rect




field_width = 1400
field_height = 800
size_factor_height = 100
size_factor_width = 100
number_of_obstacles = 30
obstacles = []





class Obstacles:


    def __init__(self):
        '''x, y - координаты прямоугольника
        width - ширина прямоугольника
        height - высота прямоугольника'''
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0



    def new_obstacle(self, field_width, field_height, size_factor_width, size_factor_height):

        '''
        создает объект класса Obstacles со случайными параметрами, зависящими от размеров экрана
        '''
        self.x = rnd.randint(0, field_width)
        self.y = rnd.randint(0, field_height)
        self.width = rnd.randint(int(size_factor_width/3), size_factor_width)
        self.height = rnd.randint(int(size_factor_height/3), size_factor_height)



    def draw_obstacle(self, screen):

        '''рисует объект класса Obstacles'''

        polygon(screen, [250, 250, 250], [[self.x + self.width/2, self.y + self.height/2], 
                                          [self.x + self.width/2, self.y - self.height/2],
                                          [self.x - self.width/2, self.y - self.height/2],
                                          [self.x - self.width/2, self.y + self.height/2]])
    





def create_obstacles_set(field_width,  field_height, size_factor_width, size_factor_height):

    '''создвет список всех объектов класса Obstacles'''

    for i in range(number_of_obstacles):
        obstacle = Obstacles()
        obstacle.new_obstacle(field_width,  field_height, size_factor_width, size_factor_height)
        obstacles.append(obstacle)





def draw_field(screen):

    '''рисует игровое поле'''
    
    for obj in obstacles:
        obj.draw_obstacle(screen)
    







