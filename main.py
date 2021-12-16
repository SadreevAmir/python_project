from game import *
from menu import *

pygame.init()

background_music()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
MainMenu(screen, menu_background, lambda: start_game()).show()

pygame.quit()
