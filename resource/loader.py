import os.path

import pygame.image


def load_image(filename, resize=(100, 100)):
    try:
        file_base = os.path.dirname(__file__)
        file_path = os.path.join(file_base, 'asset', filename)
        image = pygame.image.load(file_path).convert_alpha()
        image = pygame.transform.smoothscale(image, size=resize)
        return image
    except pygame.error as e:
        raise e