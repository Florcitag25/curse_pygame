import pygame
import math

class Weapon():
    def __init__(self,image):
        self.original_image = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.shape = self.image.get_rect()

    def draw_weapon(self,interface):
        self.image= pygame.transform.rotate(self.image,self.angle)
        interface.blit(self.image,self.shape)

    def rotate_weapon(self, rotate):
        if rotate:
            image_flip = pygame.transform.flip(self.original_image,True,False)
        else:
            image_flip = pygame.transform.flip(self.original_image,False,False)

        self.image = pygame.transform.rotate(image_flip,self.angle)
        
    def update_weapon(self, character):
        self.shape.center = character.shape.center
        if character.flip ==False:
            self.shape.x += character.shape.width/2.5
            self.rotate_weapon(False)
        else:
            self.shape.x -= character.shape.width/2.5
            self.rotate_weapon(True)

        self.shape.y += 10

        #mover pistola con el mouse
        mouse_pos = pygame.mouse.get_pos()
        diff_x=mouse_pos[0] - self.shape.centerx
        diff_y=-(mouse_pos[1] - self.shape.centery)
        self.angle = math.degrees(math.atan2(diff_y,diff_x))
        print(self.angle)


