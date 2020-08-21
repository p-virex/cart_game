from pprint import pprint

import pygame

from core.game import GameController
from core.logger import logger
from core.render import RenderCard
from game.constants import GREEN_TABLE, BASE_CARD_WIDTH, BASE_CARD_HEIGHT, BIG_CARD_WIDTH, BIG_CARD_HEIGHT
from game.deck import Deck
from game.player import Player


FPS = 60

pygame.init()
pygame.display.set_caption('Card game')
screen = pygame.display.set_mode((1200, 800))
screen.fill(GREEN_TABLE)
clock = pygame.time.Clock()

pygame.display.update()
render = RenderCard(screen)

deck = Deck()
deck.make_deck()
deck.shuffle_deck()

player = Player()
game = GameController(render, deck)
game.set_trump_card()
game.set_client_player(player)
game.add_start_card()

running = True


while running:
    clock.tick(FPS)
    render.hide_all()
    player.arm.draw(screen)
    game.render_trump_card()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, card in enumerate(player.arm):
                if card.check_click(event.pos) and not player.active_card:
                    card.change_scale(BIG_CARD_WIDTH, BIG_CARD_HEIGHT, i)
                    player.active_card = card
                    break
            # player.remove_card(player.arm[-1])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for i, card in enumerate(player.arm):
                if card.check_click(event.pos) and player.active_card:
                    card.change_scale(BASE_CARD_WIDTH, BASE_CARD_HEIGHT, i)
                    if card == player.active_card:
                        del player.active_card
                    break

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            player.add_cart(deck.get_card)

            print('!!!')
            # player.remove_card(player.arm[-1])
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
            if player.active_card:
                player.remove_card(player.active_card)
                del player.active_card
                print('@@@@')
    player.draw_pl_cards()

    pygame.display.flip()

pygame.quit()
