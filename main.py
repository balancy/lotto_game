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

    @property
    def card(self):
        return self.__card

    def get_card_for_print(self):
        return self.__name.center(22, '-') + '\n' + str(self.__card) + '-' * 22

    def __str__(self):
        return f'{self.__class__.__name__} <{self.__name}>'


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
    game_bag = Bag()
    player1 = Player('Computer1')
    player2 = Player('Computer2')
    player1_continues_game = True
    player2_continues_game = True
    step = 1

    while player1_continues_game and player2_continues_game:
        print(f'Step №{step}')
        print(f'Bag is {game_bag}')
        print(player1.get_card_for_print())
        print(player2.get_card_for_print())

        current_number = game_bag.pop()
        print(f'Current number is {current_number}')
        if current_number in player1.card:
            player1.card.cross_out(current_number)
        if current_number in player2.card:
            player2.card.cross_out(current_number)

        print()

        if player1.card.is_empty():
            player1_continues_game = False
        if player2.card.is_empty():
            player2_continues_game = False

        step += 1

    if not player1_continues_game and not player2_continues_game:
        print('It\'s a draw. Nobody wins.')
    elif not player1_continues_game:
        print(f'{player1} won the game!')
    else:
        print(f'{player2} won the game!')

    print(player1.get_card_for_print())
    print(player2.get_card_for_print())
