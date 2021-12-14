from constants import* 
import random
from perlin_noise import PerlinNoise



class NUM_FIELD:
    def __init__(self):
        self.blocks = []

    def create_vertical_borders(self):
            for i in range(NUMBER_OF_VERTICAL_BLOCKS):
                self.blocks[i][0], self.blocks[i][NUMBER_OF_HORIZONTAL_BLOCKS-1] = -2, -2




    def create_horizontal_borders(self):
            self.blocks[0] = [-2] * NUMBER_OF_HORIZONTAL_BLOCKS
            self.blocks[NUMBER_OF_VERTICAL_BLOCKS-1] = [-2] * NUMBER_OF_HORIZONTAL_BLOCKS

    def create_special_box(self):
            for i in range(1, NUMBER_OF_VERTICAL_BLOCKS//10):
                for j in range(1, NUMBER_OF_HORIZONTAL_BLOCKS//5):
                    self.blocks[i][j] = 0

            for i in range(NUMBER_OF_VERTICAL_BLOCKS - NUMBER_OF_VERTICAL_BLOCKS//10, NUMBER_OF_VERTICAL_BLOCKS - 1):
                for j in range(NUMBER_OF_HORIZONTAL_BLOCKS - NUMBER_OF_HORIZONTAL_BLOCKS//5, NUMBER_OF_HORIZONTAL_BLOCKS - 1):
                    self.blocks[i][j] = 0

    def make_specaial_tunnel(self):
        a = 0.0001
        b = random.uniform(-0.026, -0.01)
        k = HERO_SiZE_X//BLOCK_SIZE - 1
        c = -a*NUMBER_OF_HORIZONTAL_BLOCKS**2 + NUMBER_OF_VERTICAL_BLOCKS/NUMBER_OF_HORIZONTAL_BLOCKS - b*NUMBER_OF_HORIZONTAL_BLOCKS
        change = False
        changes = 0
        for j in range(5):
            for i in range(4, NUMBER_OF_HORIZONTAL_BLOCKS - 4):
                if round(a*i**3 + b*i**2 + c*i) <= 2 or round(a*i**3 + b*i**2 + c*i) >= NUMBER_OF_VERTICAL_BLOCKS - 2:
                    change = True
            if change:
                b = b/2
                changes += 1
                print(changes)
                change = False
        if changes == 5:
            a = 0
            b = 0
            c = -a*NUMBER_OF_HORIZONTAL_BLOCKS**2 + NUMBER_OF_VERTICAL_BLOCKS/NUMBER_OF_HORIZONTAL_BLOCKS - b*NUMBER_OF_HORIZONTAL_BLOCKS
    
        for i in range(4, NUMBER_OF_HORIZONTAL_BLOCKS - 4):
            y = round(a*i**3 + b*i**2 + c*i)
            for j in range(i - k - 1, i + k):
                for l in range(y - k - 1 , y + k):
                    self.blocks[l][j] = 0

    def create_nuber_field(self):
        noise = PerlinNoise(octaves=10, seed=random.randint(0,10^4))
        xpix = NUMBER_OF_HORIZONTAL_BLOCKS
        ypix = NUMBER_OF_VERTICAL_BLOCKS
        self.blocks = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
        for i in range(NUMBER_OF_VERTICAL_BLOCKS):
            for j in range(NUMBER_OF_HORIZONTAL_BLOCKS):
                if  self.blocks[i][j] >= 0.1:
                    self.blocks[i][j] = PLATFORMS_LIVES
                else:
                    self.blocks[i][j] = 1

        self.make_specaial_tunnel()
        self.create_vertical_borders()
        self.create_horizontal_borders()        
        self.create_special_box()
        

def create_field():
    num_field = NUM_FIELD()
    num_field.create_nuber_field()
    return num_field.blocks


   


