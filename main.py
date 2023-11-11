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
SCROLL_SPEED = .15     # speed of the scroll
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
        '''if self.rect.bottom + dy > SCREEN_HEIGHT - 5:
            dy = 0
            self.vey_y = 0
            self.rect.y = subY'''

        ### PRESS UP ARROW TO HOP ###
        up_arrow = pygame.key.get_pressed()
        if up_arrow[pygame.K_SPACE] == True:
            self.vel_y = -2.
    
    ### DRAW SUBMARINE ###   
    def draw(self):
        screen.blit(self.image, (self.rect.x - 0, self.rect.y - 20))
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
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
        # if self.rect.x > SCREEN_WIDTH:
            # obstacles.append(Obstacle(0, random.randint(0, SCREEN_WIDTH)))
##############################################################

### HELP HOW TO MAKE A LIST AND APPEND THIS IS SO HARD IM JUST A GIRL ###
### CREATE INSTANCES OF LOGS ### 
log = Obstacle(random.randint(-200, 0), random.randint(25, SCREEN_WIDTH))

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
        ### DRAW SUB ###
        sub.draw()
        
        ### STOP USER FROM GOING UP OFF SCREEN ###
        if sub.rect.y < 17:
            sub.rect.y = 17
        
        ### PLAYER HOPPING ###
        sub.hop()

        log.move()
        log.draw()

        ### KEEP LOG SCROLLING ###
        if log.rect.x > SCREEN_WIDTH:
            log.rect.x = -50
        if log.rect.y > SCREEN_HEIGHT:
            log.rect.y = -50
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
        ### IF GAME OVER, PAUSE 2 SECS BEFORE PLAYER CAN RESTART ###
        if event.type == pygame.KEYDOWN:
            if game_end == True:
                pygame.time.delay(2000)

    ### IF USER PRESSES SPACE BAR, RESTART GAME ###
    restart = pygame.key.get_pressed()
    if (restart[K_SPACE]) == True:
        ### RESET VARIABLES ###
        collision = False
        starting = True
        game_end = False
        ### BEGIN GAME AGAIN ###
        if collision == False and fell_off == False:
            ### CALL START GAME ###
            game_start()

    ### CHECK IF SPACE BAR IS PRESSED TO BEGIN GAME ###
    pressed = pygame.key.get_pressed()
    if (pressed[K_SPACE]) == True:
        starting = True

    ########## GAME NOT YET BEGUN #############
    if starting == False and game_end == False:
        ### CALL START MENU ###
        start_menu()

    ####### SPACE BAR PRESSED, GAME BEGINS #######
    elif starting == True:
        ### CALL START GAME ###
        game_start()
        ### START TIMER ###
        time = pygame.time.get_ticks()
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

        ######## GAME OVER CONDITIONS ########
        ###### IF SUB COLLIDES WITH LOG ######
        if sub.rect.colliderect(log):
            collision = True
            fell_off = False
            game_end = True
            starting = False
            scroll = 0
            sand_scroll = 0
            game_over()
        ###### IF SUB FALLS OFF SCREEN #######
        if sub.rect.top > SCREEN_HEIGHT + 80:
            collision = False
            fell_off = True
            game_end = True
            starting = False
            scroll = 0
            sand_scroll = 0
            game_over()
        #######################################

        ##################### SCORE TRACKER #####################
        if game_end == True:
            log.rect.x = 0
            if score > hi_score:
                hi_score = score
                print("hi-score is:", hi_score)
                score = 0
            else:
                print("hi-score is: ", score)
                score = 0
            draw_text(str("Hi-Score: "), font, white, 75, 300)
            draw_text(str(hi_score), font, white, 275, 300)
        ##########################################################

    ### UPDATE DISPLAY ###
    pygame.display.update()

### QUIT WINDOW ###
pygame.quit()
