import pygame

from core.service import load_image_card


class Button(pygame.sprite.Sprite):
    def __init__(self, name_button):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image_card((180, 80), name_button)  # 100 x 150 scale 5
        self.rect = self.image.get_rect()
        self.rect.x = 1010
        self.rect.y = 460

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
