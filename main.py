####################################################
### Please refer to the README for directions :) ###
####################################################

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

### DEFINE A FONT ANF COLOR FOR TEXT ###
font = pygame.font.SysFont('Bauhaus 93', 50)
white = ((255, 255, 255))

########### AUDIO UPLOADING, VOLUME, AND PLAYING ############
bg_music = mixer.music.load('shape-scape/audio/bg_music.mp3')
# game_over_music = mixer.music.load('shape-scape/audio/game_over_audio.mp3')
bg_music_volume = mixer.music.set_volume(0)
# game_over_music = mixer.music.set_volume(1)
bg_music_play = mixer.music.play()
# game_over_music_play = mixer.music.play()
#############################################################

######################### CONSTANTS #########################
SCREEN_WIDTH = 400     # width of the entire window (x-axis)
SCREEN_HEIGHT = 650    # height of the entire window (y-axis)
SCROLL_SPEED = .2     # speed of the scroll
SUB_X = 200             # initial x coordinate of submarine
SUB_Y = 590             # initial y coordinate of submarine
#############################################################

# variables
scroll = 0             # scroll for the bg
sand_scroll = 0        # scroll for ocean floor to disappear and not repeat
starting = False       # start playing boolean
collision = False      # collision boolean
game_end = False       # game over boolean
fell_off = False       # fell off the screen boolean
score = 0              # score !
hi_score = 0           # hi-score !

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

    def __init__(self, SUB_X, SUB_Y):
        self.image = submarine
        self.width = 80
        self.height = 45
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (SUB_X, SUB_Y)
        self.vel_y = 0

    ### HOPPING ###
    def hop(self):
        dy = 0
        gravity = .1

        ### GRAVITY ###
        self.vel_y += gravity
        dy += self.vel_y
        self.rect.y += dy

        ### PRESS UP ARROW TO HOP ###
        up_arrow = pygame.key.get_pressed()
        if up_arrow[pygame.K_SPACE] == True:
            self.vel_y = -2.
    
    ### DRAW SUBMARINE ###   
    def draw(self):
        screen.blit(self.image, (self.rect.x , self.rect.y - 30))
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
        self.rect.y += self.speed
##############################################################

### HELP HOW TO MAKE A LIST AND APPEND THIS IS SO HARD IM JUST A GIRL ###
### CREATE INSTANCES OF LOGS ### 
log1 = Obstacle(random.randint(-700, -600), random.randint(-25, 25))
log2 = Obstacle(random.randint(-500, -200), random.randint(100, 200))
log3 = Obstacle(random.randint(-100, 0), random.randint(300, 550))
### CREATE INSTANCE OF SUBMARINE ###
sub = Submarine(SUB_X, SUB_Y)

################ THE TEXT ################
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
##########################################

################### THE START MENU ###########################
def start_menu():
    ###### INITIAL BG , GAME NOT YET STARTED ######
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
    ##############################################

    ### DRAW SUB ###
    sub.draw()

    ### TITLE SCREEN ###
    screen.blit(title, (10, 50))
    screen.blit(start1, (120, 200))
    screen.blit(start2, (54, 300))
    screen.blit(start3, (75, 400))
##############################################################

######################## GAME START ##########################
def game_start():
    if game_end == False:
        # pygame.time.delay(3000) # DOESNT WORK HERE
        ############ BG WITH NO SCROLLING ############
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
        ##############################################

        ############## THE SUBMARINE #############
        ### DRAW SUB ###
        sub.draw()
        ### STOP USER FROM GOING UP OFF SCREEN ###
        if sub.rect.y < 17:
            sub.rect.y = 17
        ### PLAYER HOPPING ###
        sub.hop()
        ##########################################

        ############ THE OBSTACLES ###############
        ### CALLING THE LOG ###
        ## LOG 1 ###
        log1.draw()
        log1.move()
        ### LOG 2 ###
        log2.draw()
        log2.move()
        ### LOG 3 ###
        log3.draw()
        log3.move()
        ##### KEEP LOG SCROLLING #####
        if log1.rect.x > SCREEN_WIDTH:
            log1.rect.x = -500
        if log1.rect.y > SCREEN_HEIGHT:
            log1.rect.y = -500

        if log2.rect.x > SCREEN_WIDTH:
            log2.rect.x = -300
        if log2.rect.y > SCREEN_HEIGHT:
            log2.rect.y = -300

        if log3.rect.x > SCREEN_WIDTH:
            log3.rect.x = -100
        if log3.rect.y > SCREEN_HEIGHT:
            log3.rect.y = -100
        ###############################
##############################################################
        
######################### GAME OVER ##########################
def game_over():
    global game_end     # idk

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
    sub.rect.bottom = SUB_Y
    ### DRAW SUBMARINE ###
    sub.draw()

    ### GAME OVER WORDS ###
    screen.blit(end, (10, 200))

    ##### RESET LOG #####
    log1.rect.x = -100
    log1.rect.y = 0

    log2.rect.x = -150
    log2.rect.y = 0

    log3.rect.x = -200
    log3.rect.y = 0
    ###############################

##############################################################

### THE MAIN LOOP ###
run = True
while run:

    # EVENTS
    for event in pygame.event.get():
        ### IF USER CLICKS EXIT WINDOW< GAME QUITS ###
        if event.type == pygame.QUIT:
            ### BREAK THE LOOP ###
            run = False

        ### WHEN KEY GOES UP, INCREMENT SCORE BY 1 ###
        if event.type == pygame.KEYUP:
            score += 1
            ### IF GAME OVER, RESET SCORE ###
            if game_end == True:
                score = 0
        
    ### IF USER PRESSES SPACE BAR, RESTART GAME ###
    restart = pygame.key.get_pressed()
    if (restart[K_SPACE]) == True:
        ### RESET VARIABLES ###
        collision = False
        starting = True
        game_end = False

    ### CHECK IF SPACE BAR IS PRESSED TO BEGIN GAME ###
    pressed = pygame.key.get_pressed()
    if (pressed[K_SPACE]) == True:
        starting = True

    ########## GAME NOT YET BEGUN #############
    if starting == False and game_end == False:
        ### CALL START MENU ###
        start_menu()

    ####### SPACE BAR PRESSED, GAME BEGINS #######
    elif starting == True and game_end == False:
        ### CALL START GAME ###
        game_start()
        ### START TIMER ###
        time = pygame.time.get_ticks() # DOESNT WORK HERE
        ### DRAW SCORE ###
        draw_text(str(score), font, white, 20, 20)

        ############# SCROLLING ##############
        ### SCROLL THE BACKGROUND ###
        scroll += SCROLL_SPEED
        if abs(scroll) > 650:
            scroll = 0
        ### SCROLL OCEAN FLOOR OFF SCREEN ###
        sand_scroll += SCROLL_SPEED
        if abs(sand_scroll) > 120:
            sand_scroll = 120
        ######################################

        ##################### GAME OVER CONDITIONS ######################
        ###### IF SUB COLLIDES WITH LOG OR IF SUB FALLS OFF SCREEN ######
        if sub.rect.colliderect(log1) or sub.rect.colliderect(log2)  or sub.rect.colliderect(log3) or sub.rect.top > SCREEN_HEIGHT + 80:
            collision = True
            fell_off = False
            game_end = True
            starting = False
            scroll = 0
            sand_scroll = 0
            game_over()
        #################################################################

        ##################### SCORE TRACKER #####################
        if game_end == True:
            if score > hi_score:
                hi_score = score                
            score = 0  
            log1.rect.x = 0
            log1.rect.y = 0        
            log2.rect.x = 0
            log2.rect.y = 0      
            draw_text(str("Hi-Score: "), font, white, 75, 300)
            draw_text(str(hi_score), font, white, 275, 300)
        ##########################################################

    ### UPDATE DISPLAY ###
    pygame.display.update()

### QUIT WINDOW ###
pygame.quit()
