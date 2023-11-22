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

### DEFINE A FONT ###
font = pygame.font.SysFont('', 50)
### COLOR FOR TEXT ###
white = ((255, 255, 255))

######################### AUDIO #############################
def bg_audio():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio/bg_music.ogg'))
bg_audio()
def game_over_audio():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('audio/game_over_audio.mp3'))
def coin_audio():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('audio/coin_audio.mp3'))
#############################################################

######################### CONSTANTS #########################
SCREEN_WIDTH = 400      # width of the entire window (x-axis)
SCREEN_HEIGHT = 650     # height of the entire window (y-axis)
SCROLL_SPEED = .5       # speed of the scroll
SUB_X = 200             # initial x coordinate of submarine
SUB_Y = 590             # initial y coordinate of submarine
#############################################################

###################### VARIABLES ############################
scroll = 0              # scroll for the bg
sand_scroll = 0         # scroll for ocean floor 
starting = False        # start playing boolean
game_end = False        # game over boolean
isplaying = False       # playing audio boolean
volume_on = True        # volume boolean
mouse_over_mute = False # mouse over the mute btn boolean
score = 0               # score !
hi_score = 0            # hi-score !
money = 0               # money counter
#############################################################

################### DRAW SCREEN, NAME IT, AND SET ICON ##################
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sub Surge')
icon = pygame.image.load('img/submarine1.png')
pygame.display.set_icon(icon)
#########################################################################

############### UPLOADING AND RESIZING IMAGES ################
bg_ocean = pygame.image.load('img/ocean_bg.png')
sand = pygame.image.load('img/sand.jpg')
seaweed = pygame.image.load('img/seaweed.png')
bottle = pygame.image.load('img/bottle.png')
submarine1 = pygame.image.load('img/submarine1.png')
submarine2 = pygame.image.load('img/submarine2.png')
skin_title = pygame.image.load('img/skin_title.png')
title = pygame.image.load('img/sub_surge.png')
start1 = pygame.image.load('img/press.png')
start2 = pygame.image.load('img/space_bar.png')
start3 = pygame.image.load('img/to_start.png')
mute_btn = pygame.image.load('img/mute_btn.png')
end = pygame.image.load('img/game_over_img.png')
log = pygame.image.load('img/log1.png')
boost_up = pygame.image.load('img/boostup.png')
coin = pygame.image.load('img/coin.png')
arrow_btn = pygame.image.load('img/arrow_btn.png')

bg_ocean = pygame.transform.scale(bg_ocean, (SCREEN_WIDTH, SCREEN_HEIGHT))
sand = pygame.transform.scale(sand, (SCREEN_WIDTH, 150))
seaweed = pygame.transform.scale(seaweed, (60, 60))
bottle = pygame.transform.scale(bottle, (20, 60))
bottle = pygame.transform.rotate(bottle, 90)
submarine1 = pygame.transform.scale(submarine1, (80, 80))
submarine2 = pygame.transform.scale(submarine2, (80, 80))
skin_title = pygame.transform.scale(skin_title, (320, 60))
title = pygame.transform.scale(title, (380, 60))
start1 = pygame.transform.scale(start1, (160, 40))
start2 = pygame.transform.scale(start2, (300, 40))
start3 = pygame.transform.scale(start3, (256, 40))
mute_btn = pygame.transform.scale(mute_btn, (40, 40))
end = pygame.transform.scale(end, (380, 60))
log = pygame.transform.scale(log, (100, 25))
boost_up = pygame.transform.scale(boost_up, (60, 100))
coin = pygame.transform.scale(coin, (25, 25))
arrow_btn = pygame.transform.scale(arrow_btn, (50, 50))
arrow1 = pygame.transform.rotate(arrow_btn, 0)
arrow2 = pygame.transform.rotate(arrow_btn, 180)
##############################################################

###################### THE SUBMARINE CLASS ########################
class Submarine():

    def __init__(self, x, y):
        ### EMPTY LIST FOR IMAGES ###
        self.images = []
        ### INDEX ###
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            ### CHANGING FILE NAME I FEEL SO SNEAKY FOR THIS ###
            img_not_resized = pygame.image.load(f'img/submarine{num}.png')
            img = pygame.transform.scale(img_not_resized, (80, 80))
            ### APPEND THE LIST OF IMAGES FOR MULTIPLE PLAYERS ###
            self.images.append(img)
        self.image = self.images[self.index]

        # increment num by 1 on right arrow click, decrease by 1 if left click to go through images
        # when index reaches 5, reset to 1

        # self.image = submarine1

        ### DIMENSIONS OF THE RECT ###
        self.width = 80
        self.height = 45
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        ### VELOCITY ###
        self.vel_y = 0

    ### HOPPING ###
    def hop(self):
        ### CHANGE IN Y ###
        y_prime = 0
        ### FORCE OF GRAVITY ###
        gravity = .1

        ### GRAVITY ON SUBMARINE ###
        self.vel_y += gravity
        y_prime += self.vel_y
        self.rect.y += y_prime

        ### PRESS UP ARROW TO HOP ###
        up_arrow = pygame.key.get_pressed()
        if up_arrow[pygame.K_SPACE] == True:
            ### VELOCITY OF SUBMARINE HOPPING UP ###
            self.vel_y = -2

    ### DRAW SUBMARINE ###   
    def draw(self):
        screen.blit(self.image, (self.rect.x , self.rect.y - 30))
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
##############################################################

###################### THE SUBMARINE SAIL CLASS ########################
################# THIS IS THE SECOND RECT OF THE SUB ###################
############### FOR A MORE ACCURATE COLLISION DETECTION ################
class Sail():
    
    def __init__(self, x, y):
        ### DIMENSIONS OF THE RECT ###
        self.width = 20
        self.height = 35
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        ### VELOCITY ###
        self.vel_y = 0

    ### HOPPING ###
    def hop(self):
        ### CHANGE IN Y ###
        y_prime = 0
        ### FORCE OF GRAVITY ###
        gravity = .1

        ### GRAVITY ON SUBMARINE ###
        self.vel_y += gravity
        y_prime += self.vel_y
        self.rect.y += y_prime

        ### PRESS UP ARROW TO HOP ###
        hopping = pygame.key.get_pressed()
        if hopping[pygame.K_SPACE] == True:
            ### VELOCITY OF SUBMARINE HOPPING UP ###
            self.vel_y = -2.
##############################################################

#################### THE OBSTACLES CLASS #####################
class Obstacle():

    def __init__(self, x, y):
        ### SET IMAGE TO RECTANGLE ###
        self.image = log
        ### DIMENSIONS OF THE RECT ###
        self.width = 100
        self.height = 25
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        ### SPEED OF THE LOGS ###
        ### DIFFERENT FROM THE SCROLL SPEED ###
        self.speed = 1

        ### MAKE THE GAME HARDER ###
        ### INCREASE OBSTACLE SPEED ###
        '''if score > 5:
            self.speed = 1
        elif score > 100:
            self.speed = 1.5
        elif score > 150:
            self.speed = 2
        elif score > 200: 
            self.speed = 3

        ### IF GAME IS OVER ###
        if game_end == True:
            ### SET SELF SPEED BACK TO 1 ###
            self.speed = 1'''

    ### DRAW OBSTACLES ###
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

    ### MOVE OBSTACLES RIGHT ###
    def move_right(self):
        ### MOVING THE X COORDINATE ###
        self.rect.x += self.speed
        ### MOVING THE Y COORDINATE ###
        self.rect.y += self.speed

    ### MOVE OBSTACLES LEFT ###
    def move_left(self):
        ### MOVING THE X COORDINATE ###
        self.rect.x -= self.speed
        ### MOVING THE Y COORDINATE ###
        self.rect.y += self.speed    
##############################################################

##################### COIN CLASS ####################
class Coin():

    def __init__(self, x, y):
        ### SET IMAGE TO RECTANGLE ###
        self.image = coin
        ### DIMENSIONS OF THE RECT ###
        self.width = 25
        self.height = 25
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        ### SPEED OF THE COIN ###
        ### DIFFERENT FROM THE SCROLL SPEED ###
        self.speed = 1

    ### DRAW COIN ###
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

    ### MOVE COIN RIGHT ###
    def move(self):
        ### MOVING THE X COORDINATE ###
        self.rect.x += self.speed

#####################################################

################### MUTE BUTTON ##########################
class Mute():

    def __init__(self, x, y):
        ### SET IMAGE TO RECTANGLE ###
        self.image = mute_btn
        ### DIMENSIONS OF THE RECT ###
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)

    ### DRAW MUTE BTN ###
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
###########################################################

################## ARROW BUTTON ###########################
class Arrow_Left():
    def __init__(self, x, y):
        ### SET IMAGE TO RECTANGLE ###
        self.image = arrow1
        ### DIMENSIONS OF THE RECT ###
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)

    ### DRAW MUTE BTN ###
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

class Arrow_Right():
    def __init__(self, x, y):
        ### SET IMAGE TO RECTANGLE ###
        self.image = arrow2
        ### DIMENSIONS OF THE RECT ###
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)

    ### DRAW MUTE BTN ###
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


################### CREATING ALL INSTANCES ###################
### CREATE INSTANCES OF OBSTACLES ###
### LOG 1 INITIAL POSITION ###
log1 = Obstacle(random.randint(-800, -700), random.randint(-25, 25))
### LOG 2 INITIAL POSITION ###
log2 = Obstacle(random.randint(-300, 0), random.randint(150, 550))
### LOG 3 INITIAL POSITION ###
log3 = Obstacle(random.randint(SCREEN_WIDTH + 100, 1000), random.randint(0, SCREEN_HEIGHT))
### CREATE INSTANCE OF SUBMARINE AND ITS SAIL ###
sub = Submarine(SUB_X, SUB_Y)
sub_sail = Sail(SUB_X - 10, SUB_Y - 25)
### CREATE INSTANCE OF COIN ###
coin = Coin(random.randint(-1000, -100), random.randint(0, 500))
### CREATE INSTANCE OF MUTE BTN ###
mute = Mute(375, 30)
### CREATE INSTANCES OF THE ARROW BTNS ###
arrow_left = Arrow_Left(120, 580)
arrow_right = Arrow_Right(270, 580)
##############################################################

################ THE TEXT #################
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
###########################################

################### THE START MENU ###########################
def start_menu():

    ### SHOW MOUSE CURSOR ###
    pygame.mouse.set_visible(True)

    ###### INITIAL BG , GAME NOT YET STARTED ######
    ### OCEAN BG ### 
    screen.blit(bg_ocean, (0, 0))
    ### SAND ###
    screen.blit(sand, (0, 570))
    ### LEFTMOST SEAWEED ###
    screen.blit(seaweed, (65, 560))
    ### MIDDLE SEAWEED ###
    screen.blit(seaweed, (235, 580))
    ### RIGHTMOST SEAWEED ###
    screen.blit(seaweed, (300, 575))
    ### POLLUTION LOL ###
    screen.blit(bottle, (35, 620))
    ##############################################

    ### DRAW SUB ###
    sub.draw()
    
    ### DRAW MUTE BUTTON ###
    mute.draw()

    ### TITLE SCREEN ###
    ### SUB SURGE ###
    screen.blit(title, (10, 50))
    ### PRESS ###
    screen.blit(start1, (120, 200))
    ### SPACE BAR ###
    screen.blit(start2, (54, 300))
    ### TO START ###
    screen.blit(start3, (75, 400))    

    ### DRAW ARROWS FOR CHANGING SKINS ###
    arrow_left.draw()
    arrow_right.draw()
##############################################################

######################## GAME START OCEAN LEVEL ##########################
def game_start_ocean():

    ### HIDE MOUSE CURSOR ###
    pygame.mouse.set_visible(False)

    ### IF THE GAME IS NOT OVER ###
    if game_end == False:
        ############ BG WITH NO SCROLLING ############
        ### OCEAN BG ### 
        screen.blit(bg_ocean, (0, scroll))
        screen.blit(bg_ocean, (0, scroll - 650))
        ### SAND ###
        screen.blit(sand, (0, 570 + sand_scroll))
        ### LEFTMOST SEAWEED ###
        screen.blit(seaweed, (65, 570 + sand_scroll))
        ### MIDDLE SEAWEED ###
        screen.blit(seaweed, (235, 580 + sand_scroll))
        ### RIGHTMOST SEAWEED ###
        screen.blit(seaweed, (300, 575 + sand_scroll))
        ### POLLUTION LOL ###
        screen.blit(bottle, (35, 620 + sand_scroll))
        ##############################################

        ################## THE COINS #################:
        ### DRAW COIN ###
        coin.draw()
        ### MOVE COIN ###
        coin.move()
        ### RESET COIN POSITION ###
        if coin.rect.x > SCREEN_WIDTH:
            coin.rect.x = random.randint(-1000, -100)
            coin.rect.y = random.randint(0, 500)

        ############## THE SUBMARINE #############
        ### DRAW SUB ###
        sub.draw()
        ### STOP USER FROM GOING UP OFF SCREEN ###
        if sub.rect.y < 17:
            sub.rect.y = 17
        if sub_sail.rect.y < 17:
            sub_sail.rect.y = 17
        ### PLAYER HOPPING ###
        sub.hop()
        sub_sail.hop()
        ##########################################

        ############ THE OBSTACLES ###############
        ### CALLING THE LOGS ###
        ### DRAWING AND MOVING ###
        ## LOG 1 ###
        log1.draw()
        log1.move_right()
        ### LOG 2 ###
        log2.draw()
        log2.move_right()
        ### LOG 4 ###
        log3.draw()
        log3.move_left()
        ##### KEEP LOGS SCROLLING #####
        ### PUT LOG1 X COORDINATE BACK ###
        if log1.rect.x > SCREEN_WIDTH:
            log1.rect.x = random.randint(-700, -600)
        ### PUT LOG1 Y COORDINATE BACK ###
        if log1.rect.y > SCREEN_HEIGHT:
            log1.rect.y = -300
        ### PUT LOG2 X COORDINATE BACK ###
        if log2.rect.x > SCREEN_WIDTH:
            log2.rect.x = random.randint(-400, -200)
        ### PUT LOG2 Y COORDINATE BACK ###
        if log2.rect.y > SCREEN_HEIGHT:
            log2.rect.y = -200
        ### PUT LOG3 X COORDINATE BACK ###
        if log3.rect.x < -100:
            log3.rect.x = 800
        ### PUT LOG3 Y COORDINATE BACK ###
        if log3.rect.y > SCREEN_HEIGHT:
            log3.rect.y = 0
        ###########################################
##############################################################

######################### GAME OVER ##########################
def game_over():

    ### SHOW MOUSE CURSOR ###
    pygame.mouse.set_visible(True)

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
    ### POLLUTION LOL ###
    screen.blit(bottle, (35, 620))
    ##################################

    ### SET SUB AT STARTING POSITION ###
    sub.rect.bottom = SUB_Y
    sub_sail.rect.bottom = sub.rect.bottom - 30
    ### DRAW SUBMARINE ###
    sub.draw()

    ### DRAW MUTE BUTTON ###
    mute.draw()

    ### GAME OVER WORDS ###
    screen.blit(end, (10, 200))

    ##### RESET LOGS FOR GAME RESTART #####
    ### LOG 1 RESET ###
    log1.rect.x = -100
    log1.rect.y = 0
    ### log2 RESET ###
    log2.rect.x = -400
    log2.rect.y = 0
    ### log3 RESET ###
    log3.rect.x = -250
    log3.rect.y = 0
    #######################################

    ### RESET COIN POS ###
    coin.rect.x = random.randint(-400, -100)

    ### DRAW HIGH SCORE ###    
    draw_text(str("Score: "), font, white, 75, 300)
    draw_text(str(score), font, white, 275, 300)
    ### DRAW CURRENT SCORE ###
    draw_text(str("Hi-Score: "), font, white, 75, 350)
    draw_text(str(hi_score), font, white, 275, 350)

    ### DRAW MONEY AMOUNT ###
    draw_text(str("Coins: "), font, white, 75, 400)
    draw_text(str("$"), font, white, 250, 400)
    draw_text(str(money), font, white, 275, 400)

    ### DRAW ARROWS FOR CHANGING SKINS ###
    arrow_left.draw()
    arrow_right.draw()
##############################################################

### THE MAIN OCEAN LEVEL LOOP ###
ocean_run = True
while ocean_run:

    ### GET MOUSE POSITION ###
    pos = pygame.mouse.get_pos()

    ### HANDLING EVENTS ###
    for event in pygame.event.get():
        ### IF USER CLICKS EXIT WINDOW ### 
        ### GAME QUITS ###
        if event.type == pygame.QUIT:
            ### BREAK THE LOOP ###
            ocean_run = False
            ### WINDOW WILL CLOSE HERE ###

        ### IF KEY GOES UP ###
        if event.type == pygame.KEYUP:
            ### INCREMENT SCORE BY 1 ### 
            score += 1
        
        ### MUTE AND UNMUTE MUSIC ###
        ### CHECK FOR MOUSE COLLISION WITH MUTE BUTTON ###
        if mute.rect.collidepoint(pos):
            ### IF LEFT MOUSE CLICKED ###
            if pygame.mouse.get_pressed()[0] == 1:
                ### IF VOLUME IS ALREADY ON ###
                if volume_on:
                    ### MUTE IT ###
                    pygame.mixer.music.set_volume(0)
                    ### CHANGE VOLUME BOOLEAN ###
                    volume_on = False
                ### IF VOLUME IS NOT ON ###
                elif not volume_on:
                    ### UNMUTE IT ###
                    pygame.mixer.music.set_volume(1)
                    ### CHANGE VOLUME BOOLEAN ###
                    volume_on = True
                
        ### CHECK FOR MOUSE COLLISION WITH ARROWS ###
        ### LEFT ARROW ###
        '''if arrow_left.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                print("left arrow clicked")
                print(pos)
        ### RIGHT ARROW ###
        if arrow_right.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                print("right arrow clicked")'''

    ### IF USER PRESSES SPACE BAR ###
    restart = pygame.key.get_pressed()
    if (restart[K_SPACE]) == True:
        ### RESTART GAME ###
        ### RESET BOOLEAN VALUES ###
        starting = True
        game_end = False
        if not isplaying:
            # resume the bg audio
            pygame.mixer.Channel(0).unpause()
            isplaying = True

    ########## GAME NOT YET BEGUN #############
    ### IF THE GAME IS NOT RUNNING/ STARTING AND GAME IS NOT OVER ###
    if starting == False and game_end == False:
        ### CALL START MENU ###
        start_menu()

    ############ THE GAME RUNNING HERE ############
    ####### SPACE BAR PRESSED, GAME BEGINS #######
    ### IF THE GAME IS RUNNING/ STARTING AND IS NOT GAME OVER ###
    elif starting == True and game_end == False:
        ### CALL START GAME OCEAN LEVEL ###
        game_start_ocean()
        
        ### DRAW SCORE ###
        draw_text(str(score), font, white, 20, 5)

        ### DRAW MONEY ###
        draw_text(str("$ "), font, white, 20, 55)
        draw_text(str(money), font, white, 45, 55)

        ############# SCROLLING ##############
        ### SCROLL THE BACKGROUND ###
        scroll += SCROLL_SPEED
        ### IF SCREEN SCROLLS OFF ###
        if abs(scroll) > 650:
            ### RESET SCROLL TO RESTART AT TOP OF SCREEN ###
            scroll = 0
        ### SCROLL OCEAN FLOOR OFF SCREEN ###
        ### INFINITELY SCROLLING OFF SCREEN UNTIL NEW GAME ###
        sand_scroll += SCROLL_SPEED
        ######################################

        ### MAKE THE GAME HARDER ###
        ### INCREASE BG SPEED ###
        if score > 50:
            SCROLL_SPEED = 1
        elif score > 100:
            SCROLL_SPEED = 1.5
        elif score > 150:
            SCROLL_SPEED = 2
        elif score > 200:
            SCROLL_SPEED = 3

        ### COLLECTING COINS ###
        if sub.rect.colliderect(coin):
            money += 1
            # play coin audio
            coin_audio()
            ### figure out channels and stuff tehehehe ###

        
        ##################### GAME OVER CONDITIONS #######################
        ###### IF SUB COLLIDES WITH LOGS OR IF SUB FALLS OFF SCREEN ######
        if sub.rect.colliderect(log1)\
            or sub_sail.rect.colliderect(log1)\
            or sub.rect.colliderect(log2)\
            or sub_sail.rect.colliderect(log2)\
            or sub.rect.colliderect(log3)\
            or sub_sail.rect.colliderect(log3)\
            or sub.rect.top > SCREEN_HEIGHT\
            or sub_sail.rect.top > SCREEN_HEIGHT:
            ### RESET THE BOOLEAN VALUES ###
                game_end = True
                starting = False
                ### RESET SCROLL POSITION ###
                scroll = 0
                sand_scroll = 0
                SCROLL_SPEED = 0.5
                ##################### SCORE TRACKER #####################
                ### IF GAME IS OVER ###
                if game_end == True:
                    ### IF SCORE IS GREATER THAN HI-SCORE ###
                    if score > hi_score:
                        ### SET HI-SCORE TO SCORE ###
                        hi_score = score
                    
                    ### PAUSE BG MUSIC IF GAME OVER ###

                    ### CALL GAME OVER AUDIO ###
                    game_over_audio()
                    pygame.mixer.Channel(0).pause()

                    ### RESET LOGS POSITIONS ###
                    ### LOG1 ###
                    log1.rect.x = random.randint(-500, 100)
                    log1.rect.y = 0
                    ### LOG2 ### 
                    log2.rect.x = random.randint(50, 200)
                    log2.rect.y = 0
                    ### LOG 3 ###
                    log3.rect.x = random.randint(600, 800)
                    log3.rect.y = 0
                    ############################

                    ### CALL GAME OVER ###
                    game_over()
                    isplaying = False

                    ### SET SCORE TO 0 FOR NEW GAME ###              
                    score = 0
                ##########################################################
        #################################################################

    ### UPDATE DISPLAY ###
    pygame.display.update()

### QUIT WINDOW ###
pygame.quit()

### WINDOW HAS CLOSED ###
######## GOODBYE ########
