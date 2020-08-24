import os

import pygame


def load_image_card(size, name):
    path = os.path.normpath(os.path.join(os.getcwd(), 'res/carts/{}.png'.format(name)))
    image = pygame.image.load(path)
    return pygame.transform.scale(image, size)
