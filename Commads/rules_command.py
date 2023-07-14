import telebot
from telebot import types
from Commads.help_command import help_command

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


@telegram_bot.message_handler(commands=['rules'])
def rules_command(message):
    """command that represents the link on wiki page with Blackjack rules """
    link_to_rules = "https://en.wikipedia.org/wiki/Blackjack"
    markup = types.InlineKeyboardMarkup()
    telegram_bot.send_message(message.chat.id,
                              "1. The main objective of the game is to collect the nearest number <strong>less than or "
                              "equal to 21</strong> and more than croupier.\n"
                              "2. You have to bet at the start of the game.\n"
                              "3. Then you will get two cards and will be able to see one of croupier's cards.\n"
                              "4. After that choose either 'Hit' or 'Stand'\n"
                              "4.a 'Hit' gives one more card for you.\n"
                              "4.b 'Stand' means you don't take card from the deck for current game\n\n"
                              "In one game four decks are involved\n"
                              "For detailed and original rules use the link", parse_mode='html')
    markup.add(types.InlineKeyboardButton("Visit a website with rules of Blackjack", url=link_to_rules))
    telegram_bot.send_message(message.chat.id, 'Blackjack rules', reply_markup=markup)
    help_command(message)
