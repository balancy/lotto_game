import random

MIN_VALUE = 1
MAX_VALUE = 90


class Bag:
    def __init__(self):
        self.__numbers = list(range(MIN_VALUE, MAX_VALUE + 1))

    def pop(self):
        return self.__numbers.pop(random.randint(0, len(self.__numbers) - 1))

    def __str__(self):
        return ' '.join(str(elm) for elm in self.__numbers)


class Player:
    def __init__(self, name):
        self.__name = name
        self.__card = Card()
        self.is_playing = True

    @property
    def card(self):
        return self.__card

    def get_card_for_print(self):
        return self.__name.center(22, '-') + '\n' + str(self.__card) + '-' * 22

    def analyse_current_number(self, item, action=1):
        if item in self.__card:
            self.__card.cross_out(item)

    def __str__(self):
        return self.__name


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def request_action(self):
        requested_action = input(
            f'Do {self} want to draw out the current number or to continue '
            f'(0 - continue, 1 - draw)? By default it\'s continue: ')
        return 1 if requested_action == '1' else 0

    def analyse_current_number(self, item, action=1):
        if not action and current_number in self.card:
            return f'{self} chose to continue while he has the number ' \
                   f'to cross out. He lose!'
        elif action and current_number not in self.card:
            return f'{self} chose to cross out the number while he hasn\'t ' \
                   f'it in his card. He lose!'

        if current_number in self.card:
            self.card.cross_out(item)


class Card:
    __total_number = 15
    __all_possible_values = list(range(MIN_VALUE, MAX_VALUE + 1))

    def __init__(self):
        self.__numbers = sorted(
            random.sample(self.__all_possible_values, self.__total_number)
        )

    def __contains__(self, item):
        return item in self.__numbers

    def is_empty(self):
        return not any(self.__numbers)

    def cross_out(self, item):
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


if __name__ == '__main__':
    mode = input('Enter the game mode (1 - human vs computer, 2 - human vs human, 3 - computer vs computer). '
                 'By default it\'s human vs computer: ')
    if mode == '2':
        player1 = HumanPlayer('Player 1')
        player2 = HumanPlayer('Player 2')
    elif mode == '3':
        player1 = Player('Computer 1')
        player2 = Player('Computer 2')
    else:
        player1 = HumanPlayer('Player')
        player2 = Player('Computer')

    game_bag = Bag()
    step = 1

    while player1.is_playing and player2.is_playing:
        print(f'Step №{step}')
        print(f'Bag is {game_bag}')

        for player in (player1, player2):
            print(player.get_card_for_print())

        current_number = game_bag.pop()
        print(f'Current number is {current_number}')

        for player in (player1, player2):
            if isinstance(player, HumanPlayer):
                action = player.request_action()
                result = player.analyse_current_number(current_number, action)
                if result:
                    print(result)
                    player.is_playing = False
            else:
                player.analyse_current_number(current_number)

        print()

        for player in (player1, player2):
            if player.card.is_empty():
                player.is_playing = False

        step += 1

    if not player1.is_playing and player1.card.is_empty() and \
            not player2.is_playing and player2.card.is_empty():
        print('It\'s a draw. Everybody wins.')
    elif not player1.is_playing and player1.card.is_empty():
        print(f'{player1} won the game!')
    elif not player2.is_playing and player2.card.is_empty():
        print(f'{player2} won the game!')

    for player in (player1, player2):
        print(player.get_card_for_print())
