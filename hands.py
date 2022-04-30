"""
models a poker hand
"""
import cards as c

DEFAULT_HAND_SIZE = 5
DEFAULT_HANDS_PER_DECK = 10  # a standard deck of 52 cards would be able to create 10 hands of 5 cards


def deal(deck):
    """
    creates a hand of specified size from a deck
    :param deck: a deck of cards
    :return: a hand of cards
    """

    dealt_cards = []
    for index in range(DEFAULT_HAND_SIZE):
        dealt_cards.append(deck.pop(0))  # remove dealt cards and add to list
    return dealt_cards


def is_flush(hand):
    """
    checks if the card hand is a flush
    :param hand: a hand of 5 cards
    :return: True if all card suits match, False if not
    """
    first_suit = c.get_suit(hand[0])
    for card in hand:
        if first_suit != c.get_suit(card):
            return False
    return True


def is_pair(hand):
    """
    checks hand, iterates one pair at a time and tries all card combinations for pairs.
    if pair is found, returns True.
    :param hand: hand of cards (list)
    :return: True when a pair or three of a kind is detected
    """
    ranks = c.get_hand_ranks(hand)
    for card in range(len(ranks)):
        for card_compare in range(card + 1, (len(ranks))):
            if ranks[card] == ranks[card_compare]:
                return True
    return False


def is_two_pair(hand):
    """
    iterates through hand, determines if two pairs exist within the hand
    :param hand: a hand of cards
    :return: True if there is a two pair, four of a kind, or full house
    """
    if is_pair(hand):
        pairs = 0
        ranks = c.get_hand_ranks(hand)
        for card in range(len(ranks)):
            for card_compare in range(len(ranks) - card - 1):
                if ranks[card] == ranks[card + card_compare + 1]:
                    pairs += 1
                    ranks[card] = 'none'
                    ranks[card + card_compare + 1] = 'none1'
                    if pairs == 2:
                        return True
    return False
