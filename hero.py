from get_sprites import Sprites
from field import *
from constants import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, hero_size=(HERO_SiZE_X, HERO_SIZE_Y)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(hero_size)
        self.hero_size = hero_size
        self.run_sprite = Sprites('s_plyr_run_strip8.png')
        self.stay_sprite = Sprites('s_plyr_idle1_strip8.png')
        self.jump_sprite = Sprites('s_plyr_jump_strip7.png')
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.onGround = False
        self.left, self.right, self.jump, self.FACING = False, False, False, False
        self.Vx = 0
        self.Vy = 0

    def update(self, platforms, screen):
        self.event_handling()
        self.onGround = False
        self.movement(platforms)
        if (self.right or self.left) and (not self.right or not self.left):
            self.image = pygame.transform.scale(self.run_sprite.get_sprite(self.FACING), self.hero_size)
        elif self.jump:
            self.image = pygame.transform.scale(self.jump_sprite.get_sprite(self.FACING), self.hero_size)
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

    def event_checking_hero_1(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == a_key_rus:
                self.left, self.FACING = True, True
            elif event.key == pygame.K_d or event.key == d_key_rus:
                self.right, self.FACING = True, False
            elif event.key == pygame.K_w or event.key == w_key_rus:
                self.jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == a_key_rus:
                self.left = False
            elif event.key == pygame.K_d or event.key == d_key_rus:
                self.right = False
            elif event.key == pygame.K_w or event.key == w_key_rus:
                self.jump = False

    def event_checking_hero_2(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left, self.FACING = True, True
            elif event.key == pygame.K_RIGHT:
                self.right, self.FACING = True, False
            elif event.key == pygame.K_UP:
                self.jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = False
            elif event.key == pygame.K_RIGHT:
                self.right = False
            elif event.key == pygame.K_UP:
                self.jump = False

    def collision_x(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):

                if self.Vx > 0:
                    self.rect.right = p.rect.left

                if self.Vx < 0:
                    self.rect.left = p.rect.right

    def collision_y(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if self.Vy > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.Vy = 0

                if self.Vy < 0:
                    self.rect.top = p.rect.bottom
                    self.Vy = 0

           
    def movement(self, platforms):
        self.rect.x += self.Vx
        self.collision_x(platforms)
        if not self.onGround:
            self.Vy += GRAVITY
            self.rect.y += self.Vy
            self.collision_y(platforms)

    def reset(self):
        self.Vx = 0