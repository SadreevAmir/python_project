from hero import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, a, b):
        """
        color - цвет
        плаформы
        image - поверзность
        изображением
        плтформы
        rect - прямоугольник, представляющий
        платформу
        lives - количество жтзней у платформы
        """
        pygame.sprite.Sprite.__init__(self)
        self.color = DARK_GREEN
        self.image = pygame.Surface((a, b))
        self.rect = pygame.Rect(x, y, a, b)
        self.lives = PLATFORMS_LIVES
        self.hit = False

    def hit_check(self, character):
        """проверка удара персонажем"""
        for obj in character:
            if obj.attack:
                if self.rect.colliderect(obj.attack_rect):
                    if not self.hit:
                        self.hit = True
                        self.lives -= 1
                    if self.lives == 0 or self.lives == -1:
                        platforms.remove(self)

                    self.hit = False

    def update(self, screen):
        """обновление
         платформ"""
        if 0 <= self.lives < PLATFORMS_LIVES:
            self.color = [RED[0] * (1 - self.lives / PLATFORMS_LIVES), 0, 0]
        self.image.fill(self.color)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.hit_check(characters)


def create_platforms(number_field):
    """создание спика объектов класса platforms
    в соответсвии со спиком, создаваемым в field """
    platforms.clear()
    for i in range(NUMBER_OF_VERTICAL_BLOCKS):
        for j in range(NUMBER_OF_HORIZONTAL_BLOCKS):
            if number_field[i][j] != 0:
                platform = Platform(j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                platform.lives = number_field[i][j]
                platforms.append(platform)
