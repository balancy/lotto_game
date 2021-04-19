from classes import Game


def main():
    """
    Main function that creates and handles lotto game.
    """

    mode = input('Enter the game mode (1 - human vs computer, '
                 '2 - human vs human, 3 - computer vs computer). '
                 'By default it\'s human vs computer: ')

    game = Game(mode)
    while game.is_continue():
        game.play_round()

    game.analyse_results()


if __name__ == '__main__':
    main()
