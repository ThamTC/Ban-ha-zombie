import pygame.sprite
from pygame import Surface


class Snipper(pygame.sprite.Sprite):
    def __init__(self, snipper_image:Surface, pos=(0, 0)):
        super().__init__()
        self.original_image = snipper_image
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def get_pos(self):
        return self.rect.center
    def update(self, pos=(0,0), mouse_pos=(0,0)):
        if mouse_pos[0]<self.rect.x:
            self.image = pygame.transform.flip(self.original_image, flip_y=False, flip_x=True)
        else:
            self.image = pygame.transform.flip(self.original_image, flip_y=False, flip_x=False)