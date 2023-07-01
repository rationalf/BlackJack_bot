import random
import json
import telebot
from telebot import types


def add_dictionary_to_json(key):
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


class Card:
    """class that represents the playing card"""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        pass


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


def counting_sum(cards_on_various_hand):
    summ = 0
    for card in cards_on_various_hand:
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


class Deck:
    """class that represents the deck of playing cards
    consists of 52 cards, 4 suits and numbers from 2 up to 14"""

    def __init__(self):
        self.cards = []
        ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
        suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):

        """function that randomizes the order of cards in the deck"""
        random.shuffle(self.cards)
        pass


cards_on_hands = []
index_of_card = 0
deck = Deck()
cards_on_croupier = []
index_of_croupier_card = 0
deck_index = 0

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


@telegram_bot.message_handler(commands=['start'])
def start(message):
    """command for greeting a new user"""
    user_name = message.from_user.username
    telegram_bot.send_message(message.chat.id, f'<b>Hi</b> {user_name}', parse_mode='html')
    website(message)
    print(add_dictionary_to_json(message.from_user.id))


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

    global index_of_card, cards_on_hands, cards_on_croupier, index_of_croupier_card, deck_index
    index_of_card = 0
    cards_on_hands = []
    cards_on_croupier = []
    index_of_croupier_card = 0
    deck.shuffle()
    deck_index = 0


def give_user_card():
    global index_of_card, cards_on_hands, cards_on_croupier, index_of_croupier_card, deck_index
    cards_on_hands.append(deck.cards[deck_index])
    deck_index += 1
    rank = cards_on_hands[index_of_card].rank
    suit = cards_on_hands[index_of_card].suit
    card = view_of_card(rank, suit)
    index_of_card += 1
    return card

def give_croupier_card():
    global index_of_card, cards_on_hands, cards_on_croupier, index_of_croupier_card, deck_index
    cards_on_croupier.append(deck.cards[deck_index])
    deck_index += 1
    croupier_rank = cards_on_croupier[index_of_croupier_card].rank
    croupier_suit = cards_on_croupier[index_of_croupier_card].suit
    croupier_card = view_of_card(croupier_rank, croupier_suit)
    index_of_croupier_card += 1
    return croupier_card

@telegram_bot.message_handler()
def get_user_text(message):
    """command for handling the user's text"""
    global index_of_card, cards_on_hands, cards_on_croupier, index_of_croupier_card, deck_index
    if message.text == "Hit":

        """taking one more card if it is possible"""
        if len(cards_on_hands) == 0:
            card = give_user_card()
            telegram_bot.send_message(message.chat.id, "Your first card is " + card)

            card = give_user_card()
            telegram_bot.send_message(message.chat.id, "Your second card is " + card)
            telegram_bot.send_message(message.chat.id, "=========================")

            croupier_card = give_croupier_card()
            telegram_bot.send_message(message.chat.id, "Croupier first card is " + croupier_card)

            croupier_card = give_croupier_card()
            telegram_bot.send_message(message.chat.id, "Croupier second card is " + croupier_card)

            croupier_sum = counting_sum(cards_on_croupier)
            if croupier_sum == 21:
                telegram_bot.send_message(message.chat.id, "=========================")
                blackjack_for_croupier(message.chat.id)

            sum_of_card = counting_sum(cards_on_hands)
            if sum_of_card == 21:
                telegram_bot.send_message(message.chat.id, "=========================")
                blackjack(message.chat.id)
        else:
            card = give_user_card()
            telegram_bot.send_message(message.chat.id, "Your next card is - " + card)

            croupier_sum = counting_sum(cards_on_croupier)
            if croupier_sum <= 14:

                croupier_card = give_croupier_card()
                telegram_bot.send_message(message.chat.id, "=========================")
                telegram_bot.send_message(message.chat.id, "Croupier next card is " + croupier_card)

            else:
                telegram_bot.send_message(message.chat.id, "=========================")
                telegram_bot.send_message(message.chat.id, "Croupier don't take a card ")
        croupier_sum = counting_sum(cards_on_croupier)
        sum_of_cards = counting_sum(cards_on_hands)

        if croupier_sum > 21:
            telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {sum_of_cards}',
                                      parse_mode='html')
            telegram_bot.send_message(message.chat.id, "=========================")
            telegram_bot.send_message(message.chat.id, f'<b>Croupier final sum is - </b> {croupier_sum}',
                                      parse_mode='html')
            winner(message.chat.id)
        elif sum_of_cards > 21:
            telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {sum_of_cards}',
                                      parse_mode='html')
            telegram_bot.send_message(message.chat.id, "=========================")
            telegram_bot.send_message(message.chat.id, f'<b>Croupier final sum is - </b> {croupier_sum}',
                                      parse_mode='html')
            loser(message.chat.id)
    elif message.text == "Stand":
        croupier_sum = counting_sum(cards_on_croupier)
        if croupier_sum <= 14:

            croupier_card = give_croupier_card()
            telegram_bot.send_message(message.chat.id, "=========================")
            telegram_bot.send_message(message.chat.id, "Croupier next card is " + croupier_card)

        else:
            telegram_bot.send_message(message.chat.id, "=========================")
            telegram_bot.send_message(message.chat.id, "Croupier don't take a card ")
        """refusing other cards"""
        for i in cards_on_croupier:
            print(str(i.rank) + i.suit)
        sum_of_cards = counting_sum(cards_on_hands)
        croupier_sum = counting_sum(cards_on_croupier)
        telegram_bot.send_message(message.chat.id, f'<b>Croupier final sum is - </b> {croupier_sum}',
                                  parse_mode='html')
        telegram_bot.send_message(message.chat.id, "=========================")
        telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {sum_of_cards}',
                                  parse_mode='html')
        if croupier_sum > 21 >= sum_of_cards:
            winner(message.chat.id)
        elif 21 >= sum_of_cards > croupier_sum:
            winner(message.chat.id)
        elif sum_of_cards == croupier_sum:
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
