import pygame
import glob
from field import *
from constants import *
from hero import *
from platforms import *
from menu import *
import os
sep = os.path.sep


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.hero_sprites = all_sprites
        self.hero_1 = Hero1(HERO_X, HERO_Y)
        self.hero_2 = Hero2(WIDTH - HERO_X, HEIGHT - HERO_Y)
        characters.append(self.hero_1)
        characters.append(self.hero_2)
        self.background_image = game_background
        game_back = pygame.image.load(self.background_image).convert()
        self.game_back = pygame.transform.scale(game_back, self.screen.get_size())
        num_field = create_field([])
        create_platforms(num_field)
        self.hero_sprites.add(self.hero_1, self.hero_2)

    def pause(self):
        pause = PauseMenu(self.screen, self.background_image, lambda: MainMenu(self.screen, menu_background,
                                                                               lambda: Game().start_game()).show(),
                          lambda: self.end_game())
        pause.show()
        self.background_image = pause.background_image
        game_back = pygame.image.load(self.background_image).convert()
        self.game_back = pygame.transform.scale(game_back, self.screen.get_size())

    def start_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        clock = pygame.time.Clock()
        finished = False

        while not finished:
            clock.tick(FPS)
            self.screen.blit(self.game_back, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    self.end_game()
                else:
                    self.hero_1.event_checking_hero(event)
                    self.hero_2.event_checking_hero(event)
            self.hero_sprites.update(platforms, characters, self.screen)
            for p in platforms:
                p.update(self.screen)
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                self.pause()
            pygame.display.update()

    def end_game(self):
        all_sprites.empty()
        self.hero_sprites.empty()
        platforms.clear()
        characters.clear()
        pygame.quit()
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        background_music()
        MainMenu(screen, menu_background, lambda: start_game()).show()

    def change_background(self, rep):
        files = glob.glob(rep + sep + '*')
        pos = files.index(self.background_image)
        image = files[(pos+1) % len(files)]
        while not image.lower().endswith(('.png', '.jpg')):
            pos = (pos + 1) % len(files)
            image = files[(pos + 1) % len(files)]
        self.background_image = files[(pos + 1) % len(files)]

        pygame.time.delay(100)


def start_game():
    game = Game()
    game.start_game()

