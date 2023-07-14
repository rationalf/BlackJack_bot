def get_player(id_of_user, list_of_players):
    for player in list_of_players:
        if player.id == id_of_user:
            return player
