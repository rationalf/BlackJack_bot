import random
import json
import telebot
from telebot import types

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


def view_of_card(rank, suit):
    if suit == "Clubs":
        if rank == 2:
            return "CAACAgUAAxkBAAEJmx5kpebc_XlwoOaxJR7AXpOnMN9LjgAC7gADzD_AVUNl620pf85VLwQ"
        elif rank == 3:
            return "CAACAgUAAxkBAAEJmyBkpecF9ZOmrnEkjJSTYpndbhjp-QACxAADjXXJVSgF1c4SfQRVLwQ"
        elif rank == 4:
            return "CAACAgUAAxkBAAEJmyJkpecnUi0fkXBD2IPd0ajk9ProjQAC1QADdn3BVdsjMJCRrwM-LwQ"
        elif rank == 5:
            return "CAACAgUAAxkBAAEJmyRkpedGJAOB-Eb7mW_2ewlAEER6_gACQQEAAqyuwFUKLvZfnYor0C8E"
        elif rank == 6:
            return "CAACAgUAAxkBAAEJmyZkpedrVZtaKIWayjNNgY8OZYDL1wACLAEAAvSuwVXTZanNGx7wAi8E"
        elif rank == 7:
            return "CAACAgUAAxkBAAEJmyhkpeeOYeM-MW2LV73sKC92gUX2HAAC6QADmpzAVfqejKTvA09xLwQ"
        elif rank == 8:
            return "CAACAgUAAxkBAAEJmypkpeepvj0QZndAlV_mdXS-oeY7rwACZQEAAmsnwFXzDbUvNrlSIC8E"
        elif rank == 9:
            return "CAACAgUAAxkBAAEJmyxkpefM61NNGnMneYUjIgUYSHemHQACHwEAAoPTwVX0XbSdYZTway8E"
        elif rank == 10:
            return "CAACAgUAAxkBAAEJmy5kpefwbrb2TsRWyNEIJjutMODUEgACWAEAApCMwFVqmiojuRUZnS8E"
        elif rank == 11:
            return "CAACAgUAAxkBAAEJmzNkpegaKtyqghX1MSA3PoDjokOT7QACSgEAArVSwVWnJirONvGsjC8E"
        elif rank == 12:
            return "CAACAgUAAxkBAAEJmzVkpeg_F5oR74pLOEGeXqWpbPkKsQACYwEAAtZUwVVB9Jrr699DBi8E"
        elif rank == 13:
            return "CAACAgUAAxkBAAEJmzlkpehd3B_CsFR_HIsOBN7yIa4j6gACagEAArV1wFUsUwIdrbHrzi8E"
        else:
            return "CAACAgUAAxkBAAEJmztkpeiFpPsecJVyzK2mYSo9KoweagACVgEAAk7KwFUdsPO8bDy3zS8E"
    elif suit == "Hearts":
        if rank == 2:
            return "CAACAgUAAxkBAAEJm0JkpejBZ7Ps5jtZ_llkr3xUkyMcxAACwAEAAri0wFUoQPrcy55z9S8E"
        elif rank == 3:
            return "CAACAgUAAxkBAAEJm0RkpejjohHf8SAdYPZRw3YSNsG2WQACkgEAAi3FwVUyj7OilKkEQi8E"
        elif rank == 4:
            return "CAACAgUAAxkBAAEJm0hkpelZdPWuygoUMEy383WahLC8IAACnQEAAtIewFXlnnP4enKOES8E"
        elif rank == 5:
            return "CAACAgUAAxkBAAEJm0pkpelsKmtgxIAPzslWNHpurml6rQAC9wADiiHBVSWGu92DeH5pLwQ"
        elif rank == 6:
            return "CAACAgUAAxkBAAEJm0xkpel-GfQx7eK0qTW0SuTYDfW38AACuQEAAi7fwVUndFyOv1LeuS8E"
        elif rank == 7:
            return "CAACAgUAAxkBAAEJm05kpemOevuEQF0HotvlyRSCdAgYvAACZAEAAtV9wVVc2N-IuRlx0C8E"
        elif rank == 8:
            return "CAACAgUAAxkBAAEJm1BkpemZd1mAY0eOeCsCBR4b044s-QACWAEAAk-6wVUC0fBkmnNZvC8E"
        elif rank == 9:
            return "CAACAgUAAxkBAAEJm1JkpemkAnR8l-8s3OmCHL_TvgObjQACpAEAAoDywVXcV-kFLl4Goy8E"
        elif rank == 10:
            return "CAACAgUAAxkBAAEJm1RkpemyyecueMlXEPw5TDtCODL_DwACEQEAAkFbwFVuiN9FfpNZWS8E"
        elif rank == 11:
            return "CAACAgUAAxkBAAEJm1hkpenCAa-7Ny7MgmEbEhfMGy56GQACTwEAAuZ6wVVeHVQy8OtDZC8E"
        elif rank == 12:
            return "CAACAgUAAxkBAAEJm1Zkpem-Tsfs-zpYiuh3UXCKY4YUfwACVwEAAhgewFWcKPy_MO0FAi8E"
        elif rank == 13:
            return "CAACAgUAAxkBAAEJm1pkpenfmKP1bc0YZsq0I4FtyIrIlgACGQEAAhRTwVWjUBF47pA6ES8E"
        else:
            return "CAACAgUAAxkBAAEJm1xkpenriYn8gyGYgWl-lMvI2F5S0QACigEAAvSIwFVK_o4a4DzQaC8E"
    elif suit == "Spades":
        if rank == 2:
            return "CAACAgUAAxkBAAEJm15kpeuu42bO_JqrYPLjadF08QABtgUAAnYBAALPscBVqkQzr6Yem3ovBA"
        elif rank == 3:
            return "CAACAgUAAxkBAAEJm2Bkpeu5g-VGsCgYDhLjjyd6Dux-HwACiAEAAlr1wFXDzixQPWB0ay8E"
        elif rank == 4:
            return "CAACAgUAAxkBAAEJm2JkpevDdPKZxKxqgVkNJzmRQIjybAAC9QADkD_AVTCXjNsUgWFcLwQ"
        elif rank == 5:
            return "CAACAgUAAxkBAAEJm2RkpevOvtxcm6mTkVpRySZZRTsFhwACtgEAAnl5wVUt6BMU1V4rQS8E"
        elif rank == 6:
            return "CAACAgUAAxkBAAEJm2ZkpevYV40CGjF0yRyAx-CJoU2rTgACwgEAAhMZyFUVAQk2w9IUoy8E"
        elif rank == 7:
            return "CAACAgUAAxkBAAEJm2hkpevkc9gbeZecNow13mgMZm_XRgACXwEAAlcqwVWYKA6AaDeLNC8E"
        elif rank == 8:
            return "CAACAgUAAxkBAAEJm2pkpevuZCRgs3IuRWmGNCt2QQfaSQAC5gEAApGAwFVYXzYRg5l2hS8E"
        elif rank == 9:
            return "CAACAgUAAxkBAAEJm2xkpev7r506r0Ux3uKSe44kS9FaSAACTAEAAlTbwVUOieck2aRPdC8E"
        elif rank == 10:
            return "CAACAgUAAxkBAAEJm25kpewGDon8FBUcRD96bqP62NQvywACfgEAAjEccVarx0aBCU7B3C8E"
        elif rank == 11:
            return "CAACAgUAAxkBAAEJm3BkpewQJOW4JIu_ZaqpV5nIdG1cMgACgQEAAg1zwFVqLPJXSoY2rC8E"
        elif rank == 12:
            return "CAACAgUAAxkBAAEJm3JkpewZ5-8sI6HkgA9yHYwvLXN01QACqQIAAomTwFVYoAJh92UFLi8E"
        elif rank == 13:
            return "CAACAgUAAxkBAAEJm3RkpewjwYqjj3CkcuAXu84UGuoDEAACpQEAAmtpwFXgo7SNLAsgqC8E"
        else:
            return "CAACAgUAAxkBAAEJm3ZkpewsuZ1xIbwvTOUFK9xxZKfFlwACewEAAoCZwFXg-Nr-7hZaoC8E"
    else:
        if rank == 2:
            return "CAACAgUAAxkBAAEJm3hkpew51Ld1sEqrbHrQYW2NH9wb9AACBgEAAmovyFWY6dj4c94fYi8E"
        elif rank == 3:
            return "CAACAgUAAxkBAAEJm3pkpexezDIYng-nOKmLxscC_Ha8cQAClQEAAuvlwVUAAfo2HFjA-HkvBA"
        elif rank == 4:
            return "CAACAgUAAxkBAAEJm3xkpexsg2H2fR8VUQZbVvEbdCLk2AACwQEAAqDNwFWiDdTqzKK29i8E"
        elif rank == 5:
            return "CAACAgUAAxkBAAEJm35kpex5YialkcnlbKEcY_WAPrLbTgACmQEAApEgwVUDWtfULkqa7i8E"
        elif rank == 6:
            return "CAACAgUAAxkBAAEJm4BkpeyFmiiiQk7cG63KIhJKbEfvdwACFwEAAvt_wVWgx6nKpXzQYi8E"
        elif rank == 7:
            return "CAACAgUAAxkBAAEJm4JkpeyOSUJSR8BTqwmkJgOf4WbX0AACjQEAArJWwFW0ccMe7TSgKi8E"
        elif rank == 8:
            return "CAACAgUAAxkBAAEJm4RkpeyZELqffzkbjp9eGLDD28QiVAACXQEAAmtEwFWjpcTqT8Nj4S8E"
        elif rank == 9:
            return "CAACAgUAAxkBAAEJm4ZkpeyjonqWXsIYxLrmpdnbZgOagwACNQEAAuQkwVVVg-Fo5xtXQi8E"
        elif rank == 10:
            return "CAACAgUAAxkBAAEJm4hkpeyugogPeik0CjELnKAcF7xpWgACUgEAAhlbwFV8m-J7WE21Ki8E"
        elif rank == 11:
            return "CAACAgUAAxkBAAEJm4pkpey57_Z1KYguCylkaT4h_NhGCgACTQEAAnHCyVW3tBaN5V6XEC8E"
        elif rank == 12:
            return "CAACAgUAAxkBAAEJm4xkpezHKv6OHQbB6E2l5B39Z-yC_gACuAEAArhlwFVXtlTiCEWnDS8E"
        elif rank == 13:
            return "CAACAgUAAxkBAAEJm45kpezRWxGpcgqY1BYRg5r6CihfkgACfgEAArn-wVWBh7R834WGzy8E"
        else:
            return "CAACAgUAAxkBAAEJm5BkpezbeDgmayw31whR3tGbXGNmdgACTAEAArlrwVUCjF9P-WDqbC8E"


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
    website(message)
    add_dictionary_to_json()


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
        play(message)
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
            return play(message)
        elif player.bet > player.currency:
            telegram_bot.send_message(message.chat.id,
                                      f"Your bet is <b>NOT</b> accepted!\nYour bet must be less or equal than your "
                                      f"balance!", parse_mode='html')
            return play(message)
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
