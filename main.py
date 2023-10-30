import pygame
from pygame import * 

pygame.init()

# variables
run = True
screen_width = 400
screen_height = 600
scroll = 0
scroll_speed = 0.05

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ShapeScape')

# upload images
bg = pygame.image.load('shape-scape/img/blue_bg.jpg')
sand = pygame.image.load('shape-scape/img/sand.jpg')
seaweed = pygame.image.load('shape-scape/img/seaweed.png')

# resize images
bg = pygame.transform.scale(bg, (screen_width, screen_height))
sand = pygame.transform.scale(sand, (screen_width, 50))
seaweed = pygame.transform.scale(seaweed, (50, 50))



while run: 

     # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw background
    screen.blit(bg, (0, scroll))
    screen.blit(bg, (0, scroll - 600))

    # draw sand
    '''screen.blit(sand, (0, 550 + scroll))
    
    # draw seaweed
    screen.blit(seaweed, (75, 550 + scroll))
    screen.blit(seaweed, (200, 550 + scroll))
    screen.blit(seaweed, (300, 550 + scroll))'''

    # scroll the game
    scroll += scroll_speed
    if abs(scroll) > 600:
        scroll = 0
    
    pygame.display.update()

pygame.quit()