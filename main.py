import random
import json
import telebot
from telebot import types

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


def winner(id_of_user):
    telegram_bot.send_message(id_of_user, "You Win!",
                              parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    stop_button = types.KeyboardButton('Stop playing')
    restart_button = types.KeyboardButton('Start another game')
    markup.add(stop_button, restart_button)
    telegram_bot.send_message(id_of_user, "To restart game, press the button",
                              reply_markup=markup)


def loser(id_of_user):
    telegram_bot.send_message(id_of_user, f'<b>You Lose!</b>',
                              parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    stop_button = types.KeyboardButton('Stop playing')
    restart_button = types.KeyboardButton('Start another game')
    markup.add(stop_button, restart_button)
    telegram_bot.send_message(id_of_user, "To restart game, press the button",
                              reply_markup=markup)


def draw(id_of_user):
    telegram_bot.send_message(id_of_user, f'<b>It is a draw!</b>',
                              parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    stop_button = types.KeyboardButton('Stop playing')
    restart_button = types.KeyboardButton('Start another game')
    markup.add(stop_button, restart_button)
    telegram_bot.send_message(id_of_user, "To restart game, press the button",
                              reply_markup=markup)


def blackjack(id_of_user):
    telegram_bot.send_message(id_of_user, f'<b>You Win! You have a Blackjack</b>',
                              parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    stop_button = types.KeyboardButton('Stop playing')
    restart_button = types.KeyboardButton('Start another game')
    markup.add(stop_button, restart_button)
    telegram_bot.send_message(id_of_user, "To restart game, press the button",
                              reply_markup=markup)


def blackjack_for_croupier(id_of_user):
    telegram_bot.send_message(id_of_user, f'<b>You Lose! Croupier has a Blackjack</b>',
                              parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    stop_button = types.KeyboardButton('Stop playing')
    restart_button = types.KeyboardButton('Start another game')
    markup.add(stop_button, restart_button)
    telegram_bot.send_message(id_of_user, "To restart game, press the button",
                              reply_markup=markup)


def view_of_card(rank, suit):
    if rank == 2:
        rank = "2️⃣"
    elif rank == 3:
        rank = "3️⃣"
    elif rank == 4:
        rank = "4️⃣"
    elif rank == 5:
        rank = "5️⃣"
    elif rank == 6:
        rank = "6️⃣"
    elif rank == 7:
        rank = "7️⃣"
    elif rank == 8:
        rank = "8️⃣"
    elif rank == 9:
        rank = "9️⃣"
    elif rank == 10:
        rank = "🔟"
    elif rank == 11:
        rank = "🅹"
    elif rank == 12:
        rank = "🆀"
    elif rank == 13:
        rank = "🅺"
    else:
        rank = "🅰"
    if suit == 'Clubs':
        suit_with_emoji = "\U00002663"
    elif suit == 'Hearts':
        suit_with_emoji = "\U00002665"
    elif suit == 'Spades':
        suit_with_emoji = "\U00002660"
    else:
        suit_with_emoji = "\U00002666"
    return rank + " " + suit_with_emoji


class Player:

    def __init__(self, id):
        global deck
        self.id = id
        self.cards_on_hands = []
        self.index_of_card = 0
        deck.list_of_players.append(self)

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
        if self.id == 0:
            if croupier_sum <= 16:
                croupier_card = deck.give_user_card(self)
                telegram_bot.send_message(message.chat.id, "=========================")
                telegram_bot.send_message(message.chat.id, "Croupier next card is " + croupier_card)

            else:
                telegram_bot.send_message(message.chat.id, "=========================")
                telegram_bot.send_message(message.chat.id, "Croupier don't take a card ")


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
        self.list_of_players = []
        ranks = {i for i in range(2, 15)}
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

    def get_player(self, ID):
        for player in self.list_of_players:
            if player.id == ID:
                return player
        return None


deck = Deck()


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
        if data.keys().__contains__(str(key)):
            print(f"Skipping duplicate entry for key: {key}")
            return data.get(str(key))
        print(data)
        print(key)
        data[key] = 5000
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        return 5000

    user_name = message.from_user.username
    telegram_bot.send_message(message.chat.id, f'<b>Hi</b> {user_name}', parse_mode='html')
    website(message)
    print(add_dictionary_to_json())


@telegram_bot.message_handler(commands=['help'])
def website(message):
    """command for showing all commands"""
    telegram_bot.send_message(message.chat.id, 'All available commands:'
                                               '\n /start - for starting the bot'
                                               '\n /help - for watching all the commands'
                                               '\n /play - for starting the game'
                                               '\n /rules - for reading the rules of the game',
                              parse_mode='html')


@telegram_bot.message_handler(commands=['rules'])
def rules(message):
    """command that represents the link on wiki page with Blackjack rules """
    link_to_rules = "https://en.wikipedia.org/wiki/Blackjack"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Visit a website with rules of Blackjack", url=link_to_rules))
    telegram_bot.send_message(message.chat.id, 'Blackjack rules', reply_markup=markup)
    website(message)


@telegram_bot.message_handler(commands=['play'])
def play(message):
    """command for starting playing the game"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    hit_button = types.KeyboardButton('Hit')
    stand_button = types.KeyboardButton('Stand')
    markup.add(hit_button, stand_button)
    telegram_bot.send_message(message.chat.id, "Have a look at available buttons:", reply_markup=markup)

    global deck
    del deck
    deck = Deck()
    Player(message.from_user.id)
    Player(0)
    deck.shuffle()
    deck.index = 0


@telegram_bot.message_handler()
def get_user_text(message):
    """command for handling the user's text"""
    global deck
    player = deck.get_player(message.from_user.id)
    croupier = deck.get_player(0)

    if message.text == "Hit":

        """taking one more card if it is possible"""
        if len(player.cards_on_hands) == 0:
            player_card = deck.give_user_card(player)
            telegram_bot.send_message(message.chat.id, "Your first card is " + player_card)
            player_card = deck.give_user_card(player)
            telegram_bot.send_message(message.chat.id, "Your second card is " + player_card)

            telegram_bot.send_message(message.chat.id, "=========================")

            croupier_card = deck.give_user_card(croupier)
            telegram_bot.send_message(message.chat.id, "Croupier first card is " + croupier_card)
            croupier_card = deck.give_user_card(croupier)
            telegram_bot.send_message(message.chat.id, "Croupier second card is " + croupier_card)

            croupier_sum = croupier.counting_sum()
            if croupier_sum == 21:
                telegram_bot.send_message(message.chat.id, "=========================")
                blackjack_for_croupier(message.chat.id)

            player_sum = player.counting_sum()
            if player_sum == 21:
                telegram_bot.send_message(message.chat.id, "=========================")
                blackjack(message.chat.id)
        else:
            player_card = deck.give_user_card(player)
            telegram_bot.send_message(message.chat.id, "Your next card is - " + player_card)

            croupier_sum = croupier.counting_sum()
            croupier.croupier_choice(croupier_sum, message)

        croupier_sum = croupier.counting_sum()
        player_sum = player.counting_sum()

        if player_sum > 21:
            telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {player_sum}',
                                      parse_mode='html')
            telegram_bot.send_message(message.chat.id, "=========================")
            telegram_bot.send_message(message.chat.id, f'<b>Croupier final sum is - </b> {croupier_sum}',
                                      parse_mode='html')
            loser(message.chat.id)
        elif croupier_sum > 21:
            telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {player_sum}',
                                      parse_mode='html')
            telegram_bot.send_message(message.chat.id, "=========================")
            telegram_bot.send_message(message.chat.id, f'<b>Croupier final sum is - </b> {croupier_sum}',
                                      parse_mode='html')
            winner(message.chat.id)

    elif message.text == "Stand":
        croupier_sum = croupier.counting_sum()
        croupier.croupier_choice(croupier_sum, message)

        player_sum = player.counting_sum()
        croupier_sum = croupier.counting_sum()

        telegram_bot.send_message(message.chat.id, f'<b>Croupier final sum is - </b> {croupier_sum}',
                                  parse_mode='html')
        telegram_bot.send_message(message.chat.id, "=========================")
        telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {player_sum}',
                                  parse_mode='html')

        if croupier_sum > 21 >= player_sum:
            winner(message.chat.id)
        elif 21 >= player_sum > croupier_sum:
            winner(message.chat.id)
        elif player_sum == croupier_sum:
            draw(message.chat.id)
        else:
            loser(message.chat.id)
    elif message.text == 'Start another game' or message.text == 'Start':

        """restarting the game"""
        play(message)
    elif message.text == 'Stop playing':

        """stop playing"""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        start_button = types.KeyboardButton('Start')
        markup.add(start_button)
        telegram_bot.send_message(message.chat.id, "To start playing, press the button",
                                  reply_markup=markup)


telegram_bot.polling(none_stop=True)
