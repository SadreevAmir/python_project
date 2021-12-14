import pygame
import pathlib


def background_music():
    pygame.mixer.Channel(0).play(
        pygame.mixer.Sound('music/01-Super-Mario-Bros.wav'))
    pygame.mixer.Channel(0).set_volume(0.5)


def fireball_music():
    pygame.mixer.Channel(1).play(
        pygame.mixer.Sound('music/bolshoy-vzryiv.wav'))


def punch_music():
    pygame.mixer.Channel(2).set_volume(2)
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('music/zvuk-udara2.wav'))
