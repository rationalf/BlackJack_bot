import telebot

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


@telegram_bot.message_handler(commands=['help'])
def help_command(message):
    """command for showing all commands"""
    telegram_bot.send_message(message.chat.id, 'All available commands:'
                                               '\n /start - for starting the bot'
                                               '\n /help - for watching all the commands'
                                               '\n /play - for starting the game'
                                               '\n /rules - for reading the rules of the game', parse_mode='html')
