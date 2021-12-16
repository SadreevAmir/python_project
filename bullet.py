from get_sprites import *


class Bullet(pygame.sprite.Sprite):
    """
    Класс Bullet использующийся для описания снаряда

    Attributes:
        image - переменная типа pygame.Surface содержающая изображение фаербола.
        rect - хитбокс снаряда.
    """
    def __init__(self, kind, x, y):
        """
        Конструктор класса
        :param kind: объект который выстрелил
        :param x: начальное положение
        :param y: начальное положение
        """
        pygame.sprite.Sprite.__init__(self)
        self.kind = kind
        self.image = pygame.image.load('sprites/Fireball.png')
        self.image = pygame.transform.scale(
            self.image, (HERO_SIZE_Y//2, HERO_SIZE_Y//2))
        self.image = pygame.transform.flip(self.image, kind.FACING, False)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        if self.kind.FACING:
            self.speedy = -10
        else:
            self.speedy = 10

    def update(self, platform, screen):
        """
        Главный метод класса выполняющийся циклически.
        :param platform: список объектов, с которыми проверяются столкновения героя
        :param screen: поверхность где рисуем фаерболл
        """
        self.rect.x += self.speedy
        screen.blit(self.image, self.rect.topleft)
        self.collision(platform)

    def collision(self, platform):
        """
        Столкновение с препятствиями и поподание в героев
        :param platform: препятствия
        """
        for p in platform:
            if self.rect.colliderect(p) and not (self.kind is p):
                p.lives -= 1
                if p.lives == 0:
                    platform.remove(p)
                self.kill()
        for kind in characters:
            if self.rect.colliderect(kind) and not (kind is self.kind):
                kind.lives -= 1
                self.kill()
