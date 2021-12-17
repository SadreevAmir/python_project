import pygame


def background_music():
    """Запускает зацикленную фоновую музыку

    :return: None
    """

    pygame.mixer.Channel(0).play(pygame.mixer.Sound('music_files/mrplastic-jump-11138.wav'), -1)


def fireball_music():
    """Воспроизводит звук взрыва

    :return: None
    """

    pygame.mixer.Channel(1).play(
        pygame.mixer.Sound('music_files/bolshoy-vzryiv.wav'))


def punch_music():
    """Воспроизводит звук удара

    :return: None
    """

    pygame.mixer.Channel(2).play(pygame.mixer.Sound('music_files/zvuk-udara2.wav'))


def switch_music():
    """Запускает или останавливает воспроизведение фоновой музыки

    :return: None
    """

    if pygame.mixer.Channel(0).get_volume():
        pygame.mixer.Channel(0).set_volume(0)
    else:
        pygame.mixer.Channel(0).set_volume(0.5)


def switch_sound_effects():
    """Включает или выключает звуки эффектов (удары, выстрелы)

    :return: None
    """

    if pygame.mixer.Channel(1).get_volume():
        pygame.mixer.Channel(1).set_volume(0)
        pygame.mixer.Channel(2).set_volume(0)
    else:
        pygame.mixer.Channel(1).set_volume(1)
        pygame.mixer.Channel(2).set_volume(2)
