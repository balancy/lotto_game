import pytest

from bag import Bag
from card import Card
from player import Player


class TestCard:
    """
    Tests card class.
    """

    def test_created_card_is_not_empty(self):
        card = Card()
        assert not card.is_empty()

    def test_created_card_contains_15_elements(self):
        card = Card()
        assert len(card) == 15

    @pytest.mark.parametrize("elm", [
        pytest.param(91, id="number 91"),
        pytest.param(0, id="number 0"),
        pytest.param(-1, id="negative number"),
    ])
    def test_no_elms_outside_of_range_in_created_instance(self, elm):
        card = Card()
        assert elm not in card


class TestBag:
    """
    Tests bag class.
    """

    def test_created_bag_is_full(self):
        bag = Bag()
        assert len(bag) == 90

    def test_element_pops_from_bag(self):
        bag = Bag()
        initial_size = len(bag)
        bag.pop()
        assert initial_size == len(bag) + 1


class TestPlayer:
    """
    Tests player class.
    """

    def test_created_player_is_playing(self):
        player = Player()
        assert player.is_playing

