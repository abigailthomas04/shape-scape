### IMPORTING NECCESSARY LIBRARIES ###
import pygame
from pygame import * 
from pygame import mixer
import time
import random

### INITIALIZING ###
pygame.init()
mixer.init()

### HIDE MOUSE CURSOR ###
pygame.mouse.set_visible(False)

########### AUDIO UPLOADING, VOLUME, AND PLAYING ############
bg_music = mixer.music.load('shape-scape/audio/bg_music.mp3')
# game_over_music = mixer.music.load('shape-scape/audio/game_over_audio.mp3')
bg_music_volume = mixer.music.set_volume(0.5)
# game_over_music = mixer.music.set_volume(1)
bg_music_play = mixer.music.play()
# game_over_music_play = mixer.music.play()
#############################################################

######################### CONSTANTS #########################
SCREEN_WIDTH = 400     # width of the entire window (x-axis)
SCREEN_HEIGHT = 650    # height of the entire window (y-axis)
SCROLL_SPEED = .15     # speed of the scroll
#############################################################

# variables
scroll = 0             # scroll for the bg
sand_scroll = 0        # scroll for ocean floor to disappear and not repeat
log_scroll = 0         # scroll for logs
subX = 200             # initial x coordinate of submarine
subY = 590             # initial y coordinate of submarine
logX = 200             # intitial x coordinate of log 
logY = 175             # initial y coordinate of log
starting = False       # has player pressed SPACE BAR to start
collision = False      # collision boolean
game_end = False       # game over boolean
fell_off = False       # fell off the screen boolean

################### DRAW SCREEN AND NAME IT ##################
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ShapeScape')
##############################################################

############### UPLOADING AND RESIZING IMAGES ################
bg = pygame.image.load('shape-scape/img/ocean_bg.png')
sand = pygame.image.load('shape-scape/img/sand.jpg')
seaweed = pygame.image.load('shape-scape/img/seaweed.png')
submarine = pygame.image.load('shape-scape/img/submarine.png')
title = pygame.image.load('shape-scape/img/title.png')
start1 = pygame.image.load('shape-scape/img/press.png')
start2 = pygame.image.load('shape-scape/img/space_bar.png')
start3 = pygame.image.load('shape-scape/img/to_start.png')
end = pygame.image.load('shape-scape/img/game_over_img.png')
log = pygame.image.load('shape-scape/img/log1.png')

bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
sand = pygame.transform.scale(sand, (SCREEN_WIDTH, 100))
seaweed = pygame.transform.scale(seaweed, (50, 50))
submarine = pygame.transform.scale(submarine, (80, 80))
title = pygame.transform.scale(title, (380, 60))
start1 = pygame.transform.scale(start1, (160, 40))
start2 = pygame.transform.scale(start2, (300, 40))
start3 = pygame.transform.scale(start3, (256, 40))
end = pygame.transform.scale(end, (380, 60))
log = pygame.transform.scale(log, (100, 25))
##############################################################

###################### THE SHIP CLASS ########################
class Submarine():

    def __init__(self, x, y):
        self.image = submarine
        self.width = 80
        self.height = 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0

    ### HOPPING ###
    def hop(self):
        dy = 0
        gravity = .1

        ### GRAVITY ###
        self.vel_y += gravity
        dy += self.vel_y
        self.rect.y += dy

        ### STOP PLAYER FROM FALLING OFF SCREEN FOR FIRST 5 SECONDS ###
        if self.rect.bottom + dy > SCREEN_HEIGHT - 5 and time < 5000:
            dy = 0
            self.vey_y = 0
            self.rect.y = subY

        ### PRESS UP ARROW TO HOP ###
        up_arrow = pygame.key.get_pressed()
        if up_arrow[pygame.K_UP] == True:
            self.vel_y = -2.
    
    ### DRAW SUBMARINE ###   
    def draw(self):
        screen.blit(self.image, (self.rect.x - 0, self.rect.y - 20))
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
##############################################################
        
### LIST FOR OBSTACLES ###
obstacles = []
#################### THE OBSTACLES CLASS #####################
class Obstacle():

    def __init__(self, x, y):
        self.image = log
        self.width = 100
        self.height = 25
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.speed = 1

    ### DRAW OBSTACLES ###
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

    ### MOVE OBSTACLES ###
    def move(self):
        self.rect.x += self.speed
        if self.rect.x > SCREEN_WIDTH:
            obstacles.append(Obstacle(0, random.randint(0, SCREEN_WIDTH)))
##############################################################

# tbh idk what this does
def init():
    obstacles.append(Obstacle(0, 0))

### CREATE INSTANCES OF LOGS###
log = Obstacle(0, random.randint(25, SCREEN_WIDTH))

init()     # idk bro

### CREATE INSTANCE OF SUBMARINE ###
sub = Submarine(subX, subY)

################### THE START MENU ###########################
def start_menu():
    print("start menu NOT YET STARTED")
    #############################################
    ### INITIAL BG , GAME NOT YET STARTED ###
    # (behind the start menu)
    # draw background
    screen.blit(bg, (0, scroll))
    screen.blit(bg, (0, scroll - 650))
    # draw sand
    screen.blit(sand, (0, 550 + sand_scroll))
    # draw submarine
    sub.draw()
    # draw seaweed
    # left most seaweed
    screen.blit(seaweed, (65, 540 + sand_scroll))
    # middle seaweed
    screen.blit(seaweed, (235, 530 + sand_scroll))
    # right most seaweed
    screen.blit(seaweed, (300, 545 + sand_scroll))
    ##############################################

    screen.blit(title, (10, 50))
    screen.blit(start1, (120, 200))
    screen.blit(start2, (54, 300))
    screen.blit(start3, (75, 400))
##############################################################

######################## GAME START ##########################
def game_start():
    print("game playing")
    if game_end == False:
        ### BG WITH NO SCROLLING ###
        ### OCEAN BG ### 
        screen.blit(bg, (0, scroll))
        screen.blit(bg, (0, scroll - 650))
        ### SAND ###
        screen.blit(sand, (0, 550 + sand_scroll))
        ### LEFTMOST SEAWEED ###
        screen.blit(seaweed, (65, 540 + sand_scroll))
        ### MIDDLE SEAWEED ###
        screen.blit(seaweed, (235, 530 + sand_scroll))
        ### RIGHTMOST SEAWEED ###
        screen.blit(seaweed, (300, 545 + sand_scroll))

        sub.draw()
        
            
        # stop user from going up off screen
        if sub.rect.y < 17:
            sub.rect.y = 17
        
        # player hopping
        sub.hop()

        log.move()
        log.draw()

        ### KEEP LOG SCROLLING ###
        if log.rect.x > SCREEN_HEIGHT:
            log.rect.x = -50
##############################################################
        
######################### GAME OVER ##########################
def game_over():
    global game_end     # idk

    print("GAME OVER SCREEN")
    ### BG WITH NO SCROLLING ###
    ### OCEAN BG ### 
    screen.blit(bg, (0, 0))
    ### SAND ###
    screen.blit(sand, (0, 550))
    ### LEFTMOST SEAWEED ###
    screen.blit(seaweed, (65, 540))
    ### MIDDLE SEAWEED ###
    screen.blit(seaweed, (235, 530))
    ### RIGHTMOST SEAWEED ###
    screen.blit(seaweed, (300, 545))

    ### SUB AT STARTING POSITION ###
    sub.rect.y = 590
    ### DRAW SUBMARINE ###
    sub.draw()
    
    ### GAME OVER WORDS ###
    screen.blit(end, (10, 200))

##############################################################

run = True
### THE MAIN LOOP ###
while run: 

    # EVENTS
    for event in pygame.event.get():
         # if user clicks exit window, game quits
        if event.type == pygame.QUIT:
            # break the loop
            run = False

    restart = pygame.key.get_pressed()
    if (restart[K_SPACE]) == True:
        collision = False
        starting = True
        game_end = False
        if collision == False and fell_off == False:
            game_start()

    # check for user to press SPACE BAR to start playing game
    pressed = pygame.key.get_pressed()
    if (pressed[K_SPACE]) == True:
        starting = True

    # until user presses SPACE BAR, title screen/ start menu is drawn
    if starting == False and game_end == False:
        # call start menu
        start_menu()

    # game begins after SPACE BAR is pressed, and start menu goes away
    elif starting == True:

        game_start()
        # time stuff
        time = pygame.time.get_ticks()

        # scroll the background
        scroll += SCROLL_SPEED
        if abs(scroll) > 650:
            scroll = 0

        # scroll the ocean floor off screen
        sand_scroll += SCROLL_SPEED
        if abs(sand_scroll) > 120:
            sand_scroll = 120
        ### IF SUB COLLIDES WITH LOG OR FALLS OFF ###
        if sub.rect.colliderect(log):
            collision = True
            fell_off = False
            game_end = True
            starting = False
            scroll = 0
            sand_scroll = 0
            print("COLLISION")
            game_over()
        if sub.rect.y > SCREEN_HEIGHT + 80:
            collision = False
            fell_off = True
            game_end = True
            starting = False
            scroll = 0
            sand_scroll = 0
            print("FELL OFF")
            game_over()

    # update the display
    pygame.display.update()

# quit the window
pygame.quit()

### FIGURE OUT PLAY AGAIN ### 