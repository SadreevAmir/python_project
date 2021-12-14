import glob
from music2 import *
import pygame
from constants import *
import os
sep = os.path.sep


class Button:
    def __init__(self, screen, text, inactive_color, active_color, action=lambda: None, action2=lambda: None):
        self.screen = screen
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text = text
        self.action = action
        self.action2 = action2
        self.pressed = False

    def draw(self, x, y):
        self.pressed = False
        size = SIZE
        color = self.inactive_color
        font = pygame.font.Font(FONT, size)
        text = font.render(self.text, True, color)
        button_rect = text.get_rect(center=(x, y))
        mouse = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse):
            color = self.active_color
            size += 10
            if pygame.mouse.get_pressed()[0] == 1:
                self.pressed = True
                pygame.time.delay(50)

        else:
            color = self.inactive_color
        font = pygame.font.Font(FONT, size)
        text = font.render(self.text, True, color)
        self.screen.blit(text, (button_rect.centerx-text.get_width()/2, button_rect.centery-text.get_height()/2))


class Menu:
    def __init__(self, screen, background_image):
        # screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen = screen
        self.background_image = background_image
        background = pygame.image.load(self.background_image).convert()
        self.background = pygame.transform.scale(background, self.screen.get_size())
        self.show_flag = True
        self.buttons = []

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        num = len(self.buttons)
        pos = 1/2 - num/25
        for button in self.buttons:
            button.draw(self.screen.get_width()/2, self.screen.get_height()*pos)
            pos += 1/9

    def press(self):
        for button in self.buttons:
            if button.pressed:
                button.action()
                self.show_flag = False
                button.action2()

    def show(self):
        clock = pygame.time.Clock()

        while self.show_flag:
            clock.tick(30)
            # self.screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if type(self) == MainMenu:
                        quit()
                    self.show_flag = False

            self.draw()
            self.press()
            pygame.display.update()

    def change_background(self, rep):
        files = glob.glob(rep + sep + '*')
        pos = files.index(self.background_image)
        image = files[(pos+1) % len(files)]
        while not image.lower().endswith(('.png', '.jpg')):
            pos = (pos + 1) % len(files)
            image = files[(pos + 1) % len(files)]
        self.background_image = files[(pos + 1) % len(files)]


class MainMenu(Menu):
    def __init__(self, screen, background_image, start_function=lambda: None):
        super(MainMenu, self).__init__(screen, background_image)

        self.start_button = Button(self.screen, 'play', YELLOW, PURPLE, lambda: start_function())
        self.settings_button = Button(self.screen, 'settings', YELLOW, BROWN,
                                      lambda: SettingsMenu(self.screen, self.background_image,
                                                           lambda: start_function()).show())
        self.quit_button = Button(self.screen, 'quit', YELLOW, RED, quit)

        self.buttons = [self.start_button, self.settings_button, self.quit_button]


class SettingsMenu(Menu):
    def __init__(self, screen, background_image, start_function=lambda: None):
        super(SettingsMenu, self).__init__(screen, background_image)

        self.back_button = Button(self.screen, 'back', YELLOW, PURPLE,
                                  lambda: MainMenu(self.screen, self.background_image, lambda: start_function()).show())
        self.change_background_button = Button(self.screen, 'change background', YELLOW, BLUE,
                                               lambda: self.change_background('menu_back'),
                                               lambda: SettingsMenu(self.screen, self.background_image,
                                                                    lambda: start_function()).show())
        mus_flag = 'off'
        effects_flag = 'off'
        if pygame.mixer.Channel(0).get_volume():
            mus_flag = 'on'
        if pygame.mixer.Channel(1).get_volume():
            effects_flag = 'on'

        self.music_button = Button(self.screen, 'music: ' + mus_flag, YELLOW, PURPLE, lambda: switch_music(),
                                   lambda: SettingsMenu(self.screen, self.background_image,
                                                        lambda: start_function()).show())
        self.sound_effects_button = Button(self.screen, 'sound effects: ' + effects_flag, YELLOW, PURPLE,
                                           lambda: switch_sound_effects(),
                                           lambda: SettingsMenu(self.screen,
                                                                self.background_image, lambda: start_function()).show())
        self.buttons = [self.back_button, self.change_background_button, self.music_button, self.sound_effects_button]


class PauseMenu(Menu):
    def __init__(self, screen, background_image, start_function=lambda: None, quit_function=lambda: None):
        super(PauseMenu, self).__init__(screen, background_image)
        self.background_image = background_image

        self.pause = True
        self.continue_button = Button(self.screen, 'continue', YELLOW, PURPLE)

        self.quit_button = Button(self.screen, 'quit', YELLOW, RED,
                                  lambda: quit_function())

        mus_flag = 'off'
        effects_flag = 'off'
        if pygame.mixer.Channel(0).get_volume():
            mus_flag = 'on'
        if pygame.mixer.Channel(1).get_volume():
            effects_flag = 'on'

        self.music_button = Button(self.screen, 'music: ' + mus_flag, YELLOW, PURPLE, lambda: switch_music(),
                                   lambda: PauseMenu(self.screen, self.background_image,
                                                     lambda: start_function(), lambda: quit_function()).show())
        self.sound_effects_button = Button(self.screen, 'sound effects: ' + effects_flag, YELLOW, PURPLE,
                                           lambda: switch_sound_effects(),
                                           lambda: PauseMenu(self.screen, self.background_image,
                                                             lambda: start_function(), lambda: quit_function()).show())
        self.change_background_button = Button(self.screen, 'change background', YELLOW, BLUE,
                                               lambda: self.change_background('game_back'),
                                               lambda: PauseMenu(self.screen, self.background_image,
                                                                 lambda: start_function(),
                                                                 lambda: quit_function()).show())

        self.buttons = [self.continue_button, self.music_button, self.sound_effects_button,
                        self.change_background_button, self.quit_button]
