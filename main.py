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

# resize images
bg = pygame.transform.scale(bg, (screen_width, screen_height))
sand = pygame.transform.scale(sand, (screen_width, 50))
seaweed = pygame.transform.scale(seaweed, (50, 50))
submarine = pygame.transform.scale(submarine, (125, 125))

# the ship
class Submarine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init()
        self.image = submarine
        self.rect = self.image.get_rect()
        self.rect.x = x    # x-coordinate of sprite's top left corner
        self.rect.y = y    # y-coordinate of sprite's top left corner
        self.vel = 0

    def update(self):
         
        if hopping == True:
             
            # GRAVITY LETS GO
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 600:
                self.rect.x -= int(self.vel)

            if game_over == False:
            # hopping
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:    # if left mouse bar clicked
                    self.clicked = True
                    self.vel = -8
                if pygame.mouse.get_pressed()[0] == 0:    # if left mouse bar not clicked
                    self.clicked = False
        

submarine_group = pygame.sprite.Group()

while run: 

     # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw background
    screen.blit(bg, (0, scroll))
    screen.blit(bg, (0, scroll - 600))

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