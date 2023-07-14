import telebot
from telebot import types
from functions.get_player import get_player

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


def resize_keyboard_decorator(func):
    def wrapper(self, id_of_user, list_of_players):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        stop_button = types.KeyboardButton('Stop playing')
        restart_button = types.KeyboardButton('Start another game')
        balance_button = types.InlineKeyboardButton('Your balance - '
                                                    + str(get_player(id_of_user, list_of_players).currency))
        markup.add(restart_button, stop_button, balance_button)
        telegram_bot.send_message(id_of_user, "To restart game, press the button",
                                  reply_markup=markup)
        return func(self, id_of_user, list_of_players)

    return wrapper


class ResultOfGame:
    @resize_keyboard_decorator
    def winner(self, id_of_user, list_of_players):
        telegram_bot.send_message(id_of_user, "=========================")
        telegram_bot.send_message(id_of_user, "You Win!",
                                  parse_mode='html')
        get_player(id_of_user, list_of_players).set_currency_for_player()

    @resize_keyboard_decorator
    def loser(self, id_of_user, list_of_players):
        telegram_bot.send_message(id_of_user, "=========================")
        telegram_bot.send_message(id_of_user, f'<b>You Lose!</b>',
                                  parse_mode='html')
        get_player(id_of_user, list_of_players).set_currency_for_player()

    @resize_keyboard_decorator
    def draw(self, id_of_user, list_of_players):
        telegram_bot.send_message(id_of_user, "=========================")
        telegram_bot.send_message(id_of_user, f'<b>It is a draw!</b>',
                                  parse_mode='html')
        get_player(id_of_user, list_of_players).set_currency_for_player()

    @resize_keyboard_decorator
    def blackjack(self, id_of_user, list_of_players):
        telegram_bot.send_message(id_of_user, "=========================")
        telegram_bot.send_message(id_of_user, f'<b>You Win! You have a Blackjack</b>',
                                  parse_mode='html')
        get_player(id_of_user, list_of_players).set_currency_for_player()

    @resize_keyboard_decorator
    def blackjack_for_croupier(self, id_of_user, list_of_players):
        telegram_bot.send_message(id_of_user, "=========================")
        telegram_bot.send_message(id_of_user, f'<b>You Lose! Croupier has a Blackjack</b>',
                                  parse_mode='html')
        get_player(id_of_user, list_of_players).set_currency_for_player()

    def define_result(self, message, player, croupier, deck, list_of_players):
        player_sum = player.counting_sum()
        if player_sum == 21:
            croupier_sum = croupier.counting_sum()
            croupier.croupier_choice(croupier_sum, deck, message)
            if croupier_sum == 21:
                player.currency += player.bet
                self.draw(self, message.chat.id, list_of_players)
            else:
                player.currency += (player.bet * 15) // 10
                self.blackjack(self, message.chat.id, list_of_players)
