from field import *
from constants import *

num_field = NumberField(NUMBER_OF_HORIZONTAL_BLOCKS, NUMBER_OF_VERTICAL_BLOCKS,
                        NUMBER_OF_OBSTACLES, OBSTACLES_LENGTH_MAXIMUM)
num_field.create_vertical_borders()
num_field.create_horizontal_borders()
num_field.create_obstacles()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
field = Field(screen, num_field)
field.draw_field()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()

pygame.quit()
