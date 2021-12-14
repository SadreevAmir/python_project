import pygame
import os
sep = os.path.sep

NUMBER_OF_HORIZONTAL_BLOCKS = 120
NUMBER_OF_VERTICAL_BLOCKS = 70
NUMBER_OF_OBSTACLES = 75
OBSTACLES_LENGTH_MAXIMUM = 150 
PLATFORMS_LIVES = 10

BLOCK_SIZE = 10
HERO_SiZE_X = 20
HERO_SIZE_Y = 20
HERO_LIVES = 3
WIDTH = NUMBER_OF_HORIZONTAL_BLOCKS*BLOCK_SIZE
HEIGHT = NUMBER_OF_VERTICAL_BLOCKS*BLOCK_SIZE

HERO_X = 2*HERO_SiZE_X
HERO_Y = 2*HERO_SIZE_Y

BLACK = [0, 0, 0]
WHITE = [250, 250, 250]
GREEN = [0, 250, 0]
RED = [250, 0, 0]
BLUE = [50, 50, 150]
DARK_GREEN = [10, 30, 20]
BROWN = [70, 20, 15]
PURPLE = [130, 25, 50]
YELLOW = [220, 170, 80]
PLATFORMS_COLOR = DARK_GREEN


FONT = 'Current-Regular.ttf'
SIZE = 64
PAUSE_FONT_SIZE = min(WIDTH//30, HEIGHT//19)
menu_background = 'menu_back' + sep + 'menu_back1.png'
game_background = 'game_back' + sep + 'game_back1.png'

run_sprite1 = 's_plyr_run_strip8.png'
stay_sprite1 = 's_plyr_idle1_strip8.png'
jump_sprite1 = 's_plyr_jump_strip7.png'
milli_attack_sprite1 = 's_plyr_powUp_strip15.png'
stun_sprite1 = 's_plyr_pain2_strip7.png'

run_sprite2 = 's_purp_plyr_run_strip8.png'
stay_sprite2 = 's_purp_plyr_idle1_strip8.png'
jump_sprite2 = 's_purp_plyr_jump_strip7.png'
milli_attack_sprite2 = 's_purp_plyr_powUp_strip15.png'
stun_sprite2 = 's_purp_plyr_pain2_strip7.png'

run_sprite3 = 'blue_run6.png'
stay_sprite3 = 'blue_stay12.png'
jump_sprite3 = 'blue_jump7.png'
stun_sprite3 = 'blue_stun7.png'
milli_attack_sprite3 = 'blue_punch12.png'

w_key_rus = 1094
a_key_rus = 1092
d_key_rus = 1074
e_key_rus = 1091
q_key_rus = 1081
comma_key_rus = 1073

MOVE_SPEED = 5
JUMP_POWER = 9
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз

characters = []
num_field = []

all_sprites = pygame.sprite.Group()

FPS = 60
