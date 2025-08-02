import math

import pygame.sprite
from pygame import Surface


class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_image:Surface, pos=(0,0)):
        super().__init__()
        self.original_image = bullet_image
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.current_pos = pos
        self.rect.center = pos
        self.target_pos = None
        self.speed = 20

    def update(self, mouse_pos=(0,0)):
        if self.target_pos:
            dx = self.target_pos[0] - self.rect.centerx
            dy = self.target_pos[1] - self.rect.centery
            distance = int((dx**2+dy**2)**0.5)
            if distance>5:
                step_x, step_y = dx/distance, dy/distance
                self.rect.centerx += step_x*self.speed
                self.rect.centery += step_y*self.speed
            else:
                self.target_pos = None
                self.rect.center = mouse_pos


    def move_to(self, target_pos=()):
        self.target_pos = target_pos
