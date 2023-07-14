import telebot
from telebot import types


telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


@telegram_bot.message_handler(commands=['help'])
def help_command(message):
    """command for showing all commands"""
    telegram_bot.send_message(message.chat.id, 'All available commands:'
                                               '\n /start - for starting the bot'
                                               '\n /help - for watching all the commands'
                                               '\n /play - for starting the game'
                                               '\n /rules - for reading the rules of the game', parse_mode='html')


@telegram_bot.message_handler(commands=['rules'])
def rules_command(message):
    """command that represents the link on wiki page with Blackjack rules """
    link_to_rules = "https://en.wikipedia.org/wiki/Blackjack"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Visit a website with rules of Blackjack", url=link_to_rules))
    telegram_bot.send_message(message.chat.id, 'Blackjack rules', reply_markup=markup)
    help_command(message)