"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    numerical_value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    face_cards = ['J', 'Q', 'K']
    if card in numerical_value:
        return int(card)
    elif card == 'A':
        #  [R1705 no-else-return]  Code smell
        return 1
    elif card in face_cards:
        return 10

    # if (card in 'JQK'): return 10 No need to create a list
    # if (card == 'A'): return 1
    # return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return (card_one, card_two)
    elif value_of_card(card_one) > value_of_card(card_two):
        return card_one
    else:
        return card_two

    # if (value_of_card(card_one) > value_of_card(card_two)): return card_one
    # if (value_of_card(card_one) < value_of_card(card_two)): return card_two
    # return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    bust_value = 21
    highest_ace_value = 11

    card_one_value = 11 if card_one == 'A' else value_of_card(card_one)
    card_two_value = 11 if card_two == 'A' else value_of_card(card_two)

    sum_cards_in_hand = card_one_value + card_two_value
    if sum_cards_in_hand + highest_ace_value > bust_value:
        return 1
    else:
        # [R1705 no-else-return]  ["Unnecessary "else" after "return"", "remove the "else" and de-indent the code inside it"] was reported by Pylint.
        return 11

    # if (card_one == 'A' or card_two == 'A'): return 1 if there is an 'A' in hand, the value is 11 so new 'A' can only by '1' to keep under bust value
    # return 11 if (value_of_card(card_one) + value_of_card(card_two) <= 10) else 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    return (card_one == 'A' and value_of_card(card_two) == 10) or (card_two == 'A' and value_of_card(card_one) == 10)

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    total_dealt = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= total_dealt <= 11
