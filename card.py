import random

MIN_VALUE = 1
MAX_VALUE = 90


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

    def __len__(self):
        return len(self.__numbers)
