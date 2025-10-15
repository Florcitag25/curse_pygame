import constants
import pygame

#Create Character class

class Character:
    def __init__(self,x,y,animation):
        self.flip = False
        self.animation = animation
        self.frame_index = 0
        self.update_time= pygame.time.get_ticks()
        self.image = self.animation[self.frame_index]
        self.shape = self.image.get_rect()
        self.shape.center = (x,y)

    def draw_character(self,interface):
        image_flip = pygame.transform.flip(self.image,flip_x=self.flip,flip_y=False)
        interface.blit(image_flip,self.shape)
        pygame.draw.rect(interface,constants.CHARACTER_COLOR, self.shape)

    def move_character(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False

        self.shape.x += delta_x
        self.shape.y += delta_y

    def update(self):
        cooldown_animation = 50
        self.image = self.animation[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
            if self.frame_index == len(self.animation) - 1:
                self.frame_index = 0
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        