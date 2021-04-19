import random

MIN_VALUE = 1
MAX_VALUE = 90


class Bag:
    """
    Represents a bag for lotto game.
    """

    def __init__(self):
        self.__numbers = list(range(MIN_VALUE, MAX_VALUE + 1))

    def pop(self):
        """
        Pops random element from the bag.
        :return: random element
        """

        return self.__numbers.pop(random.randint(0, len(self.__numbers) - 1))

    def __str__(self):
        return ' '.join(str(elm) for elm in self.__numbers)


class Player:
    """
    Represents computer player.
    """

    def __init__(self, name):
        self.__name = name
        self.__card = Card()
        self.is_playing = True

    @property
    def card(self):
        return self.__card

    def get_card_for_print(self):
        """
        Gets player's lotto card for printed format.
        :return: card for printed format
        """

        return self.__name.center(22, '-') + '\n' + str(self.__card) + '-' * 22

    def analyse_current_number(self, item, action=1):
        """
        Analyses if given number is in the player's lotto card.
        :param item: given number
        :param action: will be used in child classes
        """

        if item in self.__card:
            self.__card.cross_out(item)

    def __str__(self):
        return self.__name


class HumanPlayer(Player):
    """
    Represents human player.
    """

    def __init__(self, name):
        super().__init__(name)

    def request_action(self):
        """
        Requests action to perform from user.
        :return: action signature
        """

        requested_action = input(
            f'Do {self} want to draw out the current number or to continue '
            f'(0 - continue, 1 - draw)? By default it\'s continue: ')
        return 1 if requested_action == '1' else 0

    def analyse_current_number(self, item, action=1):
        """
        Analyses if given number is in the player's lotto card
        taken action into account.
        :param item: given number
        :param action: analyses action chosen by user
        :return: None or string if action doesn't correspond to rules
        """

        if not action and item in self.card:
            return f'{self} chose to continue while he has the number ' \
                   f'to cross out. He lose!'
        elif action and item not in self.card:
            return f'{self} chose to cross out the number while he hasn\'t ' \
                   f'it in his card. He lose!'

        if item in self.card:
            self.card.cross_out(item)


class Card:
    """
    Lotto card of numbers.
    """

    __total_number = 15
    __all_possible_values = list(range(MIN_VALUE, MAX_VALUE + 1))

    def __init__(self):
        self.__numbers = sorted(
            random.sample(self.__all_possible_values, self.__total_number)
        )

    def __contains__(self, item):
        return item in self.__numbers

    def is_empty(self):
        """
        Checks if card is empty.
        :return: if card is empty
        """

        return not any(self.__numbers)

    def cross_out(self, item):
        """
        Crosses out the number from the card.
        :param item: number
        """

        item_index = self.__numbers.index(item)
        self.__numbers[item_index] = 0

    def __str__(self):
        returned_string = ''

        for line_number in range(3):
            elms_in_line = self.__numbers[
                           line_number: line_number + self.__total_number: 3]
            returned_string += '   '.join(
                f'{elm:02}' if elm else ' -' for elm in elms_in_line
            ) + '\n'

        return returned_string


class Game:
    """
    Represents lotto game
    """

    def __init__(self, mode):
        if mode == '2':
            self.player1 = HumanPlayer('Player 1')
            self.player2 = HumanPlayer('Player 2')
        elif mode == '3':
            self.player1 = Player('Computer 1')
            self.player2 = Player('Computer 2')
        else:
            self.player1 = HumanPlayer('Player')
            self.player2 = Player('Computer')

        self.game_bag = Bag()
        self.round = 1

    def __print_player_cards(self):
        """
        Prints player cards.
        """

        for player in (self.player1, self.player2):
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

        for player in (self.player1, self.player2):
            if player.card.is_empty():
                player.is_playing = False

    def __make_players_play_round(self, current_number):
        """
        Makes both players play their round.
        :param current_number: current number from the bag
        """

        for player in (self.player1, self.player2):
            if isinstance(player, HumanPlayer):
                action = player.request_action()
                result = player.analyse_current_number(current_number, action)
                if result:
                    print(result)
                    player.is_playing = False
            else:
                player.analyse_current_number(current_number)

    def is_continue(self):
        return self.player1.is_playing and self.player2.is_playing

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
            f'{self.__class__.__name__} with {self.player1} and {self.player2}'

    def analyse_results(self):
        """
        Analyses results and print them out.
        """

        if not self.player1.is_playing \
                and self.player1.card.is_empty() \
                and not self.player2.is_playing \
                and self.player2.card.is_empty():
            print('It\'s a draw. Everybody wins.')
        elif not self.player1.is_playing \
                and self.player1.card.is_empty():
            print(f'{self.player1} won the game!')
        elif not self.player2.is_playing \
                and self.player2.card.is_empty():
            print(f'{self.player2} won the game!')

        self.__print_player_cards()
