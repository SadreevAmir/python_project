import glob
from constants import *
from music import switch_music, switch_sound_effects


class Button:
    """Кнопка, совершающая передаваемые действия при нажатии. Размер шрифта берется из модуля constants.py,
    шрифт - из файла Current-Regular.ttf

    Attributes
    _________
        screen : поверхность, на которой отображается кнопка\n
        inactive_color :  цвет кнопки в начальном состоянии\n
        active_color : цвет кнопки при наведении курсора\n
        text : текст кнопки\n
        action : первое действие кнопки\n
        action2 : второе действие кнопки\n
        pressed : флаг, сообщающий о нажатии на кнопку

    Methods
    _______
        draw()
            отрисовывает кнопку

    """

    def __init__(self, screen: pygame.Surface, text: str, inactive_color: list, active_color: list, action=lambda: None,
                 action2=lambda: None):
        """
        :param screen : поверхность, на которой отображается кнопка\n
        :param inactive_color :  цвет кнопки в начальном состоянии\n
        :param active_color : цвет кнопки при наведении курсора\n
        :param text: текст кнопки\n
        :param action: первое действие кнопки\n
        :param action2: второе действие кнопки\n
        """

        self.screen = screen
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text = text
        self.action = action
        self.action2 = action2
        self.pressed = False

    def draw(self, x: float, y: float):
        """Метод для отрисовки кнопки.

        :param x: координата центра кнпоки по горизонтали\n
        :param y: ккордината центра кнопки по вертикали\n
        :return: None
        """

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
        self.screen.blit(text,
                         (button_rect.centerx - text.get_width() / 2, button_rect.centery - text.get_height() / 2))


class Menu:
    """Меню, на котором находятся кнопки

    Attributes
    __________
    screen : поверхность, на которой отображается меню\n
    background_image: ссылка на изображение фона меню\n
    background: фон меню\n
    show_flag: флаг, сообщающий об отображении меню\n
    buttons: список всех кнопок

    Methods
    _______
    draw()
        отрисовывает меню вместе с кнопками
    press()
        обрабатывает нажатие на кнопки
    show()
        отображает меню
    change_background(rep)
        меняет фон меню
    """

    def __init__(self, screen: pygame.Surface, background_image: str):
        """
        :param screen: поверхность, на которой отображается меню
        :param background_image: ссылка на изображения фона
        """

        self.screen = screen
        self.background_image = background_image
        background = pygame.image.load(self.background_image).convert()
        self.background = pygame.transform.scale(background, self.screen.get_size())
        self.show_flag = True
        self.buttons = []

    def draw(self):
        """Метод для отрисовки фона и кнопок меню

        :return: None
        """

        self.screen.blit(self.background, (0, 0))
        num = len(self.buttons)
        pos = 1/2 - num/25
        for button in self.buttons:
            button.draw(self.screen.get_width()/2, self.screen.get_height()*pos)
            pos += 1/9

    def press(self):
        """Метод для обработки нажатия на кнопки меню

        :return: None
        """

        for button in self.buttons:
            if button.pressed:
                self.show_flag = False
                button.action()
                button.action2()

    def show(self):
        """Метод для отображения меню

        :return: None
        """

        clock = pygame.time.Clock()

        while self.show_flag:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if type(self) == MainMenu:
                        quit()
                    self.show_flag = False
            self.draw()
            self.press()
            pygame.display.update()

    def change_background(self, rep: str):
        """Метод для смены фона меню

        :param rep: ссылка на папку, в которой находятся фоны
        :return: None
        """

        files = glob.glob(rep + sep + '*')
        pos = files.index(self.background_image)
        image = files[(pos+1) % len(files)]
        while not image.lower().endswith(('.png', '.jpg')):
            pos = (pos + 1) % len(files)
            image = files[(pos + 1) % len(files)]
        self.background_image = files[(pos + 1) % len(files)]


class MainMenu(Menu):
    """Главное меню при запуске игры.

    Attributes
    __________
    start_button : кнопка, запускающая саму игру\n
    settings_button: кнопка, открывающая настройки\n
    quit_button: кнопка, закрывающая игру\n
    buttons: список всех кнопок
    """

    def __init__(self, screen, background_image, start_function=lambda: None):
        """
        :param screen: поверхность, на которой отображается меню
        :param background_image: ссылка на изображения фона
        :param start_function : функция, происходящая при нажатии на кнопку начала игры
        """

        super(MainMenu, self).__init__(screen, background_image)

        self.start_button = Button(self.screen, 'play', YELLOW, PURPLE, lambda: start_function())
        self.settings_button = Button(self.screen, 'settings', YELLOW, BROWN,
                                      lambda: SettingsMenu(self.screen, self.background_image,
                                                           lambda: start_function()).show())
        self.quit_button = Button(self.screen, 'quit', YELLOW, RED, quit)

        self.buttons = [self.start_button, self.settings_button, self.quit_button]


class SettingsMenu(Menu):
    """Меню настроек

    Attributes
    __________
    back_button : кнопка, возвращающее в главное меню\n
    change_background_button : кнопка, меняющая фон\n
    music_button : кнопка, включающая/выключающая воспроизведение музыки\n
    sound_effects_button : кнопка, включающая/выключающая воспроизведение звуковых эффектов\n
    buttons : список всех кнопок
    """

    def __init__(self, screen, background_image, start_function=lambda: None):
        """
        :param screen: поверхность, на которой отображается меню
        :param background_image: ссылка на изображения фона
        :param start_function : функция, происходящая при нажатии на кнопку начала игры
        """

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
    """Меню паузы во время игры

    Attributes
    __________
    resume_button : кнопка, продолжающая игру\n
    restart_button : кнопка, перезапускающая игру\n
    quit_button : кнопка, возвращающая в главное меню\n
    change_background_button : кнопка, меняющая фон\n
    music_button : кнопка, включающая/выключающая воспроизведение музыки\n
    sound_effects_button : кнопка, включающая/выключающая воспроизведение звуковых эффектов\n
    buttons : список всех кнопок
    """

    def __init__(self, screen, background_image, quit_function=lambda: None, restart_function=lambda: None):
        """
        :param screen: поверхность, на которой отображается меню
        :param background_image: ссылка на изображение фона
        :param quit_function: функция, перезапускающая игру
        :param restart_function: функция, перезапускающая игру
        """

        super(PauseMenu, self).__init__(screen, background_image)

        self.resume_button = Button(self.screen, 'resume', YELLOW, PURPLE)

        self.restart_button = Button(self.screen, 'restart', YELLOW, RED,
                                     lambda: restart_function())
        self.quit_button = Button(self.screen, 'menu', YELLOW, RED,
                                  lambda: quit_function())

        mus_flag = 'off'
        effects_flag = 'off'
        if pygame.mixer.Channel(0).get_volume():
            mus_flag = 'on'
        if pygame.mixer.Channel(1).get_volume():
            effects_flag = 'on'

        self.music_button = Button(self.screen, 'music: ' + mus_flag, YELLOW, PURPLE, lambda: switch_music(),
                                   lambda: PauseMenu(self.screen, self.background_image,
                                                     lambda: quit_function()).show())
        self.sound_effects_button = Button(self.screen, 'sound effects: ' + effects_flag, YELLOW, PURPLE,
                                           lambda: switch_sound_effects(),
                                           lambda: PauseMenu(self.screen, self.background_image,
                                                             lambda: quit_function()).show())
        self.change_background_button = Button(self.screen, 'change background', YELLOW, BLUE,
                                               lambda: self.change_background('game_back'),
                                               lambda: PauseMenu(self.screen, self.background_image,
                                                                 lambda: quit_function()).show())

        self.buttons = [self.resume_button, self.restart_button, self.change_background_button, self.music_button,
                        self.sound_effects_button, self.quit_button]


class FinishMenu(Menu):
    """Финальное меню, открывающееся при завершении игры или ее закрытии

    Attributes
    __________
    restart_button : кнопка, перезапускающая игру\n
    menu_button :  кнопка, возвращающая в главное меню\n
    quit_button : кнопка, закрывающая игру\n
    empty_button : бездействующая кнопка, используемая для смещения
    остальных при наличии дополнительного текста об итоге игры
    """

    def __init__(self, screen, background_image, start_function=lambda: None, quit_function=lambda: None, result=None):
        super(FinishMenu, self).__init__(screen, background_image)

        self.restart_button = Button(self.screen, 'restart', YELLOW, PURPLE,
                                     lambda: start_function())

        self.menu_button = Button(self.screen, 'menu', YELLOW, RED,
                                  lambda: quit_function())

        self.quit_button = Button(self.screen, 'quit', YELLOW, RED, quit)
        self.buttons = [self.restart_button, self.menu_button, self.quit_button]
        if result != '':
            self.empty_button = Button(self.screen, '', YELLOW, PURPLE)
            self.buttons.insert(0, self.empty_button)
