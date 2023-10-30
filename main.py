import pygame
from pygame import * 

pygame.init()

# variables
run = True
screen_width = 400
screen_height = 600
scroll = 0
scroll_speed = 1

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ShapeScape')

# upload images
sand = pygame.image.load('shape-scape/img/sand.jpg')
seaweed = pygame.image.load('shape-scape/img/seaweed.png')

# resize images
sand = pygame.transform.scale(sand, (screen_width, 50))
seaweed = pygame.transform.scale(seaweed, (50, 50))



while run: 

     # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw sand
    screen.blit(sand, (0, 550))
    
    # draw seaweed
    screen.blit(seaweed, (75, 515))
    screen.blit(seaweed, (200, 505))
    screen.blit(seaweed, (300, 520))
    
    pygame.display.update()

pygame.quit()