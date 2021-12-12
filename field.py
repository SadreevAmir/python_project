from constants import* 
import random
from perlin_noise import PerlinNoise




def create_vertical_borders(num_field):
        for i in range(NUMBER_OF_VERTICAL_BLOCKS):
            num_field[i][0], num_field[i][NUMBER_OF_HORIZONTAL_BLOCKS-1] = 1, 1


def create_horizontal_borders(num_field):
        num_field[0] = [1] * NUMBER_OF_HORIZONTAL_BLOCKS
        num_field[NUMBER_OF_VERTICAL_BLOCKS-1] = [1] * NUMBER_OF_HORIZONTAL_BLOCKS

def create_special_box(num_field):
        for i in range(1, NUMBER_OF_VERTICAL_BLOCKS//10):
            for j in range(1, NUMBER_OF_HORIZONTAL_BLOCKS//5):
                num_field[i][j] = 0

        for i in range(NUMBER_OF_VERTICAL_BLOCKS - NUMBER_OF_VERTICAL_BLOCKS//10, NUMBER_OF_VERTICAL_BLOCKS - 1):
            for j in range(NUMBER_OF_HORIZONTAL_BLOCKS - NUMBER_OF_HORIZONTAL_BLOCKS//5, NUMBER_OF_HORIZONTAL_BLOCKS - 1):
                num_field[i][j] = 0

def make_specaial_tunnel(num_field):
    a = 0.0001
    c = random.uniform(0.5, 2.1)
    b = NUMBER_OF_VERTICAL_BLOCKS/NUMBER_OF_HORIZONTAL_BLOCKS**2 - c/NUMBER_OF_HORIZONTAL_BLOCKS - a*NUMBER_OF_HORIZONTAL_BLOCKS
    for i in range(2, NUMBER_OF_HORIZONTAL_BLOCKS - 2):
        k = HERO_SiZE_X//BLOCK_SIZE - 1
        y = round(a*i**3 + b*i**2 + c*i)
        for j in range(i - k, i + k + 1):
            for l in range(y - k, y + k + 1):
                num_field[l][j] = 0
        




def create_field(num_field):


    noise = PerlinNoise(octaves=10, seed=random.randint(0,10^4))
    xpix = NUMBER_OF_HORIZONTAL_BLOCKS
    ypix = NUMBER_OF_VERTICAL_BLOCKS
    num_field = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
    for i in range(NUMBER_OF_VERTICAL_BLOCKS):
        for j in range(NUMBER_OF_HORIZONTAL_BLOCKS):
            if  num_field[i][j] >= 0.1:
                num_field[i][j] = 1
            else:
                num_field[i][j] = 0

    make_specaial_tunnel(num_field)
    create_vertical_borders(num_field)
    create_horizontal_borders(num_field)
    create_special_box(num_field)
    
    return num_field

   


