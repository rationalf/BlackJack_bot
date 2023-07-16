import telebot
from Commads.help_command import help_command
from Commads.play_command import play_command
from Commads.rules_command import rules_command
from Commads.start_command import start_command
from functions.get_player import get_player
from Classes.ResultOfGame import ResultOfGame
from Messages.hit_button import hit
from Messages.stand_button import stand
from functions import bet_handling

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


@telegram_bot.message_handler()
def get_user_text(message, deck, list_of_players):
    """command for handling the user's text"""
    if message.text == '/help':
        help_command(message)
        return
    if message.text == '/rules':
        rules_command(message)
        return
    if message.text == '/start':
        start_command(message)
        return
    if message.text == '/play':
        if play_command(message, deck, list_of_players):
            get_user_text(message, deck, list_of_players)
        else:
            return

    player = get_player(message.from_user.id, list_of_players)
    croupier = get_player(str(message.from_user.id) + message.from_user.username, list_of_players)
    result_of_game = ResultOfGame()

    if message.text == "Hit":
        hit(message, deck, list_of_players, player, result_of_game)
        return

    if message.text == "Stand":
        stand(message, deck, list_of_players, player, croupier, result_of_game)
        return

    if message.text == 'Start another game' or message.text == 'Start':
        """restarting the game"""
        play_command(message, deck, list_of_players)
        return

    if message.text == 'Stop playing':
        """stop playing"""
        bet_handling.resize_keyboard_start(message, player, list_of_players)
        return

    if message.text == 'Your balance - ' + str(get_player(message.from_user.id, list_of_players).currency):
        telegram_bot.send_message(message.chat.id,
                                  "5000 chips - 100 rubles\n"
                                  "10000 chips - 175 rubles\n"
                                  "50000 chips - 750 rubles\n"
                                  "\n"
                                  "To send money contact us on telegram:\n"
                                  "@GaaanG_Hooold_oooN\n"
                                  "@Sergey_Dzyuba\n"
                                  "\nTo get 1 000 000 chips for free, give us A's for the PP course :)")
        return

    if message.text.isdigit() and player.betIsEntered:

        player.betIsEntered = False

        if bet_handling.bet_handling(message, player, list_of_players):
            return

        bet_handling.resize_keyboard_hit_stand(message, list_of_players)

        deck.initial_distribution_of_cards(message, player, croupier, deck)

        result_of_game.define_result(message, player, croupier, deck, list_of_players)
    elif message.text.isdigit():
        telegram_bot.send_message(message.chat.id, "You are not allowed to enter a bet now!")
        telegram_bot.send_message(message.chat.id, "<strong>Have a look at available buttons!</strong>",
                                  parse_mode='html')
    else:
        telegram_bot.send_message(message.chat.id, "Bet must be a natural number")
