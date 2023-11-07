# import pygame library
import pygame
from pygame import * 

# import music
from pygame import mixer

# import time
import time

# initialize pygame
pygame.init()

# initalize the music
mixer.init()

# load audio files
mixer.music.load('shape-scape/audio/bg_music.mp3')

# set volume
mixer.music.set_volume(1)
    
# play the music
mixer.music.play()

# variables
run = True
screen_width = 400     # width of the entire window (x-axis)
screen_height = 650    # height of the entire window (y-axis)
scroll = 0             # scroll for the bg
sand_scroll = 0        # scroll for ocean floor to disappear and not repeat
log_scroll = 0         # scroll for logs
scroll_speed = .15     # speed of the scroll
subX = 200             # initial x coordinate of submarine
subY = 590             # initial y coordinate of submarine
hopping = False        # is player hopping or no
game_over = False      # has player hit obstacle
starting = False       # has player pressed SPACE BAR to start
logX = 200
logY = 175
collision = False

# draw the screen 
screen = pygame.display.set_mode((screen_width, screen_height))

# name the screen
pygame.display.set_caption('ShapeScape')

# upload images
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

# resize images
bg = pygame.transform.scale(bg, (screen_width, screen_height))
sand = pygame.transform.scale(sand, (screen_width, 100))
seaweed = pygame.transform.scale(seaweed, (50, 50))
submarine = pygame.transform.scale(submarine, (80, 80))
title = pygame.transform.scale(title, (380, 60))
start1 = pygame.transform.scale(start1, (160, 40))
start2 = pygame.transform.scale(start2, (300, 40))
start3 = pygame.transform.scale(start3, (256, 40))
end = pygame.transform.scale(end, (380, 60))
log = pygame.transform.scale(log, (100, 25))

# hide mouse cursor
pygame.mouse.set_visible(False)

# the ship
class Submarine():

    def __init__(self, x, y):

        self.image = submarine
        self.width = 80
        self.height = 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0

    def hop(self):

        dy = 0
        gravity = .1

        # time
        clock = pygame.time.Clock()
        time = clock.get_time() 

        # GRAVITY
        self.vel_y += gravity
        dy += self.vel_y

        self.rect.y += dy

        if self.rect.bottom + dy > screen_height - 5:

            dy = 0
            self.vey_y = 0
            self.rect.y = subY
    
        up_arrow = pygame.key.get_pressed()

        # if UP ARROW is pressed, player hops up
        if up_arrow[pygame.K_UP] == True:
            
            # how high player hops after pressing UP ARROW
            self.vel_y = -2.
        
    def draw(self):
        screen.blit(self.image, (self.rect.x - 0, self.rect.y - 20))
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

class Obstacle():

    def __init__(self, x, y):

        self.image = log
        self.width = 100
        self.height = 25
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)

    def draw(self):
        
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

sub = Submarine(subX, subY)
log1 = Obstacle(logX - 200, logY)

# make a game_over function
def game_over():    # if collision = True, call this function

    # draw game over screen
    screen.blit(end, (10, 200))    

    # stop scrolling
    


### THE MAIN LOOP ###
while run: 

    # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            # break the loop
            run = False

    # check for user to press SPACE BAR
    pressed = pygame.key.get_pressed()
    if (pressed[K_SPACE]) == True:
        starting = True

    # draw background
    screen.blit(bg, (0, scroll))
    screen.blit(bg, (0, scroll - 650))

    # draw sand
    screen.blit(sand, (0, 550 + sand_scroll))

    # draw submarine
    sub.draw()
    
    if sub.rect.colliderect(log1.rect):
        collision = True

    # stop user from going up off screen
    if sub.rect.y < 17:
        sub.rect.y = 17

    # draw seaweed
    # left most seaweed
    screen.blit(seaweed, (65, 540 + sand_scroll))
    # middle seaweed
    screen.blit(seaweed, (235, 530 + sand_scroll))
    # right most seaweed
    screen.blit(seaweed, (300, 545 + sand_scroll))

    # until user presses SPACE BAR, title screen is drawn
    if starting == False:

        # draw title and start words
        screen.blit(title, (10, 50))
        screen.blit(start1, (120, 200))
        screen.blit(start2, (54, 300))
        screen.blit(start3, (75, 400))

    else:
        
        # player hopping
        sub.hop()

        log1.draw()

        # scroll the background
        scroll += scroll_speed
        if abs(scroll) > 650:
            scroll = 0

            if starting == True and game_over == True:
                scroll_speed = 0

        # scroll the ocean floor off screen
        sand_scroll += scroll_speed
        if abs(sand_scroll) > 100:
            sand_scroll = 120

        log1.rect.x += 1
        if log1.rect.x > 500:
            log1.rect.x = -100

    if collision == True:
        print("GAME OVER")
        game_over()
        # GOT COLLISION DETECTED 3

    # update the display
    pygame.display.update()

# quit the window
pygame.quit()