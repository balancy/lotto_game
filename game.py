from bag import Bag
from player import HumanPlayer, Player


class Game:
    """
    Represents lotto game
    """

    def __init__(self, *args):
        self.players = []
        for count, arg in enumerate(*args, start=1):
            if not arg:
                self.players.append(HumanPlayer(f'Player {count}'))
            else:
                self.players.append(Player(f'Computer {count}'))

        self.game_bag = Bag()
        self.round = 1

    def __print_player_cards(self):
        """
        Prints player cards.
        """

        for player in self.players:
            print(player.get_card_for_print())

    def __print_round_header(self):
        """
        Prints header of each round
        """

        print(f'Round №{self.round}')
        self.__print_player_cards()

    def __check_players_continue_playing(self):
        """
        Checks if both players continue the game.
        :return:
        """

        for player in self.players:
            if player.card.is_empty():
                player.is_playing = False

    def __make_players_play_round(self, current_number):
        """
        Makes both players play their round.
        :param current_number: current number from the bag
        """

        for player in self.players:
            if isinstance(player, HumanPlayer):
                action = player.request_action()
                result = player.analyse_current_number(current_number, action)
                if result:
                    print(result)
                    player.is_playing = False
            else:
                player.analyse_current_number(current_number)

    def is_continue(self):
        return all(player.is_playing for player in self.players)

    def play_round(self):
        """
        Executes all steps to play one round.
        """

        self.__print_round_header()

        current_number = self.game_bag.pop()
        print(f'Current number is {current_number}')

        self.__make_players_play_round(current_number)
        print()

        self.__check_players_continue_playing()
        self.round += 1

    def __str__(self):
        return \
            f'{self.__class__.__name__} with {len(self.players)} players'

    def analyse_results(self):
        """
        Analyses results and print them out.
        """

        if not any(player.is_playing for player in self.players) \
                and all(player.card.is_empty() for player in self.players):
            print('It\'s a draw. Everybody wins.')
        else:
            for player in self.players:
                if not player.is_playing and player.card.is_empty():
                    print(f'{player} won the game!')

        self.__print_player_cards()
