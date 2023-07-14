from Classes.Card import Card
import random
from functions.view_of_card import view_of_card
import telebot

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


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
        self.shuffle()

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

    def initial_distribution_of_cards(self, message, player, croupier, deck):
        player_card = deck.give_user_card(player)
        telegram_bot.send_message(message.chat.id, "Your first cards are ")
        telegram_bot.send_sticker(message.chat.id, str(player_card))
        player_card = deck.give_user_card(player)
        telegram_bot.send_sticker(message.chat.id, str(player_card))
        croupier_card = deck.give_user_card(croupier)
        telegram_bot.send_message(message.chat.id, "Croupier first card is ")
        telegram_bot.send_sticker(message.chat.id, str(croupier_card))
