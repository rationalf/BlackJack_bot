import json
import telebot

from Commads.help_command import help_command

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


@telegram_bot.message_handler(commands=['start'])
def start_command(message):
    """command for greeting a new user"""

    def add_user_to_json():
        nonlocal message
        key = message.from_user.id
        try:
            with open('databaseForCurrencies.json', 'r') as file:
                database = json.load(file)
        except FileNotFoundError:
            database = {}
        file.close()
        if database.keys().__contains__(str(key)):
            return database.get(str(key))
        database[key] = 5000
        with open('databaseForCurrencies.json', 'w') as file:
            print(key)
            json.dump(database, file, indent=4)
        file.close()
        return 5000

    user_name = message.from_user.username
    telegram_bot.send_message(message.chat.id, f'<b>Hi</b> {user_name}', parse_mode='html')
    help_command(message)
    add_user_to_json()
