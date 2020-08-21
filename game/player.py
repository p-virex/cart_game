import pygame


class Player(object):
    def __init__(self):
        self.__arm = pygame.sprite.Group()
        self._active_card = None

    active_card = property()

    @active_card.getter
    def active_card(self):
        return self._active_card

    @active_card.setter
    def active_card(self, card):
        self._active_card = card

    @active_card.deleter
    def active_card(self):
        self._active_card = None

    @property
    def arm(self):
        return self.__arm

    def add_cart(self, card):
        # 600 is centre, max zone for card > 630 pixels
        # start position 300 pxl for 6 cards
        # max zone = len cards * 105
        # if self.len_arm > 7:
        #     for card in self.arm:
        #         card.set_position(
        self.__arm.add(card)

    def draw_pl_cards(self):
        zone_cards = self.len_arm * 105
        max_zone = 630 if self.len_arm < 15 else 1050
        if zone_cards <= max_zone:
            start_pos = 600 - zone_cards/2
            shift = 105
        else:
            start_pos = 600 - max_zone/2
            shift = max_zone/self.len_arm
        for i, card in enumerate(self.arm):
            v_pos = 595 if self.active_card and card.name == self.active_card.name else 645
            if self.len_arm > 8 and not i % 2:
                v_pos += 25
            card.set_position((start_pos, v_pos))
            start_pos += shift

    def remove_card(self, card):
        return self.__arm.remove(card)

    @property
    def len_arm(self):
        return len(self.arm)
