from functools import cmp_to_key
from enum import Enum

class Quality(Enum):
    NOTHING = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    def __int__(self):
        return self.value

class Hand:
    def __init__(self, cards_string, bet):
        self.cards = list(cards_string)
        self.bet = int(bet)
        self.initialize_quality()
    
    def initialize_quality(self):
        quantities_list = []
        jokers_count = len([x for x in self.cards if x == "J"])
        for unique_card in set(self.cards):
            if unique_card != "J":
                quantities_list.append(len([x for x in self.cards if x == unique_card]))
        quantities_list.sort(reverse=True)
        if len(quantities_list) == 0: # special case for JJJJJ
            quantities_list.append(0)
        quantities_list[0] += jokers_count
        if quantities_list[0] == 5:
            self.quality = Quality.FIVE_OF_A_KIND
        elif quantities_list[0] == 4:
            self.quality = Quality.FOUR_OF_A_KIND
        elif quantities_list[0] == 3:
            if quantities_list[1] == 2:
                self.quality = Quality.FULL_HOUSE
            else:
                self.quality = Quality.THREE_OF_A_KIND
        elif quantities_list[0] == 2:
            if quantities_list[1] == 2:
                self.quality = Quality.TWO_PAIR
            else:
                self.quality = Quality.PAIR
        else:
            self.quality = Quality.NOTHING

def evaluate_card(card):
    if (card == "T"):
        return 10
    elif (card == "J"):
        return 1 # it's the worst now
    elif (card == "Q"):
        return 12
    elif (card == "K"):
        return 13
    elif (card == "A"):
        return 14
    else:
        return int(card)

def compare_hands(hand1, hand2):
    if int(hand1.quality) < int(hand2.quality):
        return -1
    elif int(hand1.quality) > int(hand2.quality):
        return 1
    else:
        for i in range(5):
            card_evaluation = evaluate_card(hand1.cards[i]) - evaluate_card(hand2.cards[i])
            if card_evaluation != 0:
                return card_evaluation / abs(card_evaluation)

fstream = open("input.txt", 'r')
line = fstream.readline()
hands = []
while line:
    (cards, bet) = line.split()
    hands.append(Hand(cards, bet))
    line = fstream.readline()

hands.sort(key=cmp_to_key(compare_hands))
running_total = 0
for (index, hand) in enumerate(hands, start=1):
    running_total += index * hand.bet
print(running_total)