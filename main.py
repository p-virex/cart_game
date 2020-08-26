import pygame

from core.button import Button
from core.events import EventsController
from core.game import GameController
from core.logger import logger
from core.render import RenderCard
from core.service import load_image_card
from game.card import DeckBackOfCard
from game.constants import GREEN_TABLE, GAME_DECK_WIDTH, GAME_DECK_HEIGHT
from game.deck import Deck
from game.player import Player


FPS = 60

pygame.init()
pygame.display.set_caption('Card game')
screen = pygame.display.set_mode((1200, 800))
screen.fill(GREEN_TABLE)
clock = pygame.time.Clock()

pygame.display.update()

deck = Deck()
deck.make_deck()
deck.shuffle_deck()

player = Player('Player')
bot = Player('Bot')

render = RenderCard(screen, player)

game = GameController(render, deck)
game.set_trump_card()
game.set_client_player(player)
game.add_start_card(player)
game.add_start_card(bot)

bot_card = load_image_card((100, 150), 'back_of_a_card')
buttons_group = pygame.sprite.Group()
deck_image_group = pygame.sprite.Group()

db = DeckBackOfCard()
deck_image_group.add(db)

button = Button('button')
buttons_group.add(button)

game.check_first_attacker()

events = EventsController(player, deck, render, game, db, button)

while events.running:
    clock.tick(FPS)
    screen.fill(GREEN_TABLE)
    game.render_trump_card()
    render.render_image(bot_card, (450, 155))
    deck_image_group.draw(screen)
    player.hand.draw(screen)
    game.game_deck.draw(screen)
    buttons_group.draw(screen)
    render.draw_text(25, "Trump card:", (255, 255, 255), (5, 230))
    render.draw_text(25, f"Number of cards in hand: {player.len_hand}", (255, 255, 255), (5, 600))
    render.draw_text(25, f"The number of cards in the bot's hand: {bot.len_hand}", (255, 255, 255), (5, 5))
    render.draw_text(25, f"Game deck: {game.len_game_deck}, turn: {game.name_turn_player}", (255, 255, 255), (GAME_DECK_WIDTH-25, GAME_DECK_HEIGHT-30))
    render.draw_text(25, f"Deck: {deck.get_len_deck}", (255, 255, 255), (1050, 230))
    render.draw_text(25, f"Numbers clean cards: {game.len_clear_cards}", (255, 255, 255), (990, 550))
    text = "Отдать ход" if not game.turn_bot else "Забрать карты"
    render.draw_text(25, text, (255, 255, 255), (1040, 493))
    events.run(pygame.event.get())
    render.draw_pl_cards()
    pygame.display.flip()
    game.game()

logger.info('Exit')
pygame.quit()
