import asyncio

import pygame

from random import randint
from resource import load_image
from sprites import Plasma, Snipper, Gun, Bullet

WIDTH, HEIGHT = 660, 460
FPS = 60
# --- Cấu hình ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bắn hạ zombie 3")
clock = pygame.time.Clock()
# --- Tải hình ảnh ---
background = load_image('background.png', (WIDTH, HEIGHT))
plasma_img = load_image('plasma.png', (6, 6))
snipper_img = load_image('snipper.svg', (33, 57))
gun_img = load_image('gun.svg', (59, 28))
bullet_img = load_image('bullet.svg', (10, 10))
plasmas = pygame.sprite.Group()
snipers = pygame.sprite.Group()

for i in range(15):
    plasmas.add(Plasma(plasma_img, (randint(0, 640), 460)))
sniper = Snipper(snipper_img, (150, 350))
snipers.add(sniper)
snipers.add(Gun(gun_img, (sniper.get_pos()[0]+10, sniper.get_pos()[1]+6)))
snipers.add(Bullet(bullet_img, (sniper.get_pos()[0]+10, sniper.get_pos()[1]+6)))

async def main():
    running = True
    while running:
        screen.blit(background, (0, 0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for ele in snipers:
            ele.update(mouse_pos=(mouse_x, mouse_y))
        snipers.draw(screen)
        for plasma in plasmas:
            plasma.update()
        plasmas.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)
    pygame.quit()

if __name__ == '__main__':
    asyncio.run(main())