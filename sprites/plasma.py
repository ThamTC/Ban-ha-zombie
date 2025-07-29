from random import randint, choice

import pygame.sprite
from pygame import Surface


class Plasma(pygame.sprite.Sprite):
    def __init__(self, plasma_image:Surface, pos=(0,0)):
        super().__init__()
        self.original_image = plasma_image
        self.image = self.original_image
        self.image.set_alpha(250//2)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vx = choice([-1, -2, 1, 2])
        self.vy = choice([1, 2])
        self.alpha = 180


    def change_size(self, scale):
        resize = (int(self.original_image.get_size()[0]*scale), int(self.original_image.get_size()[1]*scale))
        self.image = pygame.transform.smoothscale(self.original_image, size=resize)


    def update(self, pos=(0,0), mouse_pos=(0,0)):
        self.rect.x += self.vx
        self.rect.y -= self.vy
        self.alpha -= choice([1, 2])
        self.image.set_alpha(self.alpha)
        if self.rect.x < 0 or self.rect.x > 640 or self.rect.y < 200:
            self.rect.center = (randint(0, 640), 460)
            self.vx = choice([-1, -2, 1, 2])
            self.vy = choice([1, 2])
            self.change_size(choice([1.0, 0.8, 0.6, 0.4, 0.2]))
            self.alpha = 250
            self.image.set_alpha(self.alpha)