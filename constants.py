import pygame

NUMBER_OF_HORIZONTAL_BLOCKS = 120
NUMBER_OF_VERTICAL_BLOCKS = 70
NUMBER_OF_OBSTACLES = 75
OBSTACLES_LENGTH_MAXIMUM = 150

BLOCK_SIZE = 10
HERO_SiZE_X = 20
HERO_SIZE_Y = 20
WIDTH = NUMBER_OF_HORIZONTAL_BLOCKS*BLOCK_SIZE
HEIGHT = NUMBER_OF_VERTICAL_BLOCKS*BLOCK_SIZE

HERO_X = 2*HERO_SiZE_X
HERO_Y = 2*HERO_SIZE_Y

BLACK = [0, 0, 0]
WHITE = [250, 250, 250]
GREEN = [0, 250, 0]
RED = [190, 0, 0]
BLUE = [50, 50, 150]
DARK_GREEN = [10, 30, 20]
BROWN = [70, 20, 15]
PURPLE = [130, 25, 50]
YELLOW = [220, 170, 80]

FONT = 'Current-Regular.ttf'
SIZE = 54
PAUSE_FONT_SIZE = min(WIDTH//30, HEIGHT//19)
menu_background = 'menu_back/menu_back1.png'
game_background = 'game_back/game_back1.png'

run_sprite1 = 's_plyr_run_strip8.png'
stay_sprite1 = 's_plyr_idle1_strip8.png'
jump_sprite1 = 's_plyr_jump_strip7.png'
run_sprite2 = 'blue_run6.png'
stay_sprite2 = 'blue_stay12.png'
jump_sprite2 = 'blue_jump7.png'


w_key_rus = 1094
a_key_rus = 1092
d_key_rus = 1074

MOVE_SPEED = 5
JUMP_POWER = 9
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз

characters = []

all_sprites = pygame.sprite.Group()

FPS = 60
