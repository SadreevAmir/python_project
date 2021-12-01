import pygame
from get_sprites import Sprites

MOVE_SPEED = 5
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, a, b):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((a, b))
        self.image.fill([0, 0, 0])
        self.rect = pygame.Rect(x, y, a, b)
        #self.current_image = image.load('../cyber/sprites/thisisit.jpg')

    def update(self, platforms):
        screen.blit(self.image, (self.rect.x, self.rect.y))


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
        self.Vx = 0
        self.Vy = 0

    def update(self, platforms):
        self.event_handling()
        self.movement(platforms)
        if (self.right or self.left) and (not self.right or not self.left):
            self.image = pygame.transform.scale(self.run_sprite.get_sprite(self.FACING), self.hero_size)
        else:
            self.image = pygame.transform.scale(self.stay_sprite.get_sprite(self.FACING), self.hero_size)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.reset()

    def event_handling(self):
        if self.right:
            self.Vx += MOVE_SPEED
        if self.left:
            self.Vx -= MOVE_SPEED
        if self.onGround and self.jump:
            self.Vy = -JUMP_POWER
            self.onGround = False

    def event_checking(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.left, self.FACING = True, True
            elif event.key == pygame.K_d:
                self.right, self.FACING = True, False
            elif event.key == pygame.K_SPACE:
                self.jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.left = False
            elif event.key == pygame.K_d:
                self.right = False
            elif event.key == pygame.K_SPACE:
                self.jump = False

    def collision_x(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):

                if self.Vx > 0:
                    self.rect.right = p.rect.left
                    print(1)

                if self.Vx < 0:
                    self.rect.left = p.rect.right
                    print(2)

    def collision_y(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if self.Vy > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.Vy = 0
                    print(3)

                if self.Vy < 0:
                    self.rect.top = p.rect.bottom
                    self.Vy = 0

    def movement(self, platforms):
        self.rect.x += self.Vx
        self.collision_x(platforms)
        if not self.onGround:
            self.rect.y += self.Vy
            self.Vy += GRAVITY
            self.collision_y(platforms)

    def reset(self):
        self.Vx = 0


pygame.init()

FPS = 60
screen = pygame.display.set_mode((1000, 600))
screen.fill([55, 255, 255])

platforms = []

all_sprites = pygame.sprite.Group()
hero = Hero(500, 500)
floor = Platform(0, 530, 1000, 20)
wall_left = Platform(0, 0, 20, 600)
wall_right = Platform(980, 0, 20, 600)
roof = Platform(0, 400, 1000, 20)
platforms.append(floor)
platforms.append(wall_right)
platforms.append(wall_left)
platforms.append(roof)
all_sprites.add(hero, floor, wall_right, wall_left, roof)

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
    all_sprites.update(platforms)
    pygame.display.update()

pygame.quit()

