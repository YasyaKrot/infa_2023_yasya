# infa_2023_yasya
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

rect(screen, (190, 234, 225), (0, 0, 600, 500))
rect(screen, (155, 205, 25), (0, 300, 600, 300))

def draw_house(surface, x, y, width, height, color): 
    rect(screen, (185, 130, 105), (100, 100, 200, 200))

    rect(screen, (0, 0, 20), (100, 100, 200, 200), 5)

    polygon(screen, (225, 0, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
    polygon(screen, (0, 0, 0), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
    rect(screen, (150, 215, 225), (150, 140, 100, 100))

draw_house(screen, 200, 200, 200, 400, (200, 200, 200))

def draw_house(surface, x, y, width, height, color): 
    rect(screen, (185, 130, 105), (100, 100, 200, 200))

    rect(screen, (0, 0, 20), (100, 100, 200, 200), 5)

    polygon(screen, (225, 0, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
    polygon(screen, (0, 0, 0), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
    rect(screen, (150, 215, 225), (150, 140, 100, 100))

draw_house(screen, 100, 100, 50, 40, (200, 200, 200))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()