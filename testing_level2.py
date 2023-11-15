####################################################
### Please refer to the README for directions :) ###
####################################################

### IMPORTING NECCESSARY LIBRARIES ###
import pygame
from pygame import * 
from pygame import mixer
import random

### INITIALIZING ###
pygame.init()
mixer.init()

### HIDE MOUSE CURSOR ###
pygame.mouse.set_visible(False)

### DEFINE A FONT ###
font = pygame.font.SysFont('Bauhaus 93', 50)
### COLOR FOR TEXT ###
white = ((255, 255, 255))

############### AUDIO UPLOADING AND VOLUME ##################
### IF GAME IS STARTED, UPLOAD BG AUDIO AND PLAY ###

#############################################################

######################### CONSTANTS #########################
SCREEN_WIDTH = 400      # width of the entire window (x-axis)
SCREEN_HEIGHT = 650     # height of the entire window (y-axis)
SCROLL_SPEED = .5      # speed of the scroll
SUB_X = 200             # initial x coordinate of submarine
SUB_Y = 590             # initial y coordinate of submarine
#############################################################

###################### VARIABLES ############################
scroll = 0             # scroll for the bg
sand_scroll = 0        # scroll for ocean floor 
ocean_scroll = 0       # scroll for ocean bg
sky_scroll = 0        # scroll for sky bg
starting = False       # start playing boolean
game_end = False       # game over boolean
score = 0              # score !
hi_score = 0           # hi-score !
#############################################################

################### DRAW SCREEN, NAME IT, AND SET ICON ##################
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sub Surge')
icon = pygame.image.load('sub-surge/img/submarine.png')
pygame.display.set_icon(icon)
#########################################################################

############### UPLOADING AND RESIZING IMAGES ################
bg_ocean = pygame.image.load('sub-surge/img/ocean_bg.png')
bg_sky = pygame.image.load('sub-surge/img/sky_bg.png')
sand = pygame.image.load('sub-surge/img/sand.jpg')
seaweed = pygame.image.load('sub-surge/img/seaweed.png')
submarine = pygame.image.load('sub-surge/img/submarine.png')
airplane = pygame.image.load('sub-surge/img/plane.png')
title = pygame.image.load('sub-surge/img/sub_surge.png')
start1 = pygame.image.load('sub-surge/img/press.png')
start2 = pygame.image.load('sub-surge/img/space_bar.png')
start3 = pygame.image.load('sub-surge/img/to_start.png')
end = pygame.image.load('sub-surge/img/game_over_img.png')
log = pygame.image.load('sub-surge/img/log1.png')

bg_ocean = pygame.transform.scale(bg_ocean, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_sky = pygame.transform.scale(bg_sky, (SCREEN_WIDTH, SCREEN_HEIGHT))
sand = pygame.transform.scale(sand, (SCREEN_WIDTH, 150))
seaweed = pygame.transform.scale(seaweed, (50, 50))
submarine = pygame.transform.scale(submarine, (80, 80))
airplane = pygame.transform.scale(airplane, (100, 80))
title = pygame.transform.scale(title, (380, 60))
start1 = pygame.transform.scale(start1, (160, 40))
start2 = pygame.transform.scale(start2, (300, 40))
start3 = pygame.transform.scale(start3, (256, 40))
end = pygame.transform.scale(end, (380, 60))
log = pygame.transform.scale(log, (100, 25))
##############################################################

###################### THE SUBMARINE CLASS ########################
class Submarine():

    def __init__(self, x, y):
        self.image = submarine
        self.width = 80
        self.height = 45
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0

    ### HOPPING ###
    def hop(self):
        y_prime = 0
        gravity = .1

        ### GRAVITY ###
        self.vel_y += gravity
        y_prime += self.vel_y
        self.rect.y += y_prime

        ### PRESS UP ARROW TO HOP ###
        up_arrow = pygame.key.get_pressed()
        if up_arrow[pygame.K_SPACE] == True:
            self.vel_y = -2.

    ### DRAW SUBMARINE ###   
    def draw(self):
        screen.blit(self.image, (self.rect.x , self.rect.y - 30))
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
##############################################################

###################### THE PLANE CLASS ########################
class Airplane():

    def __init__(self, SUB_X, SUB_Y):
        self.image = airplane
        self.width = 80
        self.height = 45
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (SUB_X, SUB_Y)
        self.vel_y = 0

    ### HOPPING ###
    def hop(self):
        y_prime = 0
        gravity = .1

        ### GRAVITY ###
        self.vel_y += gravity
        y_prime += self.vel_y
        self.rect.y += y_prime

        ### PRESS UP ARROW TO HOP ###
        up_arrow = pygame.key.get_pressed()
        if up_arrow[pygame.K_SPACE] == True:
            self.vel_y = -2.

    ### DRAW SUBMARINE ###   
    def draw(self):
        screen.blit(self.image, (self.rect.x , self.rect.y - 30))
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
##############################################################


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
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

    ### MOVE OBSTACLES ###
    def move(self):
        ### MOVING THE X COORDINATE ###
        self.rect.x += self.speed
        ### MOVING THE Y COORDINATE ###
        self.rect.y += self.speed
##############################################################

### HELP HOW TO MAKE A LIST AND APPEND THIS IS SO HARD IM JUST A GIRL ###
### CREATE INSTANCES OF LOGS ###
### LOG 1 INITIAL POSITION ###
log1 = Obstacle(random.randint(-700, -600), random.randint(-25, 25))
### LOG 2 INITIAL POSITION ###
log2 = Obstacle(random.randint(-500, -200), random.randint(100, 200))
### LOG 3 INITIAL POSITION ###
log3 = Obstacle(random.randint(-100, 0), random.randint(300, 550))
### CREATE INSTANCE OF SUBMARINE ###
sub = Submarine(SUB_X, SUB_Y)
## CREATE INSTANCE OF PLANE ###
plane = Airplane(SUB_X, sub.rect.y)

################ THE TEXT ################
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
##########################################

################### THE START MENU ###########################
def start_menu():
    ###### INITIAL BG , GAME NOT YET STARTED ######
    ### OCEAN BG ### 
    screen.blit(bg_ocean, (0, 0))
    ### SAND ###
    screen.blit(sand, (0, 570))
    ### LEFTMOST SEAWEED ###
    screen.blit(seaweed, (65, 570))
    ### MIDDLE SEAWEED ###
    screen.blit(seaweed, (235, 580))
    ### RIGHTMOST SEAWEED ###
    screen.blit(seaweed, (300, 575))
    ##############################################

    ### DRAW SUB ###
    sub.draw()

    ### TITLE SCREEN ###
    ### SUB SURGE ###
    screen.blit(title, (10, 50))
    ### PRESS ###
    screen.blit(start1, (120, 200))
    ### SPACE BAR ###
    screen.blit(start2, (54, 300))
    ### TO START ###
    screen.blit(start3, (75, 400))
##############################################################

######################## GAME START OCEAN LEVEL ##########################
def game_start_ocean():
    ### IF THE GAME IS NOT OVER ###
    if game_end == False:
        ############ BG WITH NO SCROLLING ############
        ### OCEAN BG ### 
        screen.blit(bg_ocean, (0, ocean_scroll))
        screen.blit(bg_ocean, (0, ocean_scroll - 650))
        ### SAND ###
        screen.blit(sand, (0, 570 + sand_scroll))
        ### LEFTMOST SEAWEED ###
        screen.blit(seaweed, (65, 570 + sand_scroll))
        ### MIDDLE SEAWEED ###
        screen.blit(seaweed, (235, 580 + sand_scroll))
        ### RIGHTMOST SEAWEED ###
        screen.blit(seaweed, (300, 575 + sand_scroll))
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
        ##### KEEP LOGS SCROLLING #####
        ### PUT LOG1 X COORDINATE BACK ###
        if log1.rect.x > SCREEN_WIDTH:
            log1.rect.x = -500
        ### PUT LOG1 Y COORDINATE BACK ###
        if log1.rect.y > SCREEN_HEIGHT:
            log1.rect.y = -500
        ### PUT LOG2 X COORDINATE BACK ### 
        if log2.rect.x > SCREEN_WIDTH:
            log2.rect.x = -300
        ### PUT LOG2 Y COORDINATE BACK ###
        if log2.rect.y > SCREEN_HEIGHT:
            log2.rect.y = -300
        ### PUT LOG3 X COORDINATE BACK ###
        if log3.rect.x > SCREEN_WIDTH:
            log3.rect.x = -100
        ### PUT LOG3 Y COORDINATE BACK ###
        if log3.rect.y > SCREEN_HEIGHT:
            log3.rect.y = -100
        ###########################################
##############################################################


######################## GAME START SKY LEVEL ##########################
def game_start_sky():
    ############ BG WITH NO SCROLLING ############
    ### SKY BG ###
    screen.blit(bg_ocean, (0, ocean_scroll))
    screen.blit(bg_sky, (0, sky_scroll - 650))
    screen.blit(bg_sky, (0, sky_scroll - 1300))
    ##############################################

    ############## THE PLANE #############
    if sub.rect.y > ocean_scroll:
        ### DRAW SUB ###
        sub.draw()
        ### STOP USER FROM GOING UP OFF SCREEN ###
        if sub.rect.y < 17:
            sub.rect.y = 17
        ### PLAYER HOPPING ###
        sub.hop()
    else:
        ### DRAW SUB ###
        plane.draw()
        ### STOP USER FROM GOING UP OFF SCREEN ###
        if plane.rect.y < 17:
            plane.rect.y = 17
        ### PLAYER HOPPING ###
        plane.hop()
##########################################

    ############ THE OBSTACLES ###############
    ### CALLING THE LOGS ###
    ## LOG 1 ###
    log1.draw()
    log1.move()
    ### LOG 2 ###
    log2.draw()
    log2.move()
    ### LOG 3 ###
    log3.draw()
    log3.move()
    ##### KEEP LOGS SCROLLING #####
    ### PUT LOG1 X COORDINATE BACK ###
    if log1.rect.x > SCREEN_WIDTH:
        log1.rect.x = -500
    ### PUT LOG1 Y COORDINATE BACK ###
    if log1.rect.y > SCREEN_HEIGHT:
        log1.rect.y = -500
    ### PUT LOG2 X COORDINATE BACK ### 
    if log2.rect.x > SCREEN_WIDTH:
        log2.rect.x = -300
    ### PUT LOG2 Y COORDINATE BACK ###
    if log2.rect.y > SCREEN_HEIGHT:
        log2.rect.y = -300
    ### PUT LOG3 X COORDINATE BACK ###
    if log3.rect.x > SCREEN_WIDTH:
        log3.rect.x = -100
    ### PUT LOG3 Y COORDINATE BACK ###
    if log3.rect.y > SCREEN_HEIGHT:
        log3.rect.y = -100
    ###########################################
##############################################################

######################### GAME OVER ##########################
def game_over():
    ### DRAW BG WITH NO SCROLLING ###
    ### OCEAN BG ### 
    screen.blit(bg_ocean, (0, 0))
    ### SAND ###
    screen.blit(sand, (0, 570))
    ### LEFTMOST SEAWEED ###
    screen.blit(seaweed, (65, 570))
    ### MIDDLE SEAWEED ###
    screen.blit(seaweed, (235, 580))
    ### RIGHTMOST SEAWEED ###
    screen.blit(seaweed, (300, 575))
    ##################################

    ### SET SUB AT STARTING POSITION ###
    sub.rect.bottom = SUB_Y
    ### DRAW SUBMARINE ###
    sub.draw()

    ### GAME OVER WORDS ###
    screen.blit(end, (10, 200))

    ##### RESET LOGS FOR GAME RESTART #####
    ### LOG 1 RESET ###
    log1.rect.x = -100
    log1.rect.y = 0
    ### LOG2 RESET ###
    log2.rect.x = -150
    log2.rect.y = 0
    ### LOG3 RESET ###
    log3.rect.x = -200
    log3.rect.y = 0
    #######################################
##############################################################

### THE MAIN OCEAN LEVEL LOOP ###
ocean_run = True
while ocean_run:

    ### HANDLING EVENTS ###
    for event in pygame.event.get():
        ### IF USER CLICKS EXIT WINDOW< GAME QUITS ###
        if event.type == pygame.QUIT:
            ### BREAK THE LOOP ###
            ocean_run = False

        ### WHEN KEY GOES UP, INCREMENT SCORE BY 1 ###
        if event.type == pygame.KEYUP:
            score += 1

    ### IF USER PRESSES SPACE BAR, RESTART GAME ###
    restart = pygame.key.get_pressed()
    if (restart[K_SPACE]) == True:
        ### RESET VARIABLES ###
        starting = True
        game_end = False

    ########## GAME NOT YET BEGUN #############
    if starting == False and game_end == False:
        ### CALL START MENU ###
        start_menu()

    ####### SPACE BAR PRESSED, GAME BEGINS #######
    elif starting == True and game_end == False:
        ### CALL START GAME OCEAN LEVEL ###
        game_start_ocean()
        ### DRAW SCORE ###
        draw_text(str(score), font, white, 20, 20)

        ############# SCROLLING ##############
        ### SCROLL THE BACKGROUND ###
        ocean_scroll += SCROLL_SPEED
        ### IF SCREEN SCROLLS OFF, RESET ###
        if abs(ocean_scroll) > 650:
            ocean_scroll = 0
        ### SCROLL OCEAN FLOOR OFF SCREEN ###
        sand_scroll += SCROLL_SPEED
        ### IF OCEAN FLOOR SCROLLS OFF, KEEP OFF ###
        ######################################

        ##################### GAME OVER CONDITIONS #######################
        ###### IF SUB COLLIDES WITH LOGS OR IF SUB FALLS OFF SCREEN ######
        '''if sub.rect.colliderect(log1)\
            or sub.rect.colliderect(log2)\
            or sub.rect.colliderect(log3)\
            or sub.rect.top > SCREEN_HEIGHT:'''
            ### CHANGE VARIABLES FOR GAME OVER ###
        if sub.rect.top > SCREEN_HEIGHT:
            game_end = True
            starting = False
            ocean_scroll = 0
            sand_scroll = 0
            sky_scroll = 0
            game_over()
        #################################################################

        ##################### SCORE TRACKER #####################
        if game_end == True:
            if score > hi_score:
                hi_score = score
            ### SET SCORE TO 0 FOR NEW GAME ###              
            score = 0
            ### PAUSE BG MUSIC IF GAME OVER ###

            ### LOAD GAME OVER AUDIO AND PLAY FOR GAME OVER ###
            ### RESET LOGS POSITIONS ###
            ### LOG1 ###
            log1.rect.x = 0
            log1.rect.y = 0
            ### LOG2 ###       
            log2.rect.x = 0
            log2.rect.y = 0
            ### LOG3 ### 
            log3.rect.x = 0
            log3.rect.y = 0
            ### DRAW HIGH SCORE ###    
            draw_text(str("Hi-Score: "), font, white, 75, 300)
            draw_text(str(hi_score), font, white, 275, 300)
        ##########################################################

    ################## THE SKY LEVEL #########################
    ### IF SCORE IS GREATER THAN 150, MOVE ON TO SKY LEVEL ###
    if score > 5 and ocean_scroll == 0 and game_end == False:                
        ### THE MAIN SKY LEVEL LOOP ###
        sky_run = True
        while sky_run:

                ### HANDLING EVENTS ###
            for event in pygame.event.get():
                ### IF USER CLICKS EXIT WINDOW< GAME QUITS ###
                if event.type == pygame.QUIT:
                    ### BREAK THE LOOP ###
                    sky_run = False

                ### WHEN KEY GOES UP, INCREMENT SCORE BY 1 ###
                if event.type == pygame.KEYUP:
                    score += 1

            ####### THE SKY LEVEL GAME STARTING #######
            if starting == True and game_end == False:
                ### CALL START SKY LEVEL ###
                game_start_sky()
                ### DRAW SCORE ###
                draw_text(str(score), font, white, 20, 20)

                ############# SCROLLING ##############
                ### SCROLL THE BACKGROUND ###
                sky_scroll += SCROLL_SPEED
                ### IF SCREEN SCROLLS OFF, RESET ###
                if abs(sky_scroll) > 1300:
                    sky_scroll = 650
                ### SCROLL OCEAN AWAY ###
                ocean_scroll += SCROLL_SPEED
                if abs(ocean_scroll) > 650:
                    ocean_scroll = 650
                ######################################

                ##################### GAME OVER CONDITIONS #######################
                ###### IF SUB COLLIDES WITH LOGS OR IF SUB FALLS OFF SCREEN ######
                '''if plane.rect.colliderect(log1)\
                    or plane.rect.colliderect(log2)\
                    or plane.rect.colliderect(log3)\
                    or plane.rect.top > SCREEN_HEIGHT:'''
                    ### CHANGE VARIABLES FOR GAME OVER ###
                if plane.rect.top > SCREEN_HEIGHT + 180:
                    print(plane.rect.top)
                    
                    game_end = True
                    starting = False
                    game_over()
                #################################################################
                ##################### SCORE TRACKER #####################
                if game_end == True:
                    if score > hi_score:
                        hi_score = score
                    ### SET SCORE TO 0 FOR NEW GAME ###              
                    score = 0
                    ### DRAW HIGH SCORE ###    
                    ### DRAW HIGH SCORE ###    
                    draw_text(str("Hi-Score: "), font, white, 75, 300)
                    draw_text(str(hi_score), font, white, 275, 300)
                    break
                game_over()

            ### UPDATE DISPLAY ###
            pygame.display.update()

    ### UPDATE DISPLAY ###
    pygame.display.update()

### QUIT WINDOW ###
pygame.quit()
