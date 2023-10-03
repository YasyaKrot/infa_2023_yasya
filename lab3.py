# infa_2023_yasya
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))



circle(screen, (255, 190, 10), (300, 300), 260, 0)

circle(screen, (200, 45, 45), (190, 200), 60, 60)

circle(screen, (20, 35, 35), (190, 200), 20, 60)

circle(screen, (200, 45, 45), (410, 200), 60, 60)

circle(screen, (20, 35, 35), (410, 200), 20, 60)



rect(screen, (0, 0, 0), (190, 370, 240, 50))

polygon(screen, (0, 0, 0), [(280,110), (280,150), (100, 100), (100,60)])

polygon(screen, (0, 0, 0), [(300,110), (300,150), (480, 100), (480,60)])



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()




