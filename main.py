from obstacles_2 import*
from draw_field import*


FPS = 30

pygame.init()

screen = pygame.display.set_mode((field_width, field_height))
make_field()
draw_field(screen)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


