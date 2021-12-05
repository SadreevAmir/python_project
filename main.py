from field import *
from constants import *
from hero import *
from platforms import *
from game import *
from menu import *

pygame.init()

screen = pygame.display.set_mode((1000, 600))
MainMenu(screen, menu_background).show()

pygame.quit()

