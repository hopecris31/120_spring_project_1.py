"""
models a card
"""


def create_card(rank, suit):
    """
    takes the rank and suit of a card (string) and concatenates them to form a card
    :param rank: a letter or number (string)
    :param suit: a letter
    :return: card (string)
    """
    card = rank+suit
    return card


def get_rank(card):
    """
    :param card: a card (string) with a rank and suit
    :return: rank
    """
    if len(card) == 3:
        return card[0:2]
    else:
        return card[0]


def get_hand_ranks(hand):
    """
    gets the ranks of the cards in a hand
    :param hand: a hand
    :return: the ranks of the hand
    """
    hand_ranks = []
    for card in hand:
        rank = get_rank(card)
        hand_ranks.append(rank)
    return hand_ranks


def get_suit(card):
    """
    :param card: a card (string) with a rank and suit
    :return: suit
    """
    return card[-1]
