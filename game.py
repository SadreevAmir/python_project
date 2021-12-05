import pygame

from field import *
from constants import *
from hero import *
from platforms import *


def pause(screen):
    paused = True
    clock = pygame.time.Clock()
    font = pygame.font.Font(FONT, PAUSE_FONT_SIZE)
    text1 = font.render('paused', True, RED)
    text2 = font.render('tap or press enter to continue', True, RED)
    text3 = font.render('press backspace to quit', True, RED)

    while paused:
        clock.tick(FPS)
        screen.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT/3))
        screen.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT*1/2))
        screen.blit(text3, (WIDTH/2 - text3.get_width()/2, HEIGHT*2/3))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                pygame.quit()
                quit()
            if pygame.mouse.get_pressed()[0] == 1:
                paused = False
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            paused = False
        elif key[pygame.K_BACKSPACE]:
            pygame.quit()
            quit()
        pygame.display.update()


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # screen.fill([55, 255, 255])
    hero_sprites = pygame.sprite.Group()
    hero_1 = Hero(HERO_X, HERO_Y)
    hero_2 = Hero(WIDTH - HERO_X, HEIGHT - HERO_Y)

    create_field(num_field)
    create_platforms(num_field.blocks)

    hero_sprites.add(hero_1, hero_2)

    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        # screen.fill([55, 255, 255])
        game_back = pygame.image.load(game_background).convert()
        game_back = pygame.transform.scale(game_back, screen.get_size())
        screen.blit(game_back, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                pygame.quit()
                quit()
            else:
                hero_1.event_checking_hero_1(event)
                hero_2.event_checking_hero_2(event)
        hero_sprites.update(platforms, screen)
        for p in platforms:
            p.update(screen)
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pause(screen)
        pygame.display.update()
