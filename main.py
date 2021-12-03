from field import *
from constants import *
from hero import *
from platforms import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill([55, 255, 255])
hero_sprites = pygame.sprite.Group()
hero_1 = Hero(HERO_X, HERO_Y)
hero_2 = Hero(WIDTH - HERO_X, HEIGHT - HERO_Y)


create_field(num_field)
create_platforms(num_field.blocks)

hero_sprites.add(hero_1, hero_2)

field = Field(screen, num_field)  

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    screen.fill([55, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            hero_1.event_checking_hero_1(event)
            hero_2.event_checking_hero_2(event)
    hero_sprites.update(platforms, screen)
    for p in platforms:
        p.update(screen)
    pygame.display.update()

pygame.quit()


