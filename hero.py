import pygame
from get_sprites import Sprites

MOVE_SPEED = 5
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз


class Hero(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, hero_size=(60, 60)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(hero_size)
        self.hero_size = hero_size
        self.run_sprite = Sprites('s_plyr_run_strip8.png')
        self.stay_sprite = Sprites('s_plyr_idle1_strip8.png')
        self.jump_sprite = Sprites('s_plyr_jump_strip7.png')
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.onGround = True
        self.left, self.right, self.jump, self.FACING = False, False, False, False

    def update(self):
        self.event_handling()
        if (self.right or self.left) and (not self.right or not self.left):
            self.image = pygame.transform.scale(self.run_sprite.get_sprite(self.FACING), self.hero_size)
        else:
            self.image = pygame.transform.scale(self.stay_sprite.get_sprite(self.FACING), self.hero_size)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def event_handling(self):
        if self.right:
            self.rect.x += MOVE_SPEED
        if self.left:
            self.rect.x -= MOVE_SPEED

    def event_checking(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.left, self.FACING = True, True
            elif event.key == pygame.K_d:
                self.right, self.FACING = True, False
            elif self.onGround and event.key == pygame.K_SPACE:
                self.jump = True
                self.onGround = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.left = False
            elif event.key == pygame.K_d:
                self.right = False
            elif event.key == pygame.K_SPACE:
                ...


pygame.init()

FPS = 60
screen = pygame.display.set_mode((1000, 600))
screen.fill([55, 255, 255])

all_sprites = pygame.sprite.Group()
hero = Hero(500, 500)
all_sprites.add(hero)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    screen.fill([55, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            hero.event_checking(event)
    all_sprites.update()
    pygame.display.update()

pygame.quit()

