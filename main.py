from game import Game


def request_user_input_data():
    """
    Requests user how many players will be playing.
    :return: number of players
    """

    players_number = input('Enter players number (by default it\'s 2): ')
    try:
        players_number = int(players_number)
    except ValueError:
        players_number = 2
    return players_number


def request_players_details(number):
    """
    Requests details about players. Will it be computer or human.
    :param number: number of players
    :return: list with players signatures
    """

    players_signatures = []
    for player in range(number):
        choice = input(
            f'Do you want Player {player + 1} to be human (0) or computer (1)?'
            f' By default it\'s computer: ')
        players_signatures.append(0 if choice == '0' else 1)

    return players_signatures


def main():
    """
    Main function that creates and handles lotto game.
    """

    players_number = request_user_input_data()
    players_signatures = request_players_details(players_number)

    game = Game(players_signatures)
    while game.is_continue():
        game.play_round()

    game.analyse_results()


if __name__ == '__main__':
    main()
