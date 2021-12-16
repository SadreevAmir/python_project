
from game import *
from menu import *

pygame.init()
pygame.mixer.Channel(0).set_volume(0.5)
pygame.mixer.Channel(1).set_volume(1)
pygame.mixer.Channel(2).set_volume(2)

background_music()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
MainMenu(screen, menu_background, lambda: start_game(game_background)).show()

pygame.quit()
