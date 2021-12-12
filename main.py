from field import *
from constants import *
from hero import *
from music2 import background_music
from platforms import *
from game import *
from menu import *

pygame.init()

background_music()
screen = pygame.display.set_mode((1000, 600))
MainMenu(screen, menu_background, lambda: Game().start_game()).show()

pygame.quit()
