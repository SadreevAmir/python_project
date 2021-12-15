from constants import *
from hero import Hero1, Hero2
from field import create_field
from platforms import create_platforms
from menu import MainMenu, PauseMenu, FinishMenu
from music2 import background_music


class Game:
    """Класс игры. При инициализации создает поверхность, персонажей и поле

    Attributes
    __________
    screen : поверхность на которой отображается игра\n
    hero_sprites : список спрайтов, участвующих в игре\n
    hero_1 : спрайт первого игрока\n
    hero_2 : спрайт второго игрока\n
    background_image : ссылка на изображение фона\n
    game_back : изображение фона\n
    finish_text : текст, сообщающий об итогах игры\n

    Methods
    _______
    start_game()
        начинает игру
    pause()
        приостанавливает игру, отображает меню PauseMenu
    restart_game()
        перезапускает игру
    end_game()
        завершает игру, очищает поле, открывает главное меню
    won_game()
        выводит на экран итоги игры при их наличии, отображает меню FinishMenu
    change_background()
        меняет фон в игре
    """

    def __init__(self, background: str):
        """
        :param background: ссылка на изображение фона игры
        """
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.hero_sprites = all_sprites
        self.hero_1 = Hero1(HERO_X, HERO_Y)
        self.hero_2 = Hero2(WIDTH - HERO_X, HEIGHT - HERO_Y)
        characters.append(self.hero_1)
        characters.append(self.hero_2)
        self.background_image = background
        game_back = pygame.image.load(self.background_image).convert()
        self.game_back = pygame.transform.scale(game_back, self.screen.get_size())
        num_field = create_field()
        create_platforms(num_field)
        self.hero_sprites.add(self.hero_1, self.hero_2)
        self.finish_text = ''

    def start_game(self):
        """Начинает игру. Она длится до ее закрытия или победы одного из игроков (или ничьи).
        Также заносит итоги игры при их наличии в finish_text.

        :return: None
        """

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
        """Приостанавливает игру и открывает меню Паузы

        :return: None
        """

        pause = PauseMenu(self.screen, self.background_image, lambda: self.end_game(), lambda: self.restart_game())
        pause.show()
        self.background_image = pause.background_image
        self.change_background()

    def restart_game(self):
        """Перезапускает игру. При этом очищается поле и списки с персонажами исходной игры.

        :return: None
        """
        all_sprites.empty()
        self.hero_sprites.empty()
        platforms.clear()
        characters.clear()
        start_game(self.background_image)

    def end_game(self):
        """Завершает игру. Очищает поле и все списки, возвращает в главное меню.
        Начинает воспроизведние фоновой музыки сначала

        :return: None
        """
        all_sprites.empty()
        self.hero_sprites.empty()
        platforms.clear()
        characters.clear()
        background_music()
        MainMenu(self.screen, menu_background, lambda: start_game(self.background_image)).show()

    def won_game(self):
        """Отображает итоги игры при их наличии и открывает Финальное меню.
         Сохраняет последний кадр игры в screenshot.png

        :return: None
        """
        if self.finish_text != '':
            font = pygame.font.Font(FONT, SIZE)
            text = font.render(self.finish_text, True, VIOLET)
            text_rect = text.get_rect(center=(WIDTH/2, 0.34*HEIGHT))
            self.screen.blit(text, (text_rect.centerx-text_rect.width/2, text_rect.y))

        pygame.image.save(self.screen, 'screenshot.png')
        FinishMenu(self.screen, 'screenshot.png', lambda: self.restart_game(), lambda: self.end_game(),
                   self.finish_text).show()

    def change_background(self):
        """Меняет фон игры.

        :return: None
        """
        game_back = pygame.image.load(self.background_image).convert()
        self.game_back = pygame.transform.scale(game_back, self.screen.get_size())


def start_game(background: str):
    """Инициализирует игру и запускает ее.

    :param background: ссылка на изображение фона игры
    :return: None
    """
    game = Game(background)
    game.start_game()
