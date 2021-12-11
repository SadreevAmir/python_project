import pygame

from get_sprites import Sprites
from field import *
from constants import *
from bullet import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, hero_size=(HERO_SiZE_X, HERO_SIZE_Y)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(hero_size)
        self.hero_size = hero_size
        self.run_sprite = Sprites(run_sprite1)
        self.stay_sprite = Sprites(stay_sprite1)
        self.milli_attack_sprite = Sprites(milli_attack_sprite1, 40, 2)
        self.stun_sprite = Sprites(stun_sprite1, 60)
        self.jump_sprite = Sprites(jump_sprite1)
        self.rect = self.image.get_rect()
        self.attack_rect = pygame.Surface((hero_size[0], 2*hero_size[1])).get_rect()
        self.rect.center = (start_x, start_y)
        self.onGround = False
        self.left, self.right, self.jump, self.milli_attack, self.FACING = False, False, False, False, False
        self.Vx = 0
        self.Vy = 0
        self.kick_speed = 0
        self.running = False
        self.attack = False
        self.stun = False
        self.shot()
        self.lives = 30

    def update(self, platforms, characters, screen):
        self.event_handling()
        self.onGround = False
        self.faze_checking()
        if True:
            self.hitcheck(characters)
            y, x = self.animate(screen)
            self.movement(platforms)
            # pygame.draw.rect(screen, [0, 0, 0], self.attack_rect)
            screen.blit(self.image, (x, y))
            self.reset()

    def faze_checking(self):
        if self.lives > 0:
            if not self.attack and self.milli_attack:
                self.attack = True
            elif self.attack and not self.milli_attack:
                self.attack = False
        else:
            self.kill()

    def hitcheck(self, characters):
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
                        self.Vy -= 2
                        self.stun = True

    def shot(self):
        all_sprites.add(Bullet(self, self.rect.centerx, self.rect.centery))

    def death(self):
        ...

    def animate(self, screen):
        if self.stun:
            self.image = self.stun_sprite.get_sprite(self.FACING)
            if self.stun_sprite.currentFrame == self.stun_sprite.numbers_image - 1:
                self.stun = False
            return self.rect.y, self.rect.x
        elif self.attack:
            self.image = self.milli_attack_sprite.get_sprite(self.FACING)
            if self.milli_attack_sprite.currentFrame == self.milli_attack_sprite.numbers_image - 1:
                self.milli_attack = False
            if self.FACING:
                self.attack_rect.bottomright = self.rect.bottomleft
                return 2*self.rect.y - self.rect.bottom, 2*self.rect.x - self.rect.right
            else:
                self.attack_rect.bottomleft = self.rect.bottomright
                return 2*self.rect.y - self.rect.bottom, self.rect.x
        elif (self.right or self.left) and (not self.right or not self.left):
            self.image = self.run_sprite.get_sprite(self.FACING)
            return self.rect.y, self.rect.x
        else:
            self.image = self.stay_sprite.get_sprite(self.FACING)
            return self.rect.y, self.rect.x

    def event_handling(self):
        if not self.stun:
            if self.right:
                self.Vx += MOVE_SPEED
            if self.left:
                self.Vx -= MOVE_SPEED
            if self.onGround and self.jump:
                self.Vy = -JUMP_POWER
                self.onGround = False

    def collision_x(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p) and not (self is p):

                if self.Vx > 0:
                    self.rect.right = p.rect.left

                if self.Vx < 0:
                    self.rect.left = p.rect.right

    def collision_y(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p) and not (self is p):
                if self.Vy > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.Vy = 0

                if self.Vy < 0:
                    self.rect.top = p.rect.bottom
                    self.Vy = 0

    def movement(self, platforms):
        self.Vx += self.kick_speed
        self.rect.x += self.Vx
        self.collision_x(platforms)
        if not self.onGround:
            self.Vy += GRAVITY
            self.rect.y += self.Vy
            self.collision_y(platforms)

    def reset(self):
        self.Vx = 0
        if self.kick_speed > 0:
            self.kick_speed -= 1
        elif self.kick_speed < 0:
            self.kick_speed += 1


class Hero1(Hero):
    def __init__(self, start_x, start_y):
        super(Hero1, self).__init__(start_x, start_y)
        self.jump_sprite = Sprites(jump_sprite1)
        self.run_sprite = Sprites(run_sprite1)
        self.stay_sprite = Sprites(stay_sprite1)
        self.milli_attack_sprite = Sprites(milli_attack_sprite1, 40, 2)
        self.stun_sprite = Sprites(stun_sprite1, 60)

    def event_checking_hero(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == a_key_rus:
                self.left, self.FACING = True, True
            elif event.key == pygame.K_d or event.key == d_key_rus:
                self.right, self.FACING = True, False
            elif event.key == pygame.K_w or event.key == w_key_rus:
                self.jump = True
            elif event.key == pygame.K_e or event.key == e_key_rus:
                self.shot()
            elif event.key == pygame.K_q or event.key == q_key_rus:
                self.milli_attack = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == a_key_rus:
                self.left = False
            elif event.key == pygame.K_d or event.key == d_key_rus:
                self.right = False
            elif event.key == pygame.K_w or event.key == w_key_rus:
                self.jump = False


class Hero2(Hero):
    def __init__(self, start_x, start_y):
        super(Hero2, self).__init__(start_x, start_y)
        self.jump_sprite = Sprites(jump_sprite2)
        self.run_sprite = Sprites(run_sprite2)
        self.stay_sprite = Sprites(stay_sprite2)
        self.milli_attack_sprite = Sprites(milli_attack_sprite2, 40, 2)
        self.stun_sprite = Sprites(stun_sprite2, 60)

    def event_checking_hero(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left, self.FACING = True, True
            elif event.key == pygame.K_RIGHT:
                self.right, self.FACING = True, False
            elif event.key == pygame.K_UP:
                self.jump = True
            elif event.key == pygame.K_SLASH:
                self.milli_attack = True
            elif event.key == pygame.K_COMMA or event.key == comma_key_rus:
                self.shot()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = False
            elif event.key == pygame.K_RIGHT:
                self.right = False
            elif event.key == pygame.K_UP:
                self.jump = False
