import telebot
from telebot import types
from Classes.Deck import Deck
from Classes.Player import Player
from functions.get_player import get_player

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


@telegram_bot.message_handler(commands=['play'])
def play_command(message, deck, list_of_players):
    '''Creating a deck for gaming and starting game'''
    del deck

    def delete_player(id_of_user):
        for user in list_of_players:
            if user.id == id_of_user:
                list_of_players.remove(user)

    deck = Deck()
    delete_player(message.from_user.id)
    delete_player(str(message.from_user.id) + message.from_user.username)

    player = Player(message.from_user.id, list_of_players)
    player.currency = player.get_currency_from_json()
    Player(str(message.from_user.id) + message.from_user.username, list_of_players)
    deck.index = 0
    if get_player(message.from_user.id, list_of_players).currency < 50:
        telegram_bot.send_message(message.chat.id, "Your balance is lower than minimum bet")
        message.text = 'Your balance - ' + str(get_player(message.from_user.id, list_of_players).currency)
        return True
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    balance_button = types.InlineKeyboardButton('Your balance - '
                                                + str(get_player(message.from_user.id, list_of_players).currency))
    markup.add(balance_button)
    telegram_bot.send_message(message.chat.id, "Enter your bet:", reply_markup=markup)
    player.betIsEntered = True
    return False
