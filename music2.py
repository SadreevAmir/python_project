import pygame
import pathlib


def background_music():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('music/mrplastic-jump-11138.wav'), -1)
    pygame.mixer.Channel(0).set_volume(0.5)


def fireball_music():
    pygame.mixer.Channel(1).play(
        pygame.mixer.Sound('music/bolshoy-vzryiv.wav'))


def punch_music():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('music/zvuk-udara2.wav'))


def switch_music():
    if pygame.mixer.Channel(0).get_volume():
        pygame.mixer.Channel(0).set_volume(0)
    else:
        pygame.mixer.Channel(0).set_volume(0.5)


def switch_sound_effects():
    if pygame.mixer.Channel(1).get_volume():
        pygame.mixer.Channel(1).set_volume(0)
        pygame.mixer.Channel(2).set_volume(0)
    else:
        pygame.mixer.Channel(1).set_volume(1)
        pygame.mixer.Channel(2).set_volume(2)

