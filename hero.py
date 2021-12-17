from pygame.constants import K_SPACE, MOUSEBUTTONDOWN
from bullet import Bullet
from get_sprites import Sprites
from constants import *
from music import punch_music, fireball_music


class Hero(pygame.sprite.Sprite):
    """
    Класс Hero используется для создания персонажа.
    Основное применение - основа для содания идивидуального героя.

    Note:
        В классах наследующихся от данного для отображения анимации атаки требуется дополнительное описание метода
        special_attack(), который возврашает две координаты левого верхнего угла картинки.

        Также требуется описание метода обродатывающего события клавиатуры и мыши (wasd) тем или иным способом.
        Ключевым является преобразование этих данных в соответствующие атрибуты класса.

    Attributes
        image - переменная типа pygame.Surface содержающая изображение персонажа на данный момент.
        rect - хитбокс персонажа.
        attack_rect - зона поражения мили атаки.
        Далее ислользуется ряд объектов класа get_sprites обслуживающих анимацию соответствующих действий.
        Также используется переменные состояния и фаз персонажа.
    """
    def __init__(self, start_x, start_y, hero_size=(HERO_SiZE_X, HERO_SIZE_Y)):
        """
        Конструкор класса
        :param start_x: начальное положение
        :param start_y: начальное положение
        :param hero_size: характерные размеры персонажа которые определяют хитбокс персонажа
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(hero_size)
        self.run_sprite = Sprites(run_sprite1)
        self.stay_sprite = Sprites(stay_sprite1)
        self.milli_attack_sprite = Sprites(milli_attack_sprite1, 40, 2)
        self.stun_sprite = Sprites(stun_sprite1, 60)
        self.jump_sprite = Sprites(jump_sprite1)
        self.death_sprite = Sprites(death_sprite1)
        self.rect = self.image.get_rect()
        self.attack_rect = pygame.Surface((hero_size[0], 2*hero_size[1])).get_rect()
        self.rect.center = (start_x, start_y)
        self.onGround = False
        self.left, self.right, self.jump, self.milli_attack, self.FACING = False, False, False, False, False
        self.Vx = 0
        self.Vy = 0
        self.kick_speed = 0
        self.attack = False
        self.stun = False
        self.shooting = False
        self.power_bar = Sprites('s_pow_bar_strip10.png', 2000, 1, True)
        self.power_bar_rect = self.power_bar.sprite.get_rect()
        self.power_bar.currentFrame = 4
        self.power = 4
        self.health_bar = Sprites('S_health_bars.png', 20000, 1, True)
        self.health_bar_rect = self.health_bar.sprite.get_rect()
        self.health_bar.currentFrame = 9
        self.health_bar.get_sprite()
        self.lives = self.health_bar.currentFrame
        self.death = False

    def update(self, platform, screen):
        """
        Главный метод класса выполняющийся циклически.
        :param platform: список объектов, с которыми проверяются столкновения героя
        :param screen: поверхность где рисуем персонажа
        """
        if not self.death:
            self.event_handling()
            self.power = self.power_bar.currentFrame
            self.hitcheck()
            self.faze_checking()
            self.health_bar.currentFrame = self.lives
            y, x = self.animate()
            screen.blit(self.power_bar.sprite, self.power_bar_rect.topleft)
        else:
            self.onGround = False
            y, x = self.death_animate()
        self.movement(platform)
        screen.blit(self.image, (x, y))
        screen.blit(self.health_bar.sprite, self.health_bar_rect.topleft)
        self.reset()

    def faze_checking(self):
        """
        Проверяет фазы персонажа и отвечает за расход энергии по совместительству (выстрелы и вход в атаку)
        """
        if self.lives > 0:
            if not self.attack and self.milli_attack and self.power > 3:
                self.attack = True
                punch_music()
                self.power_bar.currentFrame -= 4
            elif self.shooting and self.power > 1:
                self.shot()
                self.power_bar.currentFrame -= 2
        else:
            self.death = True
            self.lives = 0
            characters.remove(self)

    def hitcheck(self):
        """
        Проверка попадания в героя чужого 'кулака' (пересечение с чужой зоной поражения)
        Также описывает последствия попадания (стан и отскок) (снимает хп)
        """
        for obj in characters:
            if obj.attack and not (self is obj):
                if self.rect.colliderect(obj.attack_rect):
                    if not self.stun:
                        self.lives -= 1
                        if obj.FACING:
                            self.FACING = False
                            self.kick_speed = -10
                        else:
                            self.FACING = True
                            self.kick_speed = 10
                        self.Vy -= 3
                        self.stun = True

    def shot(self):
        """
        Создает новый объект класса bullet в результате выстрела
        """
        all_sprites.add(Bullet(self, self.rect.centerx, self.rect.centery))
        fireball_music()
        self.shooting = False

    def animate(self):
        """
        Основной метод отвечающий за анимацию всего связанного с героем
        и проверки какую имено анимацию следует использовать(полоска здоровья и энергии, и сам персонаж)
        Также выводит из состаяния атаки (в методе special_attack это необходимо прописать)
        :return: Положение верхнего левого угла картинки
        """
        if self.power_bar.currentFrame < self.power_bar.numbers_image - 1:
            self.power_bar.get_sprite()
        else:
            self.power_bar.last_update = pygame.time.get_ticks()
        if self.health_bar.currentFrame < self.health_bar.numbers_image - 1:
            self.health_bar.get_sprite()
            self.lives = self.health_bar.currentFrame
        else:
            self.health_bar.last_update = pygame.time.get_ticks()
        self.health_bar_rect.midbottom = self.rect.midtop
        self.power_bar_rect.bottomleft = self.health_bar_rect.topleft
        if self.stun:
            self.image = self.stun_sprite.get_sprite(self.FACING)
            if self.stun_sprite.currentFrame == self.stun_sprite.numbers_image - 1:
                self.stun = False
            return self.rect.y, self.rect.x
        elif self.attack:
            return self.special_attack()
        elif (self.right or self.left) and (not self.right or not self.left):
            self.image = self.run_sprite.get_sprite(self.FACING)
            return self.rect.y, self.rect.x
        else:
            self.image = self.stay_sprite.get_sprite(self.FACING)
            return self.rect.y, self.rect.x

    def death_animate(self):
        """
        Специальная анимация при смерти. Доп метод служит для уменьшения проверок
        :return: Положение верхнего левого угла картинки
        """
        self.health_bar_rect.midbottom = self.rect.midtop
        # self.power_bar_rect.bottomleft = self.health_bar_rect.topleft
        self.image = self.death_sprite.get_sprite()
        return self.rect.y, self.rect.x

    def special_attack(self):
        ...

    def event_handling(self):
        """
        обработка событий уже считанным с клавиатуры и после этого присвоение пременной
        onGround значения False для коректной проверки столкновений
        """
        if not self.stun:
            if self.right:
                self.Vx += MOVE_SPEED
            if self.left:
                self.Vx -= MOVE_SPEED
            if self.onGround and self.jump:
                self.Vy = -JUMP_POWER
                self.onGround = False
        self.onGround = False

    def collision_x(self, platform):
        """
        проверка столнконовения героя с препятствиями(или другими героями) по горизонтали
        :param platform: объекты, с которыми проверяются столкновения
        """
        for p in platform:
            if pygame.sprite.collide_rect(self, p):

                if self.Vx > 0:
                    self.rect.right = p.rect.left

                if self.Vx < 0:
                    self.rect.left = p.rect.right

        if self in characters:
            for p in characters:
                if pygame.sprite.collide_rect(self, p) and not (self is p):

                    if self.Vx > 0:
                        self.rect.right = p.rect.left

                    if self.Vx < 0:
                        self.rect.left = p.rect.right

    def collision_y(self, platform):
        """
        проверка столнконовения героя с препятствиями(или другими героями) по вертикали
        :param platform: объекты, с которыми проверяются столкновения
        """
        for p in platform:
            if pygame.sprite.collide_rect(self, p):
                if self.Vy > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.Vy = 0

                if self.Vy < 0:
                    self.rect.top = p.rect.bottom
                    self.Vy = 0

        if self in characters:
            for p in characters:
                if pygame.sprite.collide_rect(self, p) and not (self is p):
                    if self.Vy > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.Vy = 0

                    if self.Vy < 0:
                        self.rect.top = p.rect.bottom
                        self.Vy = 0

    def movement(self, platform):
        """
        Перемешения персонажа
        :param platform: транзит параметра для collision
        """
        self.Vx += self.kick_speed
        self.rect.x += self.Vx
        self.collision_x(platform)
        if not self.onGround:
            self.Vy += GRAVITY
            self.rect.y += self.Vy
            self.collision_y(platform)

    def reset(self):
        """
        Сброс значение переменных или их откат
        """
        self.Vx = 0
        self.milli_attack = self.shooting = False
        if self.kick_speed > 0:
            self.kick_speed -= 1
        elif self.kick_speed < 0:
            self.kick_speed += 1


class Hero1(Hero):
    """
    Первый герой(типо монстрик)
    """
    def __init__(self, start_x, start_y):
        super(Hero1, self).__init__(start_x, start_y)
        self.jump_sprite = Sprites(jump_sprite1)
        self.run_sprite = Sprites(run_sprite1)
        self.stay_sprite = Sprites(stay_sprite1)
        self.milli_attack_sprite = Sprites(milli_attack_sprite1, 40, 2)
        self.stun_sprite = Sprites(stun_sprite1, 60)
        self.death_sprite = Sprites(death_sprite1)

    def event_checking_hero(self, event):
        """
        обработка событий с манипуляторов
        :param event: объект события pygame
        """
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.shooting = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == a_key_rus:
                self.left, self.FACING = True, True
            elif event.key == pygame.K_d or event.key == d_key_rus:
                self.right, self.FACING = True, False
            elif event.key == pygame.K_w or event.key == w_key_rus:
                self.jump = True
            elif event.key == pygame.K_e or event.key == e_key_rus:
                self.shooting = True
            elif event.key == pygame.K_q or event.key == q_key_rus or event.key == K_SPACE:
                self.milli_attack = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == a_key_rus:
                self.left = False
            elif event.key == pygame.K_d or event.key == d_key_rus:
                self.right = False
            elif event.key == pygame.K_w or event.key == w_key_rus:
                self.jump = False

    def special_attack(self):
        """
        атака анимация
        :return: верхний левый угол
        """
        self.image = self.milli_attack_sprite.get_sprite(self.FACING)
        if self.milli_attack_sprite.currentFrame == self.milli_attack_sprite.numbers_image - 1:
            self.attack = False
        if self.FACING:
            self.attack_rect.bottomright = self.rect.bottomleft
            return 2 * self.rect.y - self.rect.bottom, 2 * self.rect.x - self.rect.right
        else:
            self.attack_rect.bottomleft = self.rect.bottomright
            return 2 * self.rect.y - self.rect.bottom, self.rect.x


class Hero2(Hero):
    """
    Второй герой (сейчас используется нарисованная Сардором версия спрайтов)
    """
    def __init__(self, start_x, start_y):
        super(Hero2, self).__init__(start_x, start_y)
        self.jump_sprite = Sprites(jump_sprite3)
        self.run_sprite = Sprites(run_sprite3)
        self.stay_sprite = Sprites(stay_sprite3)
        self.milli_attack_sprite = Sprites(milli_attack_sprite3, 40, 1)
        self.stun_sprite = Sprites(stun_sprite3, 60)
        self.death_sprite = Sprites(death_sprite3, 50)

    def event_checking_hero(self, event):
        """
        обработка событий с манипуляторов
        :param event: объект события pygame
        """
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                self.shooting = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left, self.FACING = True, True
            elif event.key == pygame.K_RIGHT:
                self.right, self.FACING = True, False
            elif event.key == pygame.K_UP:
                self.jump = True
            elif event.key == pygame.K_SLASH or event.key == slash_rus:
                self.milli_attack = True
            elif event.key == pygame.K_COMMA or event.key == comma_key_rus:
                self.shooting = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = False
            elif event.key == pygame.K_RIGHT:
                self.right = False
            elif event.key == pygame.K_UP:
                self.jump = False

    def special_attack(self):
        """
        атака анимация
        :return: верхний левый угол
        """
        self.image = self.milli_attack_sprite.get_sprite(self.FACING)
        if self.milli_attack_sprite.currentFrame == self.milli_attack_sprite.numbers_image - 1:
            self.attack = False
        if self.FACING:
            self.attack_rect.bottomright = self.rect.bottomleft
            return self.rect.y, self.rect.x
        else:
            self.attack_rect.bottomleft = self.rect.bottomright
            return self.rect.y, self.rect.x
