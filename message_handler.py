import telebot
import json
from Deck import Deck
from Player import Player
from telebot import types
from get_player import get_player
from ResultOfGame import ResultOfGame

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


@telegram_bot.message_handler(commands=['start'])
def start_command(message):
    """command for greeting a new user"""

    def add_dictionary_to_json():
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
            json.dump(database, file, indent=4)
        file.close()
        return 5000

    user_name = message.from_user.username
    telegram_bot.send_message(message.chat.id, f'<b>Hi</b> {user_name}', parse_mode='html')
    help_command(message)
    add_dictionary_to_json()


@telegram_bot.message_handler(commands=['play'])
def play_command(message, deck, list_of_players):
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
        get_user_text(message)
        return
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    balance_button = types.InlineKeyboardButton('Your balance - '
                                                + str(get_player(message.from_user.id, list_of_players).currency))
    markup.add(balance_button)
    telegram_bot.send_message(message.chat.id, "Enter your bet:", reply_markup=markup)


@telegram_bot.message_handler()
def get_user_text(message, deck, list_of_players):
    """command for handling the user's text"""
    if message.text == '/help':
        help_command(message)
        return
    elif message.text == '/rules':
        rules_command(message)
        return
    elif message.text == '/start':
        start_command(message)
        return
    elif message.text == '/play':
        play_command(message, deck, list_of_players)
        return

    player = get_player(message.from_user.id, list_of_players)
    croupier = get_player(str(message.from_user.id) + message.from_user.username, list_of_players)
    result_of_game = ResultOfGame()
    if message.text == "Hit":
        player_card = deck.give_user_card(player)
        telegram_bot.send_message(message.chat.id, "Your next card is:")
        telegram_bot.send_sticker(message.chat.id, str(player_card))
        player_sum = player.counting_sum()

        if player_sum > 21:
            telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {player_sum}',
                                      parse_mode='html')
            result_of_game.loser(message.chat.id, list_of_players)

    elif message.text == "Stand":
        player_sum = player.counting_sum()
        croupier_sum = croupier.counting_sum()
        while croupier_sum <= 16:
            croupier.croupier_choice(croupier_sum, deck, message)
            croupier_sum = croupier.counting_sum()
        if croupier_sum == 21 and len(croupier.cards_on_hands) == 2:
            telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {player_sum}',
                                      parse_mode='html')
            result_of_game.blackjack_for_croupier(message.chat.id, list_of_players)

        telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {player_sum}',
                                  parse_mode='html')
        telegram_bot.send_message(message.chat.id, f'<b>Croupier final sum is - </b> {croupier_sum}',
                                  parse_mode='html')

        if croupier_sum > 21 >= player_sum or 21 >= player_sum > croupier_sum:
            player.currency += player.bet * 2
            result_of_game.winner(message.chat.id, list_of_players)
        elif player_sum == croupier_sum:
            player.currency += player.bet
            result_of_game.draw(message.chat.id, list_of_players)
        else:
            result_of_game.loser(message.chat.id, list_of_players)

    elif message.text == 'Start another game' or message.text == 'Start':
        """restarting the game"""
        play_command(message, deck, list_of_players)
    elif message.text == 'Stop playing':

        """stop playing"""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        start_button = types.KeyboardButton('Start')
        markup.add(start_button)
        telegram_bot.send_message(message.chat.id, "To start playing, press the button",
                                  reply_markup=markup)
        get_player(player.id, list_of_players).set_currency_for_player()
    elif message.text == 'Your balance - ' + str(get_player(message.from_user.id, list_of_players).currency):
        telegram_bot.send_message(message.chat.id,
                                  "5000 chips - 100 rubles\n"
                                  "10000 chips - 175 rubles\n"
                                  "50000 chips - 750 rubles\n"
                                  "\n"
                                  "To send money contact us on telegram:\n"
                                  "@GaaanG_Hooold_oooN\n"
                                  "@Sergey_Dzyuba\n"
                                  "\nTo get 1 000 000 chips for free, give us A's for the PP course :)")
    elif message.text.isdigit():
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

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        hit_button = types.KeyboardButton('Hit')
        stand_button = types.KeyboardButton('Stand')
        balance_button = types.InlineKeyboardButton('Your balance - '
                                                    + str(get_player(message.from_user.id, list_of_players).currency))
        markup.add(hit_button, stand_button, balance_button)
        telegram_bot.send_message(message.chat.id, "Your bet is accepted", reply_markup=markup)
        player_card = deck.give_user_card(player)
        telegram_bot.send_message(message.chat.id, "Your first cards are ")
        telegram_bot.send_sticker(message.chat.id, str(player_card))
        player_card = deck.give_user_card(player)
        telegram_bot.send_sticker(message.chat.id, str(player_card))
        croupier_card = deck.give_user_card(croupier)
        telegram_bot.send_message(message.chat.id, "Croupier first card is ")
        telegram_bot.send_sticker(message.chat.id, str(croupier_card))

        player_sum = player.counting_sum()
        if player_sum == 21:
            croupier_sum = croupier.counting_sum()
            croupier.croupier_choice(croupier_sum, deck, message)
            if croupier_sum == 21:
                player.currency += player.bet
                result_of_game.draw(message.chat.id, list_of_players)
            else:
                player.currency += (player.bet * 15) // 10
                result_of_game.blackjack(message.chat.id, list_of_players)

    else:
        telegram_bot.send_message(message.chat.id, "Bet must be a natural number")
