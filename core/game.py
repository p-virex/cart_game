from core.logger import logger
from game.constants import START_POS_PLAYER_ARM, POS_TRAMP_CARD, RANK_INDEX_NAME, COUNT_START_CARD


class GameController:
    def __init__(self, render, deck):
        self.__players = list()
        self.__client_player = None
        self.render = render
        self.deck = deck
        self.__trump_card = None

    def set_trump_card(self):
        self.__trump_card = self.deck.get_card
        if RANK_INDEX_NAME[self.__trump_card.rank] == 'ace':
            logger.warning('Ace for trump card: %s' % self.__trump_card.name)
            self.deck.return_card_in_deck(self.__trump_card)
            # todo: fix me
            self.__trump_card = self.deck.get_card
            logger.warning('New trump card: %s' % self.__trump_card.name)
        # logger.info(f'Set trump card: {self.__trump_card.name}')

    def render_trump_card(self):
        self.render.render_image(self.__trump_card.image, POS_TRAMP_CARD)

    def set_client_player(self, player):
        self.__client_player = player

    def add_start_card(self):
        for i in range(COUNT_START_CARD):
            card = self.deck.get_card
            self.__client_player.add_cart(card)
        self.__client_player.draw_pl_cards()

