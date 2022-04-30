"""
main, runs the game
"""

# should not start a new increment of 10,000 each round, but should add on to each other

import deck as d
import hands as h

INCREMENT_SIZE = 10000
ITERATION_TOTAL = 10000
ITERATION_LIMIT = 100000
COLUMN_COUNT = 10


def deal_round(num_rounds):
    """
    creates deck, makes hands
    :param num_rounds: number of rounds that will be played (100k)
    :return: the hands specified for the number of rounds
    """
    list_of_hands = []
    deck = d.shuffle(d.create_deck())  # creates and shuffles deck
    for i in range(num_rounds):
        if d.enough_in_deck(deck):  # if there are enough cards in deck to make hand
            list_of_hands.append(check_hand_type(h.deal(deck)))  # checks and adds the hand type to the list
        else:
            deck = d.shuffle(d.create_deck())  # if not enough cards for new deck, create new deck
            list_of_hands.append(check_hand_type(h.deal(deck)))  # checks and adds hand type and adds to list
    return list_of_hands  # list of all hand types from test hands


def check_hand_type(hand):
    """
    :param hand: a hand of 5 cards
    :return: the type of hand it is
    """

    if h.is_flush(hand):
        return 'Flush'
    elif h.is_two_pair(hand):
        return 'Two Pair'
    elif h.is_pair(hand):
        return 'Pair'
    else:
        return 'High Card'


def hand_counter(hands_list):
    """
    counts the occurrences of each hand from a round
    :param hands_list: a list of hands
    :return: list of the counts of all the hands
    """
    flushes = hands_list.count('Flush')
    two_pairs = hands_list.count('Two Pair')
    pairs = hands_list.count('Pair')
    high_cards = hands_list.count('High Card')

    return [pairs, two_pairs, flushes, high_cards]


def find_percent(hand_counter_list, hand_counter_list_index, interval):
    """
    finds percent chance of a hand occurrence
    :param hand_counter_list: the list with the number of hand occurences
    :param hand_counter_list_index: the index of the hand count you want to access
    :param interval: number of hands to be tested
    :return: the percent of hand occurrences
    """
    percent = (hand_counter_list[hand_counter_list_index]/interval)*100
    return percent


def table_display(iteration_total, iteration_limit, columns):
    """
    creates a table for the percent chances of all hands
    :return: a table with
    """

    header = '# of hands    pairs   %         2 pairs   %         flushes   %         high card   %'
    print(header)

    for interval in range(columns):
        create_round = deal_round(iteration_total)  # creates a deck and number of specified hands (10k)
        hand_counts = hand_counter(create_round)
        find_percent(hand_counts, 0, iteration_limit)

        num_pairs = hand_counts[0]
        percent_pairs = find_percent(hand_counts, 0, iteration_total)

        num_two_pairs = hand_counts[1]
        percent_two_pairs = find_percent(hand_counts, 1, iteration_total)

        num_flushes = hand_counts[2]
        percent_flushes = find_percent(hand_counts, 2, iteration_total)

        num_high_cards = hand_counts[3]
        percent_high_cards = find_percent(hand_counts, 3, iteration_total)

        print("{:,}".format(iteration_total), '    ',
              "{:}".format(num_pairs), ' ', "{:.2f}".format(percent_pairs), '       '
              "{:}".format(num_two_pairs), '  ', "{:.2f}".format(percent_two_pairs), '        '
              "{:}".format(num_flushes), '  ', "{:.2f}".format(percent_flushes), '     ',
              num_high_cards, '   ', "{:.2f}".format(percent_high_cards))

        if iteration_total < iteration_limit:
            iteration_total += 10000


def play_rounds():
    """
    starts the entire program
    :return:
    """
    return table_display(ITERATION_TOTAL, ITERATION_LIMIT, COLUMN_COUNT)


if __name__ == "__main__":
    play_rounds()
