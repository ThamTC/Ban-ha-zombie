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

    def update(self, pos=(0,0), mouse_pos=(0,0)):
        pass
