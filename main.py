import random
import json
import telebot
from telebot import types
from view_of_card import view_of_card
from commands import help_command, rules_command

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


class ResultOfGame:
    def winner(self, id_of_user):
        telegram_bot.send_message(id_of_user, "=========================")
        telegram_bot.send_message(id_of_user, "You Win!",
                                  parse_mode='html')
        resize_keyboard(id_of_user)
        get_player(id_of_user).set_currency_for_player()

    def loser(self, id_of_user):
        telegram_bot.send_message(id_of_user, "=========================")
        telegram_bot.send_message(id_of_user, f'<b>You Lose!</b>',
                                  parse_mode='html')
        resize_keyboard(id_of_user)
        get_player(id_of_user).set_currency_for_player()

    def draw(self, id_of_user):
        telegram_bot.send_message(id_of_user, "=========================")
        telegram_bot.send_message(id_of_user, f'<b>It is a draw!</b>',
                                  parse_mode='html')
        resize_keyboard(id_of_user)
        get_player(id_of_user).set_currency_for_player()

    def blackjack(self, id_of_user):
        telegram_bot.send_message(id_of_user, "=========================")
        telegram_bot.send_message(id_of_user, f'<b>You Win! You have a Blackjack</b>',
                                  parse_mode='html')
        resize_keyboard(id_of_user)
        get_player(id_of_user).set_currency_for_player()

    def blackjack_for_croupier(self, id_of_user):
        telegram_bot.send_message(id_of_user, "=========================")
        telegram_bot.send_message(id_of_user, f'<b>You Lose! Croupier has a Blackjack</b>',
                                  parse_mode='html')
        resize_keyboard(id_of_user)
        get_player(id_of_user).set_currency_for_player()


def resize_keyboard(id_of_user):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    stop_button = types.KeyboardButton('Stop playing')
    restart_button = types.KeyboardButton('Start another game')
    balance_button = types.InlineKeyboardButton('Your balance - ' + str(get_player(id_of_user).currency))
    markup.add(restart_button, stop_button, balance_button)
    telegram_bot.send_message(id_of_user, "To restart game, press the button",
                              reply_markup=markup)


class Player:

    def __init__(self, user_id):
        global list_of_players
        self.id = user_id
        self.currency = self.get_currency_from_json()
        self.cards_on_hands = []
        self.index_of_card = 0
        list_of_players.append(self)

    def counting_sum(self):
        summ = 0
        for card in self.cards_on_hands:
            if int(card.rank) < 10:
                summ += int(card.rank)
            else:
                if int(card.rank) != 14:
                    summ += 10
                else:
                    if summ + 11 > 21:
                        summ += 1
                    else:
                        summ += 11
        return summ

    def croupier_choice(self, croupier_sum, message):
        global deck
        if self.id == str(message.from_user.id) + message.from_user.username:
            if croupier_sum <= 16:
                croupier_card = deck.give_user_card(self)
                telegram_bot.send_message(message.chat.id, "=========================")
                telegram_bot.send_message(message.chat.id, "Croupier next card is ")
                telegram_bot.send_sticker(message.chat.id, str(croupier_card))
            else:
                telegram_bot.send_message(message.chat.id, "=========================")
                telegram_bot.send_message(message.chat.id, "Croupier don't take a card ")

    def get_currency_from_json(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
        file.close()
        if data.keys().__contains__(str(self.id)):
            return data.get(str(self.id))
        return 0

    def set_currency_for_player(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
        file.close()
        if data.keys().__contains__(str(self.id)):
            data[str(self.id)] = self.currency
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        file.close()


class Card:
    """class that represents the playing card"""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        pass


class Deck:
    """class that represents the deck of playing cards
    consists of 52 cards, 4 suits and numbers from 2 up to 14"""

    def __init__(self):
        self.cards = []
        self.index = 0
        ranks = [i for i in range(2, 15)] * 4
        suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):

        """function that randomizes the order of cards in the deck"""
        random.shuffle(self.cards)
        pass

    def give_user_card(self, user):
        user.cards_on_hands.append(self.cards[self.index])
        self.index += 1
        rank = user.cards_on_hands[user.index_of_card].rank
        suit = user.cards_on_hands[user.index_of_card].suit
        card = view_of_card(rank, suit)
        user.index_of_card += 1
        return card


deck = Deck()
list_of_players = []


def get_player(id_of_user):
    for player in list_of_players:
        if player.id == id_of_user:
            return player


def delete_player(ID):
    for player in list_of_players:
        if player.id == ID:
            list_of_players.remove(player)


@telegram_bot.message_handler(commands=['start'])
def start(message):
    """command for greeting a new user"""

    def add_dictionary_to_json():
        nonlocal message
        key = message.from_user.id
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        file.close()
        if data.keys().__contains__(str(key)):
            return data.get(str(key))
        data[key] = 5000
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        file.close()
        return 5000

    user_name = message.from_user.username
    telegram_bot.send_message(message.chat.id, f'<b>Hi</b> {user_name}', parse_mode='html')
    help_command(message)
    add_dictionary_to_json()


@telegram_bot.message_handler(commands=['play'])
def play_command(message):
    global deck, list_of_players
    del deck
    deck = Deck()
    delete_player(message.from_user.id)
    delete_player(str(message.from_user.id) + message.from_user.username)

    player = Player(message.from_user.id)
    player.currency = player.get_currency_from_json()
    Player(str(message.from_user.id) + message.from_user.username)
    deck.shuffle()
    deck.index = 0
    if get_player(message.from_user.id).currency < 50:
        telegram_bot.send_message(message.chat.id, "Your balance is lower than minimum bet")
        message.text = 'Your balance - ' + str(get_player(message.from_user.id).currency)
        get_user_text(message)
        return
    telegram_bot.send_message(message.chat.id, "Enter your bet:")


@telegram_bot.message_handler()
def get_user_text(message):
    """command for handling the user's text"""
    if message.text == '/help':
        help_command(message)
        return
    elif message.text == '/rules':
        rules_command(message)
        return
    global deck
    player = get_player(message.from_user.id)
    croupier = get_player(str(message.from_user.id) + message.from_user.username)
    result_of_game = ResultOfGame()
    if message.text == "Hit":
        player_card = deck.give_user_card(player)
        telegram_bot.send_message(message.chat.id, "Your next card is:")
        telegram_bot.send_sticker(message.chat.id, str(player_card))
        player_sum = player.counting_sum()

        if player_sum > 21:
            telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {player_sum}',
                                      parse_mode='html')
            result_of_game.loser(message.chat.id)

    elif message.text == "Stand":
        player_sum = player.counting_sum()
        croupier_sum = croupier.counting_sum()
        while croupier_sum <= 16:
            croupier.croupier_choice(croupier_sum, message)
            croupier_sum = croupier.counting_sum()
        if croupier_sum == 21 and len(croupier.cards_on_hands) == 2:
            telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {player_sum}',
                                      parse_mode='html')
            result_of_game.blackjack_for_croupier(message.chat.id)

        telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {player_sum}',
                                  parse_mode='html')
        telegram_bot.send_message(message.chat.id, f'<b>Croupier final sum is - </b> {croupier_sum}',
                                  parse_mode='html')

        if croupier_sum > 21 >= player_sum or 21 >= player_sum > croupier_sum:
            player.currency += player.bet * 2
            result_of_game.winner(message.chat.id)
        elif player_sum == croupier_sum:
            player.currency += player.bet
            result_of_game.draw(message.chat.id)
        else:
            result_of_game.loser(message.chat.id)

    elif message.text == 'Start another game' or message.text == 'Start':
        """restarting the game"""
        play_command(message)
    elif message.text == 'Stop playing':

        """stop playing"""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        start_button = types.KeyboardButton('Start')
        markup.add(start_button)
        telegram_bot.send_message(message.chat.id, "To start playing, press the button",
                                  reply_markup=markup)
        get_player(player.id).set_currency_for_player()
    elif message.text == 'Your balance - ' + str(get_player(message.from_user.id).currency):
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
            return play_command(message)
        elif player.bet > player.currency:
            telegram_bot.send_message(message.chat.id,
                                      f"Your bet is <b>NOT</b> accepted!\nYour bet must be less or equal than your "
                                      f"balance!", parse_mode='html')
            return play_command(message)
        player.currency -= player.bet

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        hit_button = types.KeyboardButton('Hit')
        stand_button = types.KeyboardButton('Stand')
        balance_button = types.InlineKeyboardButton('Your balance - ' + str(get_player(message.from_user.id).currency))
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
            croupier.croupier_choice(croupier_sum, message)
            if croupier_sum == 21:
                player.currency += player.bet
                result_of_game.draw(message.chat.id)
            else:
                player.currency += (player.bet * 15) // 10
                result_of_game.blackjack(message.chat.id)

    else:
        telegram_bot.send_message(message.chat.id, "Bet must be a natural number")


telegram_bot.polling(none_stop=True)
