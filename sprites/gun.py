from math import radians, atan2, degrees

import pygame.sprite
from pygame import Surface, Vector2


class Gun(pygame.sprite.Sprite):
    def __init__(self, gun_image:Surface, pos=(0,0)):
        super().__init__()
        self.original_image = gun_image
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.current_pos = pos
        self.rect.center = pos

    def update(self, pos=(0,0), mouse_pos=(0,0)):

        # vector của mouse
        mouse_vt = Vector2(mouse_pos)
        # vector của gun
        gun_vt = Vector2(self.rect.center)
        # hướng xoay
        direction = mouse_vt-gun_vt
        # xác định góc xoay
        rad = atan2(direction.y, direction.x)
        if mouse_vt.x <= gun_vt.x:
            rad = rad*(-1)
        gun_angle = -degrees(rad)
        # xoay nhân vật gun
        self.image = pygame.transform.rotate(self.original_image, angle=gun_angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.current_pos
        if mouse_vt.x <= gun_vt.x:
            self.rect.center = (self.current_pos[0]-10, self.current_pos[1])
        if mouse_pos[0] <= self.rect.x:
            self.image = pygame.transform.flip(self.image, flip_y=True, flip_x=False)
        else:
            self.image = pygame.transform.flip(self.image, flip_y=False, flip_x=False)