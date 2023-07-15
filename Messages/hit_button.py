import telebot

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


def hit(message, deck, list_of_players, player, result_of_game):
    """Function for initial hit"""
    player_card = deck.give_user_card(player)
    telegram_bot.send_message(message.chat.id, "Your next card is:")
    telegram_bot.send_sticker(message.chat.id, str(player_card))
    player_sum = player.counting_sum()

    if player_sum > 21:
        telegram_bot.send_message(message.chat.id, f'<b>Your final sum is - </b> {player_sum}',
                                  parse_mode='html')
        result_of_game.loser(message.chat.id, list_of_players)
