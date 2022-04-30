"""
models a deck of cards
"""
import random
import cards

HAND_SIZE = 5
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
SUITS = ['H', 'D', 'C', 'S']


def create_deck():
    """
    creates a deck of cards by combining one of each rank and suit
    :return: deck of 52 cards as list
    """
    deck = []
    for i in range(len(RANKS)):
        for j in range(len(SUITS)):
            card = cards.create_card(RANKS[i], SUITS[j])
            deck.append(card)
    return deck


def shuffle(deck):
    """
    shuffles a deck of cards
    :return: the shuffled deck of cards as a list
    """

    random.shuffle(deck)
    return deck


def enough_in_deck(deck):
    """
    checks if there are enough cards in the deck to make another hand
    :param deck: a list of cards
    :return: True or False, depending of if there are enough cards
    """
    if len(deck) >= HAND_SIZE:
        enough = True
    else:
        enough = False
    return enough
