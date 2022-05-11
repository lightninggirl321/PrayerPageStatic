#+AMDG+JMJ+TTM+
#imports
import pygame
from pygame.locals import *
from pygame import mixer
pygame.init()

#global variables
resolution = (679, 588)
white = (255, 255, 255)
black = (0, 0)
red = (255, 0, 0)
screen = pygame.display.set_mode(resolution)
background = pygame.image.load("RevFinishedBG.png").convert()
game_running = True

#music
mixer.init()
mixer.music.load("PrayerProjectBachAveMaria.mp3")
mixer.music.play()

#Body Code
while game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()

#Music
#Animation (twinkling stars)