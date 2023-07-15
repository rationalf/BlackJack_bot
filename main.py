import telebot
from Messages.message_handler import get_user_text
from Classes.Deck import Deck

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')

deck = Deck()
list_of_players = []


@telegram_bot.message_handler()
def game(message):
    """This function for starting game"""
    get_user_text(message, deck, list_of_players)


telegram_bot.polling(none_stop=True)
