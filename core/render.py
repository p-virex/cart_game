import pygame


class RenderCard:
    def __init__(self, screen):
        self.screen = screen

    def render_image(self, image, pos): # hor, ver - по нижнему правому углу
        image_rect = image.get_rect(bottomright=pos)
        self.screen.blit(image, image_rect)

    @staticmethod
    def change_scale(image, scale):
        return pygame.transform.scale(image, (image.get_width()//scale, image.get_height()//scale))
