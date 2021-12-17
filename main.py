
from game import background_music, start_game
from music import starting_sound_settings
from menu import MainMenu
from constants import*

pygame.init()
starting_sound_settings()
background_music()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
MainMenu(screen, menu_background, lambda: start_game(game_background)).show()

pygame.quit()
