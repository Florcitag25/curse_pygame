import pygame

class Weapon():
    def __init__(self,image):
        self.original_image = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.shape = self.image.get_rect()

    def draw_weapon(self,interface):
        interface.blit(self.image,self.shape)
        
    def update_weapon(self, character):
        self.shape.center = character.shape.center