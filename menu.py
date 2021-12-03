import pygame
from constants import *
from game import start_game


class Button:
    def __init__(self, screen, text, inactive_color, active_color, action=lambda: None):
        self.screen = screen
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text = text
        self.action = action
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


class MainMenu(Menu):
    def __init__(self, screen, background_image):
        super(MainMenu, self).__init__(screen, background_image)

        self.start_button = Button(self.screen, 'start', YELLOW, PURPLE, start_game)
        self.settings_button = Button(self.screen, 'settings', YELLOW, BROWN)
        self.quit_button = Button(self.screen, 'quit', YELLOW, RED, quit)

        self.buttons = [self.start_button, self.settings_button, self.quit_button]


def show_main_menu(screen):
    main_menu = MainMenu(screen, main_menu_background)
    clock = pygame.time.Clock()
    show = True

    while show:
        clock.tick(30)
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False

        main_menu.draw()
        main_menu.press()
        pygame.display.update()


