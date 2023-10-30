import pygame
from pygame import * 

pygame.init()

screen_width = 300
screen_height = 600

# variables
run = True

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ShapeScape')

while run: 

     # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()

pygame.quit()