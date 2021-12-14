from field import *
from constants import *
from hero import *
from music2 import background_music
from platforms import *
from game import *
from menu import *

pygame.init()

background_music()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
MainMenu(screen, menu_background, lambda: start_game()).show()

pygame.quit()
