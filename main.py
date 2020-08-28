# импорт библиотеки
import pygame

# импорт модулей
from core.button import Button
from core.events import EventsController
from core.game import GameController
from core.logger import logger
from core.render import Render
from core.service import load_image_card
from game.card import DeckBackOfCard
from game.constants import GREEN_TABLE, GAME_DECK_WIDTH, GAME_DECK_HEIGHT, FPS, SIZE_WINDOW
from game.deck import Deck
from game.player import Player

# инициализация pygame
pygame.init()

# установим название окна
pygame.display.set_caption('Дурак')

# устанавливаем размер окна и сохраняем объект
screen = pygame.display.set_mode(SIZE_WINDOW)
# заполняем поле зеленым цветом
screen.fill(GREEN_TABLE)
# объект вреиени для контролирования кол-ва кадров
clock = pygame.time.Clock()

# создаем колоду карт
deck = Deck()
deck.make_deck()
# перетусуем колоду
deck.shuffle_deck()

# создаем 2 игроков и как нибудь их называем
player = Player(name='Player')
bot = Player(name='Bot')

# объект рендер отвечает за отрисовку и позиционирование некоторых объектов
render = Render(screen, player)

# объект для контроля хода игры
game = GameController(render, deck)
# устанавливаем козырную карту
game.set_trump_card()
# определяем игрока который играет из окна
game.set_client_player(player)
# раздаем игрокам стартовое кол-во карт
game.add_start_card(player)
game.add_start_card(bot)

# изображение карт бота, просто рубашка карт
bot_card = load_image_card((100, 150), 'back_of_a_card')

# группа кнопки клика по колоде, используем для отладки
buttons_group = pygame.sprite.Group()
deck_image_group = pygame.sprite.Group()

# группа для сброса карт, отбой
db = DeckBackOfCard()
deck_image_group.add(db)

# кнопка для игрока. забрать колоду или отдать ходе если не чем ходить
button = Button('button')
buttons_group.add(button)

# определяем кто хъодит первым
game.check_first_attacker()

# объект для контроля событий игрока
events = EventsController(player, deck, render, game, db, button)
clock.tick(FPS)

# основной цикл в котором производим проверку, отрисовку
while events.running:
    # обновляем поле, убираем все объекты
    screen.fill(GREEN_TABLE)
    # перед отрисовкой всего остального проверка, что нет победителя
    if game.winner:
        render.draw_text(f"Победил: {game.winner}", (GAME_DECK_WIDTH/2+200, GAME_DECK_HEIGHT/2), size=50)
        events.run(pygame.event.get())
        game.game_deck.draw(screen)
        pygame.display.flip()
        continue
    # рисуем козырь
    game.render_trump_card()
    # рисуем карты бота
    render.render_image(bot_card, (450, 155))
    # рисуем колоду
    deck_image_group.draw(screen)
    # рисуем карты в руке игрока
    player.hand.draw(screen)
    # рисуем игровую колоду
    game.game_deck.draw(screen)
    # рисуем кнопку
    buttons_group.draw(screen)
    # рисуем весь текст
    render.draw_text("Козырь:", (40, 230))
    render.draw_text(f"Карты в руке: {player.len_hand}", (GAME_DECK_WIDTH, 550))
    render.draw_text(f"Карты в руке бота: {bot.len_hand}",  (5, 5))
    render.draw_text(f"Игровая колода: {game.len_game_deck}, ходит: {game.name_turn_player}", (GAME_DECK_WIDTH-50, GAME_DECK_HEIGHT-30))
    render.draw_text(f"Колода: {deck.get_len_deck}", (1050, 250))
    render.draw_text(f"Отбой: {game.len_clear_cards}, карт", (1045, 525))
    text = "Отдать ход" if not game.turn_bot else "Забрать карты"
    render.draw_text(text, (1040, 493))
    # проверяем собтия игрока
    events.run(pygame.event.get())
    # рисуем карты игрока
    render.draw_pl_cards()
    # обновляем экран
    pygame.display.flip()
    # проверяем игровые события
    game.game()


logger.info('Exit')
pygame.quit()
