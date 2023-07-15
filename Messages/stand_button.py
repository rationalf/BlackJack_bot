import telebot

telegram_bot = telebot.TeleBot('6071571860:AAFch9-DHyN7EZ8zZUQRk5aM50u-ZD05cgs')


def stand(message, deck, list_of_players, player, croupier, result_of_game):
    """Function for ending game"""
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