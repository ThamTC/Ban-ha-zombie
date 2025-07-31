import os.path

import pygame.image


def load_image(filename, scale:float=1.0):
    try:
        file_base = os.path.dirname(__file__)
        file_path = os.path.join(file_base, 'asset', filename)
        image = pygame.image.load(file_path).convert_alpha()
        new_size = (int(image.get_width()*scale), int(image.get_height()*scale))
        image = pygame.transform.smoothscale(image, size=new_size)
        return image
    except pygame.error as e:
        raise e