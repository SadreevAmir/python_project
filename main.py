from field import *
from constants import *
from hero import *
from platforms import *
from game import *
from menu import *

pygame.init()

screen = pygame.display.set_mode((1000, 600))
show_main_menu(screen)

pygame.quit()

