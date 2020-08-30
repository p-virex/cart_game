import pygame

from game.constants import WIDTH_CARD_FOR_UI, ZONE_FOR_CARDS, MAX_ZONE_FOR_CARDS, WIDTH, WHITE


class Render:
    def __init__(self, screen, player):
        self.screen = screen
        self.p = player

    def render_image(self, image, pos):  # hor, ver - по нижнему правому углу
        image_rect = image.get_rect(bottomright=pos)
        self.screen.blit(image, image_rect)

    def draw_pl_cards(self):
        """
        Метод для отрисовки игровых карт в руке игрока.

        Карты располагаются в специально отведенной зоне, которая завсит от кол-ва карт в руке игрока.
        Определяем центр экрана по горизонтали, получаем зону в которой могут располагаться карты и определяем
        ширину самой заны для карт. Располагаем карты в зоне с сдвигом по горизонтале, для
        правильного вывода изображений.
        :return:
        """
        zone_cards = self.p.len_hand * WIDTH_CARD_FOR_UI
        # max_zone = ZONE_FOR_CARDS if self.p.len_hand < 10 else MAX_ZONE_FOR_CARDS
        max_zone = zone_cards if zone_cards <= MAX_ZONE_FOR_CARDS else MAX_ZONE_FOR_CARDS
        if zone_cards <= max_zone:
            start_pos = WIDTH/2 - zone_cards/2
            shift = WIDTH_CARD_FOR_UI
        else:
            start_pos = WIDTH/2 - max_zone/2
            shift = max_zone/self.p.len_hand
        for i, card in enumerate(sorted(self.p.hand, key=lambda x: x.rank, reverse=True)):
            v_pos = 595 if self.p.active_card and card.name == self.p.active_card.name else 645
            if self.p.len_hand > 10 and not i % 2:
                # располагаем карты в шахматном порядке, если карт больше 8
                v_pos -= 25
            card.set_position((start_pos, v_pos))
            start_pos += shift

    def draw_text(self, msg, pos, size=25):
        font = pygame.font.Font(None, size)
        text = font.render(msg,  1, WHITE)
        self.screen.blit(text, pos)


