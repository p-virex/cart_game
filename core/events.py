import pygame

from core.keys import MOUSE_LEFT_BUTTON, MOUSE_RIGHT_BUTTON, MOUSE_MIDDLE_BUTTON
from core.logger import logger
from game.constants import BIG_CARD_WIDTH, BIG_CARD_HEIGHT, BASE_CARD_WIDTH, BASE_CARD_HEIGHT, DEBUG


class EventsController:
    def __init__(self, player, deck, render, game, deck_image, buttons):
        self.p = player
        self.d = deck
        self.r = render
        self.g = game
        self.d_i = deck_image
        self.b = buttons
        self.running = True

    def run(self, events):

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == MOUSE_LEFT_BUTTON:
                if self.b.rect.collidepoint(event.pos):
                    if not self.p.made_turn and self.g.game_deck and self.g.turn_bot:
                        # забрать карты если не чем отбиться
                        self.g.pick_up_cards(self.p)
                        logger.info('Игрок забрал колоду')
                        del self.p.made_turn
                        del self.g.bot.made_turn
                        self.g.check_cards_in_hands()
                        return
                    if self.g.bot.made_turn and self.g.game_deck and not self.g.turn_bot:
                        self.g.clear_game_deck()
                        del self.g.bot.made_turn
                        logger.info('Игрок отдал ход')
                        self.g.set_player_turn(self.g.bot)
                        return
                if self.d_i.rect.collidepoint(event.pos) and DEBUG:
                    # добавляем карту в руку игрока по клику на колоду, для отладки
                    self.p.add_cart(self.d.get_card)
                    logger.info('Get card from deck')
                    return
                for card in self.p.hand:
                    if card.check_click(event.pos) and self.p.active_card and card.name == self.p.active_card.name:
                        # проверем, что игрок кликнул по активной карте
                        if self.g.turn_bot:
                            # если ходит бот, то мы защищаемся
                            self.p.player_defend_event(self.g)
                            return
                        else:
                            if not self.g.game_deck:
                                self.p.first_player_turn(self.g)
                            else:
                                self.p.player_turn(self.g)
                            return
                    if card.check_click(event.pos) and not self.p.active_card:
                        # активируем карту игрока, которой он намерен ходить
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
