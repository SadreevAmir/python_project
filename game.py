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
        num_field = create_field()
        create_platforms(num_field)
        self.hero_sprites.add(self.hero_1, self.hero_2)
        self.finish_text = ''

    def start_game(self):
        pygame.init()
        time = 0
        clock = pygame.time.Clock()
        finished = False
        finished1 = False
        while not finished:
            clock.tick(FPS)
            self.screen.blit(self.game_back, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                else:
                    self.hero_1.event_checking_hero(event)
                    self.hero_2.event_checking_hero(event)
            self.hero_sprites.update(platforms, characters, self.screen)
            for p in platforms:
                p.update(self.screen)
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                self.pause()

            if len(characters) < 2:
                if len(characters) == 0:
                    self.finish_text = 'draw'
                elif self.hero_1 not in characters:
                    self.finish_text = 'winner player 1'
                else:
                    self.finish_text = 'winner player 2'
                finished1 = True
                if time == 0:
                    time = pygame.time.get_ticks()
            pygame.display.update()
            if finished1 and pygame.time.get_ticks()-time > 1000:
                finished = True
        self.won_game()

    def pause(self):
        pause = PauseMenu(self.screen, self.background_image, lambda: MainMenu(self.screen, menu_background,
                                                                               lambda: Game().start_game()).show(),
                          lambda: self.end_game(), lambda: self.restart_game())
        pause.show()
        self.background_image = pause.background_image
        self.change_background()

    def restart_game(self):
        all_sprites.empty()
        self.hero_sprites.empty()
        platforms.clear()
        characters.clear()
        start_game()

    def end_game(self):
        all_sprites.empty()
        self.hero_sprites.empty()
        platforms.clear()
        characters.clear()
        pygame.quit()
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        background_music()
        print(self.finish_text)
        MainMenu(screen, menu_background, lambda: start_game()).show()

    def won_game(self):
        if self.finish_text != '':
            font = pygame.font.Font(FONT, SIZE)
            text = font.render(self.finish_text, True, VIOLET)
            text_rect = text.get_rect(center=(WIDTH/2, 0.34*HEIGHT))
            self.screen.blit(text, (text_rect.centerx-text_rect.width/2, text_rect.y))

        pygame.image.save(self.screen, 'screenshot.png')
        FinishMenu(self.screen, 'screenshot.png', lambda: self.restart_game(), lambda: self.end_game(),
                   self.finish_text).show()

    def change_background(self):
        game_back = pygame.image.load(self.background_image).convert()
        self.game_back = pygame.transform.scale(game_back, self.screen.get_size())


def start_game():
    game = Game()
    game.start_game()
