import telebot
import json

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


class Player:

    def __init__(self, user_id, list_of_players):
        self.id = user_id
        self.currency = self.get_currency_from_json()
        self.cards_on_hands = []
        self.index_of_card = 0
        self.betIsEntered = False
        list_of_players.append(self)

    def counting_sum(self):
        """Function for counting sum of card"""
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

    def croupier_choice(self, croupier_sum, deck, message):
        """Function for giving croupier cards"""
        if self.id == str(message.from_user.id) + message.from_user.username:
            if croupier_sum <= 16:
                croupier_card = deck.give_user_card(self)
                telegram_bot.send_message(message.chat.id, "Croupier next card is ")
                telegram_bot.send_sticker(message.chat.id, str(croupier_card))
            else:
                telegram_bot.send_message(message.chat.id, "Croupier don't take a card ")

    def get_currency_from_json(self):
        """Function for taking currency from database"""
        with open('databaseForCurrencies.json', 'r') as file:
            database = json.load(file)
        file.close()
        if database.keys().__contains__(str(self.id)):
            return database.get(str(self.id))
        return 0

    def set_currency_for_player(self):
        """Function of setting new currency"""
        with open('databaseForCurrencies.json', 'r') as file:
            database = json.load(file)
        file.close()
        if database.keys().__contains__(str(self.id)):
            database[str(self.id)] = self.currency
        with open('databaseForCurrencies.json', 'w') as file:
            json.dump(database, file, indent=4)
        file.close()
