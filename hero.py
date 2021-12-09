from get_sprites import Sprites
from field import *
from constants import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, stay_sprite='s_plyr_idle1_strip8.png',
                 run_sprite='s_plyr_run_strip8.png', hero_size=(HERO_SiZE_X, HERO_SIZE_Y)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(hero_size)
        self.hero_size = hero_size
        self.run_sprite = Sprites(run_sprite)
        self.stay_sprite = Sprites(stay_sprite)
        self.milli_attack_sprite = Sprites('s_plyr_powUp_strip15.png', 2)
        self.stun_sprite = Sprites('s_plyr_pain2_strip7.png')
        self.jump_sprite = Sprites('s_plyr_jump_strip7.png')
        self.rect = self.image.get_rect()
        self.attack_rect = pygame.Surface((hero_size[0], 2*hero_size[1])).get_rect()
        self.rect.center = (start_x, start_y)
        self.onGround = False
        self.left, self.right, self.jump, self.milli_attack, self.FACING = False, False, False, False, False
        self.Vx = 0
        self.Vy = 0
        self.running = False
        self.attack = False
        self.stun = False
        self.lives = 3

    def update(self, platforms, characters, screen):
        self.event_handling()
        self.onGround = False
        self.faze_checking()
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
            ...

    def hitcheck(self, characters):
        for obj in characters:
            if obj.attack and not (self is obj):
                if self.rect.colliderect(obj.attack_rect):
                    self.stun = True
                    if obj.FACING:
                        self.FACING = False
                        self.Vx = -10
                    else:
                        self.FACING = True
                        self.Vx = 10

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

        '''if self.FACING:
            x = self.rect.bottomright
            self.rect = self.image.get_rect()
            self.rect.bottomright = x
        else:
            x = self.rect.bottomleft
            self.rect = self.image.get_rect()
            self.rect.bottomleft = x'''

    def event_handling(self):
        if not self.stun:
            if self.right:
                self.Vx += MOVE_SPEED
            if self.left:
                self.Vx -= MOVE_SPEED
            if self.onGround and self.jump:
                self.Vy = -JUMP_POWER
                self.onGround = False

    def event_checking_hero_1(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.left, self.FACING = True, True
            elif event.key == pygame.K_d:
                self.right, self.FACING = True, False
            elif event.key == pygame.K_w:
                self.jump = True
            elif event.key == pygame.K_q:
                self.milli_attack = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.left = False
            elif event.key == pygame.K_d:
                self.right = False
            elif event.key == pygame.K_w:
                self.jump = False

    def event_checking_hero_2(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left, self.FACING = True, True
            elif event.key == pygame.K_RIGHT:
                self.right, self.FACING = True, False
            elif event.key == pygame.K_UP:
                self.jump = True
            elif event.key == pygame.K_PAGEUP:
                self.milli_attack = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = False
            elif event.key == pygame.K_RIGHT:
                self.right = False
            elif event.key == pygame.K_UP:
                self.jump = False

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
        self.rect.x += self.Vx
        self.collision_x(platforms)
        if not self.onGround:
            self.Vy += GRAVITY
            self.rect.y += self.Vy
            self.collision_y(platforms)

    def reset(self):
        self.Vx = 0



