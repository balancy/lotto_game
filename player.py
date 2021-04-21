from card import Card


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

        return f'{self.__name.center(22, "-")}\n{self.__card}{"-" * 22}'

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
            return (f'{self} chose to continue while he has the number '
                    f'to cross out. He lose!')
        elif action and item not in self.card:
            return (f'{self} chose to cross out the number while he hasn\'t '
                    f'it in his card. He lose!')

        if item in self.card:
            self.card.cross_out(item)
