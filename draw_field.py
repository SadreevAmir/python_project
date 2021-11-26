from obstacles_2 import*
from pygame.draw import rect


def draw_square(screen, x, y):
    rect(screen, [250, 250, 250], [x*square_size, y*square_size, square_size, square_size])

def draw_field(screen):
    for i in range(number_of_vertical_squares):
        for j in range(number_of_horizontal_squares):
            if squares[j][i] == 1:
                draw_square(screen, j, i)


