from obstacles import*


FPS = 30

pygame.init()

screen = pygame.display.set_mode((field_width, field_height))
create_obstacles_set(field_width,  field_height, size_factor_width, size_factor_height)

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


