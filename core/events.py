import pygame

from core.keys import MOUSE_LEFT_BUTTON, MOUSE_RIGHT_BUTTON, MOUSE_MIDDLE_BUTTON
from core.logger import logger
from game.constants import BIG_CARD_WIDTH, BIG_CARD_HEIGHT, BASE_CARD_WIDTH, BASE_CARD_HEIGHT, DEBUG


class Events:
    def __init__(self, player, deck, render, game, deck_image):
        self.p = player
        self.d = deck
        self.r = render
        self.g = game
        self.d_i = deck_image
        self.running = True

    def run(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == MOUSE_LEFT_BUTTON:
                if self.d_i.rect.collidepoint(event.pos):
                    self.p.add_cart(self.d.get_card)
                    logger.info('Get card from deck')
                    return
                for card in self.p.hand:
                    if card.check_click(event.pos) and self.p.active_card and card.name == self.p.active_card.name:
                        logger.info(f'Is active card: {self.p.active_card.name}')
                        self.g.add_card_in_game_deck(self.p.active_card)
                        self.p.remove_card(self.p.active_card)
                        del self.p.active_card
                        return
                    if card.check_click(event.pos) and not self.p.active_card:
                        card.change_scale(BIG_CARD_WIDTH, BIG_CARD_HEIGHT)
                        self.p.active_card = card
                        break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == MOUSE_RIGHT_BUTTON:
                for card in self.p.hand:
                    if card.check_click(event.pos) and self.p.active_card:
                        card.change_scale(BASE_CARD_WIDTH, BASE_CARD_HEIGHT)
                        if card == self.p.active_card:
                            del self.p.active_card
                        break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == MOUSE_MIDDLE_BUTTON and DEBUG:
                self.p.add_cart(self.d.get_card)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE and DEBUG:
                if self.p.active_card:
                    self.p.remove_card(self.p.active_card)
                    del self.p.active_card
