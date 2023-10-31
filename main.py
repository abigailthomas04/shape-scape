# import pygame library
import pygame
from pygame import * 

from pygame import mixer

# initialize pygame
pygame.init()

# initalize the music
mixer.init()

# load audio files
# mixer.music.load('song.mp3')

# set volume
# mixer/music.set_volume(0.2)

# variables
run = True
screen_width = 400     # width of the entire window (x-axis)
screen_height = 600    # height of the entire window (y-axis)
scroll = 0             # scroll for the bg
scroll_speed = 0.1     # speed of the scroll
initial_scroll = 0     # scroll for ocean floor to disappear and not repeat
subX = 137.5           # initial x coordinate of submarine
subY = 475             # initial y coordinate of submarine
hopping = False        # is player hopping or still
game_over = False      # has player hit obstacle
starting = False       # has player pressed SPACE BAR to start

# draw the screen 
screen = pygame.display.set_mode((screen_width, screen_height))

# name the screen
pygame.display.set_caption('ShapeScape')

# upload images
bg = pygame.image.load('shape-scape/img/sea_bg.png')
sand = pygame.image.load('shape-scape/img/sand.jpg')
seaweed = pygame.image.load('shape-scape/img/seaweed.png')
submarine = pygame.image.load('shape-scape/img/submarine.png')
title = pygame.image.load('shape-scape/img/title.png')
start1 = pygame.image.load('shape-scape/img/press.png')
start2 = pygame.image.load('shape-scape/img/space_bar.png')
start3 = pygame.image.load('shape-scape/img/start.png')

# resize images
bg = pygame.transform.scale(bg, (screen_width, screen_height))
sand = pygame.transform.scale(sand, (screen_width, 50))
seaweed = pygame.transform.scale(seaweed, (50, 50))
submarine = pygame.transform.scale(submarine, (125, 125))
title = pygame.transform.scale(title, (380, 60))
start1 = pygame.transform.scale(start1, (160, 40))
start2 = pygame.transform.scale(start2, (300, 40))
start3 = pygame.transform.scale(start3, (256, 40))

# the ship
class Submarine(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init()
        self.image = submarine
        self.rect = self.image.get_rect()
        self.rect.x = x    # x-coordinate of sprite's top left corner
        self.rect.y = y    # y-coordinate of sprite's top left corner

submarine_group = pygame.sprite.Group()

### THE MAIN LOOP ###
while run: 

    # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            # break the loop
            run = False

    # play the music
    # mixer.music.play()

    # check for user to press SPACE BAR
    pressed = pygame.key.get_pressed()
    if(pressed[K_SPACE]) == True:
        starting = True

    # draw background
    screen.blit(bg, (0, scroll))
    screen.blit(bg, (0, scroll - 600))

    # draw sand
    screen.blit(sand, (0, 550 + initial_scroll))

    # draw submarine
    screen.blit(submarine, ((subX, subY)))
    
    # draw seaweed
    # left most seaweed
    screen.blit(seaweed, (65, 540 + initial_scroll))
    # middle seaweed
    screen.blit(seaweed, (235, 530 + initial_scroll))
    # right most seaweed
    screen.blit(seaweed, (300, 545 + initial_scroll))

    # until user presses SPACE BAR, title screen is drawn
    if starting == False:
        # draw title and start words
        screen.blit(title, (10, 50))
        screen.blit(start1, (120, 200))
        screen.blit(start2, (54, 300))
        screen.blit(start3, (75, 400))

    # scroll the background
    # scroll += scroll_speed
    if abs(scroll) > 650:
        scroll = 0

    # scroll the ocean floor off screen
    # initial_scroll += scroll_speed
    if abs(initial_scroll) > 100:
        initial_scroll = 100
    
    # update the display
    pygame.display.update()

# quit the window
pygame.quit()