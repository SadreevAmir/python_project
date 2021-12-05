import pygame
from constants import *
from game import start_game
import re


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

        else:
            color = self.inactive_color
        font = pygame.font.Font(FONT, size)
        text = font.render(self.text, True, color)
        self.screen.blit(text, (button_rect.centerx-text.get_width()/2, button_rect.centery-text.get_height()/2))


class Menu:
    def __init__(self, screen, background_image):
        self.screen = screen
        background = pygame.image.load(background_image).convert()
        self.background = pygame.transform.scale(background, self.screen.get_size())
        self.show_flag = True
        self.buttons = []

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        num = len(self.buttons)
        pos = (num-0.5)/2
        for button in self.buttons:
            button.draw(self.screen.get_width()/2, self.screen.get_height()*(pos/num))
            pos += num/9

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
            self.screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_flag = False

            self.draw()
            self.press()
            pygame.display.update()


class MainMenu(Menu):
    def __init__(self, screen, background_image):
        super(MainMenu, self).__init__(screen, background_image)

        self.start_button = Button(self.screen, 'play', YELLOW, PURPLE, start_game)
        self.settings_button = Button(self.screen, 'settings', YELLOW, BROWN,
                                      lambda: SettingsMenu(self.screen, background_image).show())
        self.quit_button = Button(self.screen, 'quit', YELLOW, RED, quit)

        self.buttons = [self.start_button, self.settings_button, self.quit_button]


class SettingsMenu(Menu):
    def __init__(self, screen, background_image):
        super(SettingsMenu, self).__init__(screen, background_image)

        self.back_button = Button(self.screen, 'back', YELLOW, PURPLE,
                                  lambda: MainMenu(self.screen, background_image).show())
        self.change_background = Button(self.screen, 'change background', YELLOW, BLUE, change_background,
                                        lambda: SettingsMenu(self.screen, menu_background).show())

        self.buttons = [self.back_button, self.change_background]


def change_background():
    global menu_background
    num = re.findall('\d+', menu_background)[0]
    if num.isdigit():
        pos = menu_background.find(num)
        num = int(num)
        chap1 = menu_background[0:pos]
        chap2 = menu_background[pos+1:len(menu_background)]
        menu_background = chap1 + str(num % 5+1) + chap2

