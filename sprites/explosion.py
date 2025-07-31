import asyncio
from random import choice

import pygame.sprite
from pygame import Surface


class Explosion(pygame.sprite.Sprite):
    def __init__(self, explosion_image:Surface, pos=(0,0)):
        super().__init__()
        self.original_image = explosion_image
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.original_size = self.rect.size
        self.vx = choice([-3,-2,-1,1,2,3])
        self.vy = choice([-3,-2,-1,1,2,3])
        self.old_center = self.rect.center

    def set_alpha(self, alpha):
        self.image.set_alpha(alpha)

    def set_size(self, scale):
        new_size = (int(self.original_size[0]*scale), int(self.original_size[1]*scale))
        self.image = pygame.transform.smoothscale(self.original_image, new_size)

    def update(self):
        pass

    async def animation_scale(self, speed:int=1, start_time:float=0.0):
        await asyncio.sleep(start_time)
        for i in range(0, 20, speed):
            scale_factor = i * 0.05
            new_size = (int(self.original_size[0] * scale_factor), int(self.original_size[1] * scale_factor))
            self.image = pygame.transform.smoothscale(self.original_image, new_size)
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            await asyncio.sleep(0.005)
        for i in range(40, 30, -1):
            scale_factor = i*0.025
            new_size = (int(self.original_size[0] * scale_factor), int(self.original_size[1] * scale_factor))
            self.image = pygame.transform.smoothscale(self.original_image, new_size)
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            await asyncio.sleep(0.005)

    async def animation_alpha(self, alpha:int=150, speed:int=1, start_time:float=0.0):
        await asyncio.sleep(start_time)
        for i in range(0, 20, speed):
            alpha_factor = i * 0.05
            new_alpha = int(alpha * alpha_factor)
            self.image.set_alpha(new_alpha)
            await asyncio.sleep(0.005)
        for i in range(10, -1, -1):
            alpha_factor = i*0.1
            new_alpha = int(alpha*alpha_factor)
            self.image.set_alpha(new_alpha)
            await asyncio.sleep(0.005)


    async def animation_move(self):
        self.rect.center = self.old_center
        self.set_size(choice([0.5, 0.4, 0.3]))
        for i in range(15):
            self.rect.x += self.vx
            self.rect.y += self.vy
            await asyncio.sleep(0.005)

        self.vx = choice([-2, -3, 3, 2])
        self.vy = choice([-2, -3, 3, 2])