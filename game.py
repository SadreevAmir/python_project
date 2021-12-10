import pygame
import glob
from field import *
from constants import *
from hero import *
from platforms import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.hero_sprites = pygame.sprite.Group()
        self.hero_1 = Hero1(HERO_X, HERO_Y)
        self.hero_2 = Hero2(WIDTH - HERO_X, HEIGHT - HERO_Y)
        self.background_image = game_background
        game_back = pygame.image.load(self.background_image).convert()
        self.game_back = pygame.transform.scale(game_back, self.screen.get_size())
        create_field(num_field)
        create_platforms(num_field.blocks)

        self.hero_sprites.add(self.hero_1, self.hero_2)

    def pause(self):
        clock = pygame.time.Clock()
        font = pygame.font.Font(FONT, PAUSE_FONT_SIZE)
        text1 = font.render('paused', True, RED)
        text2 = font.render('tap or press enter to continue', True, RED)
        text3 = font.render('press backspace to quit', True, RED)
        text4 = font.render('press shift to change background', True, RED)
        paused = True
        while paused:
            clock.tick(FPS)
            self.screen.blit(self.game_back, (0, 0))
            # self.hero_sprites.update(platforms, self.screen)
            self.screen.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT/4))
            self.screen.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT*5/12))
            self.screen.blit(text4, (WIDTH/2 - text4.get_width()/2, HEIGHT*7/12))
            self.screen.blit(text3, (WIDTH/2 - text3.get_width()/2, HEIGHT*3/4))
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
            elif key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
                self.change_background()
                game_back = pygame.image.load(self.background_image).convert()
                self.game_back = pygame.transform.scale(game_back, self.screen.get_size())

            pygame.display.update()

    def start_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # screen.fill([55, 255, 255])

        clock = pygame.time.Clock()
        finished = False

        while not finished:
            clock.tick(FPS)
            # screen.fill([55, 255, 255])
            self.screen.blit(self.game_back, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    pygame.quit()
                    quit()
                else:
                    self.hero_1.event_checking_hero(event)
                    self.hero_2.event_checking_hero(event)
            self.hero_sprites.update(platforms, self.screen)
            for p in platforms:
                p.update(self.screen)
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                self.pause()
            pygame.display.update()

    def change_background(self):
        files = glob.glob('game_back/*')
        pos = files.index(self.background_image)
        image = files[(pos+1) % len(files)]
        while not image.lower().endswith(('.png', '.jpg')):
            pos = (pos + 1) % len(files)
            image = files[(pos + 1) % len(files)]
        self.background_image = files[(pos + 1) % len(files)]

        pygame.time.delay(200)
