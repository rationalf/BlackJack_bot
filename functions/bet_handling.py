import telebot
from telebot import types
from Commads.play_command import play_command
from functions.get_player import get_player

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


def bet_handling(message, player, deck, list_of_players):
    """Function for bets"""
    player.bet = int(message.text)

    if player.bet < 50:
        telegram_bot.send_message(message.chat.id, "Your bet is NOT accepted!\nMinimum value of bet - 50!")
        return play_command(message, deck, list_of_players)
    elif player.bet > player.currency:
        telegram_bot.send_message(message.chat.id,
                                  f"Your bet is <b>NOT</b> accepted!\nYour bet must be less or equal than your "
                                  f"balance!", parse_mode='html')
        return play_command(message, deck, list_of_players)
    player.currency -= player.bet


def resize_keyboard_start(message, player, list_of_players):
    """Function for buttons start"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start_button = types.KeyboardButton('Start')
    markup.add(start_button)
    telegram_bot.send_message(message.chat.id, "To start playing, press the button",
                              reply_markup=markup)
    get_player(player.id, list_of_players).set_currency_for_player()
    return


def resize_keyboard_hit_stand(message, list_of_players):
    """Function for buttons hit and stand"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    hit_button = types.KeyboardButton('Hit')
    stand_button = types.KeyboardButton('Stand')
    balance_button = types.InlineKeyboardButton('Your balance - '
                                                + str(get_player(message.from_user.id, list_of_players).currency))
    markup.add(hit_button, stand_button, balance_button)
    telegram_bot.send_message(message.chat.id, "Your bet is accepted", reply_markup=markup)
