from core.logger import logger
from game.constants import START_POS_PLAYER_ARM, POS_TRAMP_CARD, RANK_INDEX_NAME


class GameController:
    def __init__(self, render, deck):
        self.__players = list()
        self.__client_player = None
        self.render = render
        self.deck = deck
        self.__trump_card = None

    def set_trump_card(self):
        self.__trump_card = self.deck.get_cart
        if RANK_INDEX_NAME[self.__trump_card.rank] == 'ace':
            logger.warning('Ace for trump card: %s' % self.__trump_card.name)
            self.deck.return_card_in_deck(self.__trump_card)
            # todo: fix me
            self.__trump_card = self.deck.get_cart
            logger.warning('New trump card: %s' % self.__trump_card.name)
        logger.info('Set trump card: %s' % self.__trump_card.name)

    def render_trump_card(self):
        card_object = self.render.change_scale(self.__trump_card.image, 4)
        self.render.render_image(card_object, POS_TRAMP_CARD)

    def set_client_player(self, player):
        self.__client_player = player

    def add_start_card(self):
        for i in range(6):
            self.__client_player.add_cart(self.deck.get_cart)

    def render_player_cards(self):
        len_arm = self.__client_player.len_arm
        # if len_arm <= 6:
        start_pos = START_POS_PLAYER_ARM
        shift_pos = 105 if len_arm <= 6 else 35
        for card in self.__client_player.arm:
            card_object = self.render.change_scale(card.image, 5)
            self.render.render_image(card_object, start_pos)
            start_pos = (start_pos[0] + shift_pos, start_pos[-1])


