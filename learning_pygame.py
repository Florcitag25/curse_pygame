#Import necessary libraries and created modules
import constants
import pygame
import sys
from character import Character
from weapons import Weapon

#Start pygame 
pygame.init()

#assign the dimensions of the game window to variables
width = constants.WINDOW_WIDTH
height = constants.WINDOW_HEIGHT

#Create the window
window = pygame.display.set_mode((width,height))

#Change the window title
pygame.display.set_caption("Bubu's game")

#Create a list where the images that are part of the character animation will be stored
animation = []

#Create a loop to open the animation images and change their scale, then append those images to the animation list
for i in range (11):
    img = pygame.image.load(constants.PATH_IMAGE+f"{i}.png")
    img = pygame.transform.smoothscale(img,(constants.SCALE_CHARACTER,constants.SCALE_CHARACTER))
    animation.append(img)

weapon_image = pygame.image.load(constants.PATH_WEAPON)

#Call the Character class to make an instance, with its initial position and list
character = Character(50,50,animation)

weapon = Weapon(weapon_image)

#Initialize booleans to move the character
move_up = False
move_down = False
move_left = False
move_right = False

#Create a clock to control how many times per second the following loop will run
clock = pygame.time.Clock()

#Create the game loop
while True:
    #Limit the loop to a certain number of times per second
    clock.tick(constants.FPS)

    #Change the window background color
    window.fill(constants.BG_COLOR)

    #Initialize movement variables
    delta_x = 0
    delta_y = 0

    #Check the boolean variables to move the character, to determine which way the character moves
    if move_up == True:
        delta_y = -constants.MOVEMENT

    if move_down == True:
        delta_y = constants.MOVEMENT

    if move_left == True:
        delta_x = -constants.MOVEMENT

    if move_right == True:
        delta_x = constants.MOVEMENT

    #Call the Character movement method to move the character
    character.move_character(delta_x,delta_y)

    #Call the Character update method to animate character
    character.update()

    weapon.update_weapon(character)

    #Call the Character draw method to draw the character and flip it horizontally if it moves to the left
    character.draw_character(window)

    weapon.draw_weapon(window)


    #Check the events, mainly if the user presses a key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            
            if event.key == pygame.K_w:
                move_up = True

            if event.key == pygame.K_d:
                move_right = True

            if event.key == pygame.K_s:
                move_down = True      

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False

            if event.key == pygame.K_w:
                move_up = False

            if event.key == pygame.K_d:
                move_right = False

            if event.key == pygame.K_s:
                move_down = False 
                
    #Refresh game window
    pygame.display.update()
