# здесь подключаются модули
from pprint import pprint

import pygame

# здесь определяются константы, классы и функции
from core.game import GameController
from core.logger import logger
from core.render import RenderCard
from game.constants import GREEN_TABLE
from game.deck import Deck
from game.player import Player

FPS = 60

# здесь происходит инициация, создание объектов и др.
pygame.init()
pygame.display.set_caption('Card game')
screen = pygame.display.set_mode((1200, 800))
screen.fill(GREEN_TABLE)
clock = pygame.time.Clock()

# если надо до цикла отобразить объекты на экране
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
    game.render_player_cards()
    game.render_trump_card()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            render.hide_all()
            player.add_cart(deck.get_cart)
            print('!!')
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            print('@@@@@')
            player.remove_card(0)
            render.hide_all()

    # обновление экрана
    pygame.display.flip()

logger.info('Exit')
pygame.quit()
