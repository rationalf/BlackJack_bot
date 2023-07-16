import telebot
from telebot import types
from functions.get_player import get_player

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


def bet_handling(message, player, list_of_players):
    """Function for approving the bet"""
    player.bet = int(message.text)

    if get_player(message.from_user.id, list_of_players).currency < 50:
        telegram_bot.send_message(message.chat.id, "Your balance is lower than minimum bet")
        resize_keyboard_low_balance(message, list_of_players)
        return True
    elif player.bet > player.currency:
        telegram_bot.send_message(message.chat.id,
                                  f"Your bet is <b>NOT</b> accepted!\nYour bet must be less than or equal to your "
                                  f"balance!", parse_mode='html')
        telegram_bot.send_message(message.chat.id, "Enter your bet:")
        player.betIsEntered = True
        return True
    elif player.bet < 50:
        telegram_bot.send_message(message.chat.id, "Your bet is NOT accepted!\nMinimum value of bet - 50!")
        telegram_bot.send_message(message.chat.id, "Enter your bet:")
        player.betIsEntered = True
        return True
    player.currency -= player.bet
    return False


def resize_keyboard_start(message, player, list_of_players):
    """Function for buttons start"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start_button = types.KeyboardButton('Start')
    balance_button = types.InlineKeyboardButton('Your balance - '
                                                + str(get_player(message.from_user.id, list_of_players).currency))
    markup.add(start_button, balance_button)
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


def resize_keyboard_low_balance(message, list_of_players):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    balance_button = types.InlineKeyboardButton('Your balance - '
                                                + str(get_player(message.from_user.id, list_of_players).currency))
    markup.add(balance_button)
    telegram_bot.send_message(message.chat.id, "Press the button: ", reply_markup=markup)
