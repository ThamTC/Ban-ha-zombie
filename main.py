
import asyncio

import pygame

from random import randint

from pygame import Surface

from resource import load_image
from sprites import Plasma, Snipper, Gun, Bullet, Explosion

WIDTH, HEIGHT = 660, 460
FPS = 60
# --- Cấu hình ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bắn hạ zombie 3")
clock = pygame.time.Clock()
# --- Tải hình ảnh ---
background = load_image('background.png', 1.0)
plasma_img = load_image('plasma.png', 0.03)
snipper_img = load_image('snipper.svg')
gun_img = load_image('gun.svg')
bullet_img = load_image('bullet.svg', 0.12)
explosion1 = load_image('explosion1.svg', 0.7)
explosion2 = load_image('explosion2.svg', 0.6)
explosion3 = load_image('explosion3.svg', 0.6)
explosion4 = load_image('explosion4.svg', 0.6)
flash_img = load_image('flash.svg', 1.5)

plasmas = pygame.sprite.Group()
snipers = pygame.sprite.Group()
explosions = pygame.sprite.Group()
smokes = pygame.sprite.Group()

for i in range(15):
    plasmas.add(Plasma(plasma_img, (randint(0, 640), 460)))

sniper = Snipper(snipper_img, (150, 350))
snipers.add(sniper)
snipers.add(Gun(gun_img, (sniper.get_pos()[0]+10, sniper.get_pos()[1]+6)))
snipers.add(Bullet(bullet_img, (sniper.get_pos()[0]+10, sniper.get_pos()[1]+6)))

for i in range(5):
    explosion = Explosion(explosion3, (WIDTH//2, HEIGHT//2))
    explosion.set_alpha(0)
    smokes.add(explosion)

for i in (explosion1, explosion2, explosion4, flash_img):
    explosion = Explosion(i, (WIDTH//2, HEIGHT//2))
    explosion.set_alpha(0)
    explosions.add(explosion)

async def abc():
    await asyncio.sleep(0.05)


async def main():
    running = True
    explosion_task = None
    while running:
        screen.blit(background, (0, 0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for ele in snipers:
            ele.update()
        snipers.draw(screen)
        for plasma in plasmas:
            plasma.update()
        plasmas.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and explosion_task is None:
                tasks = [ele.animation_scale(speed=sp, start_time=d) for ele, sp, d in zip(explosions.sprites()[:3],(3,3,3),(0.1,0.0,0.0))]
                tasks_2 = [ele.animation_alpha(alpha=alp,speed=sp, start_time=d) for ele, alp, sp, d in zip(explosions.sprites()[:3],(200,70,150),(3,3,3),(0.1,0.0,0.0))]
                tasks.extend(tasks_2)
                tasks_3 = [smokes.sprites()[i].animation_move() for i in range(5)]
                tasks_4 = [smokes.sprites()[i].animation_alpha(alpha=200, speed=3) for i in range(5)]
                tasks.extend(tasks_3)
                tasks.extend(tasks_4)
                flash_task = explosions.sprites()[-1].animation_alpha(alpha=100, speed=6)
                tasks.append(flash_task)
                explosion_task = asyncio.gather(*tasks)
                snipers.sprites()[-1].move_to(target_pos=pygame.mouse.get_pos())
        if explosion_task is not None and explosion_task.done():
            explosion_task = None
        smokes.draw(screen)
        explosions.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)
    pygame.quit()

if __name__ == '__main__':
    asyncio.run(main())


