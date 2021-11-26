from pygame import draw
from pygame.constants import NUMEVENTS
import pygame.draw
import random as rnd
from pygame.draw import polygon, rect









number_of_horizontal_squares = 50
number_of_vertical_squares = 30
number_of_obstacles = 50
obstacles_lenght_maximum = 10
square_size = 20


field_width = square_size * number_of_horizontal_squares
field_height = square_size * number_of_vertical_squares


squares = []


def new_square(x, y, squares):
    a = rnd.randint(-1, 1)
    b = rnd.randint(0, 1)
    if b == 1:
        x = x + a
    
    if b == 0:
        y = y + b


def suitable_square(x ,y, squares):

    return squares[x][y] == 0



for i in range(number_of_horizontal_squares):
    line = []

    for i in range(number_of_vertical_squares):
        line.append(0)
    
    squares.append(line)


for i in range(number_of_horizontal_squares - 1):
    squares[i][0] = 1
    squares[i][number_of_vertical_squares - 1] = 1

for i in range(number_of_vertical_squares - 1):
    squares[0][i] = 1
    squares[number_of_horizontal_squares - 1][i] = 1

 
def make_field():

    for i in range(number_of_obstacles):


        square_y = rnd.randint(0, number_of_vertical_squares - 1)
        square_x = rnd.randint(0, number_of_horizontal_squares - 1)

        x = square_x
        y = square_y

        obstacle_lenght = rnd.randint(0, obstacles_lenght_maximum)

        for i in range(obstacle_lenght):

            #while not suitable_square(x, y, squares):

            a = rnd.randint(-1, 1)
            b = rnd.randint(-1, 1)
            if b == 1:
                x = x + a
            else:
                y = y + b

            if (0 < x < number_of_horizontal_squares) and  (0 < y < number_of_vertical_squares):
                squares[x][y] = 1







        





