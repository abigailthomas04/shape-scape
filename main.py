import pygame
from pygame import * 

pygame.init()

# variables
run = True
screen_width = 400
screen_height = 600
scroll = 0
scroll_speed = 0.1
initial_scroll = 0
subX = 137.5
subY = 475
hopping = False
game_over = False

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ShapeScape')

# upload images
bg = pygame.image.load('shape-scape/img/sea_bg.png')
sand = pygame.image.load('shape-scape/img/sand.jpg')
seaweed = pygame.image.load('shape-scape/img/seaweed.png')
submarine = pygame.image.load('shape-scape/img/submarine.png')
title = pygame.image.load('shape-scape/img/title.png')
start1 = pygame.image.load('shape-scape/img/press_any_key.png')
start2 = pygame.image.load('shape-scape/img/any_key.png')
start3 = pygame.image.load('shape-scape/img/start.png')

# resize images
bg = pygame.transform.scale(bg, (screen_width, screen_height))
sand = pygame.transform.scale(sand, (screen_width, 50))
seaweed = pygame.transform.scale(seaweed, (50, 50))
submarine = pygame.transform.scale(submarine, (125, 125))
title = pygame.transform.scale(title, (380, 60))
start1 = pygame.transform.scale(start1, (160, 40))
start2 = pygame.transform.scale(start2, (256, 40))
start3 = pygame.transform.scale(start3, (256, 40))

# the ship
class Submarine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init()
        self.image = submarine
        self.rect = self.image.get_rect()
        self.rect.x = x    # x-coordinate of sprite's top left corner
        self.rect.y = y    # y-coordinate of sprite's top left corner
        self.vel = 0
submarine_group = pygame.sprite.Group()

while run: 

     # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw background
    screen.blit(bg, (0, scroll))
    screen.blit(bg, (0, scroll - 600))

    # draw title and start words
    screen.blit(title, (10, 50))
    screen.blit(start1, (120, 200))
    screen.blit(start2, (75, 300))
    screen.blit(start3, (75, 400))


    # draw sand
    screen.blit(sand, (0, 550 + initial_scroll))
    
    # draw seaweed
    screen.blit(seaweed, (75, 550 + initial_scroll))
    screen.blit(seaweed, (200, 550 + initial_scroll))
    screen.blit(seaweed, (300, 550 + initial_scroll))

    # draw submarine
    screen.blit(submarine, ((subX, subY)))

    # scroll the game
    scroll += scroll_speed
    if abs(scroll) > 600:
        scroll = 0
    initial_scroll += scroll_speed
    if abs(initial_scroll) > 100:
        initial_scroll = 100
    
    pygame.display.update()

pygame.quit()