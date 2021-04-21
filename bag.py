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

    def __len__(self):
        return len(self.__numbers)




