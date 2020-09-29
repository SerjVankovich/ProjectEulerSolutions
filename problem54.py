SUITS = ['D', 'C', 'H', 'S']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, card):
        """

        :param card: list(Card)
        """
        self.value = card[0]
        self.suit = card[1]

    def __str__(self):
        return self.value + self.suit


def sort_values(cards):
    if len(cards) == 0:
        return []
    if len(cards) == 1:
        return cards
    middle = cards[len(cards) // 2]
    return sort_values(list(filter(lambda card: VALUES.index(card.value) < VALUES.index(middle.value), cards))) + [
        middle] + list(filter(lambda card: VALUES.index(card.value) == VALUES.index(middle.value) and
                                           card.suit != middle.suit, cards)) \
           + sort_values(list(filter(lambda card: VALUES.index(card.value) > VALUES.index(middle.value), cards)))


class PokerHand:
    def __init__(self, cards):
        self.cards = sort_values(cards)

    def high_card(self):
        return self.cards[-1]

    def has_pairs(self):
        pairs = []
        h_p = False
        for card in self.cards:
            if [x.value for x in self.cards].count(card.value) == 2:
                h_p = True
                pairs.append(list(filter(lambda c: VALUES.index(c.value) == VALUES.index(card.value), self.cards)))
        return h_p, pairs

    def has_triples(self):
        triples = []
        h_p = False
        for card in self.cards:
            if [x.value for x in self.cards].count(card.value) == 3:
                h_p = True
                triples.append(list(filter(lambda c: VALUES.index(c.value) == VALUES.index(card.value), self.cards)))
        return h_p, triples

    def has_care(self):
        h_p = False
        for card in self.cards:
            if [x.value for x in self.cards].count(card.value) == 4:
                h_p = True
                return h_p, list(filter(lambda c: VALUES.index(c.value) == VALUES.index(card.value), self.cards))
        return h_p, []

    def has_straight(self):
        card = VALUES.index(self.cards[0].value)
        for c in self.cards[1:]:
            index = VALUES.index(c.value)
            if index != card + 1:
                return False, -1
            card = index
        return True, VALUES.index(self.cards[-1].value)

    def has_flush(self):
        suits = [x.suit for x in self.cards]
        if suits.count(self.cards[0].suit) == 5:
            return True, VALUES.index(self.cards[-1].value)
        else:
            return False, -1

    def has_full_house(self):
        has_p, pairs = self.has_pairs()
        has_t, triples = self.has_triples()
        if has_p and has_t:
            return True, {
                'pairs': pairs[-1],
                'triples': triples[-1]
            }
        return False, {}

    def has_two_pairs(self):
        h_p, pairs = self.has_pairs()
        if h_p and len(pairs) == 4:
            return True, [pairs[0], pairs[-1]]
        return False, []

    def has_straight_flush(self):
        h_s, straight = self.has_straight()
        h_f, flush = self.has_flush()

        if h_s and h_f:
            return True, straight
        return False, -1

    def has_royal_flush(self):
        h_s, straight = self.has_straight()
        h_f, flush = self.has_flush()

        if h_s and h_f and straight == 'A':
            return True
        return False

    def analyze(self):
        has_royal = self.has_royal_flush()
        has_straight_flush, s_f_max_card = self.has_straight_flush()
        has_care, care_card = self.has_care()
        has_full_house, pairs_triples = self.has_full_house()
        has_flush, f_max_card = self.has_flush()
        has_straight, s_max_card = self.has_straight()
        has_triple, triple = self.has_triples()
        has_two_pairs, two_pairs = self.has_two_pairs()
        has_pairs, pairs = self.has_pairs()
        high_card = self.high_card()

        if has_royal:
            return 10, {'max': None, 'last': []}
        elif has_straight_flush:
            return 9, {'max': s_f_max_card, 'last': []}
        elif has_care:
            last = list(filter(lambda x: x.value != care_card[0].value, self.cards))
            return 8, {'max': VALUES.index(care_card[0].value), 'last': last}
        elif has_full_house:
            pair_max = VALUES.index(pairs_triples['pairs'][0].value)
            triple_max = VALUES.index(pairs_triples['triples'][0].value)
            return 7, {'max': max(pair_max, triple_max), 'last': []}
        elif has_flush:
            return 6, {'max': f_max_card, 'last': []}
        elif has_straight:
            return 5, {'max': s_max_card, 'last': []}
        elif has_triple:
            last = list(filter(lambda x: x.value != triple[0][0].value, self.cards))
            return 4, {'max': VALUES.index(triple[0][0].value), 'last': last}
        elif has_two_pairs:
            pair_1_max = VALUES.index(two_pairs[0][0].value)
            pair_2_max = VALUES.index(two_pairs[1][0].value)
            last = list(filter(lambda x: x.value != two_pairs[0][0].value and x.value != two_pairs[1][0].value,
                               self.cards))
            return 3, {'max': max(pair_1_max, pair_2_max), 'last': last}
        elif has_pairs:
            pair_max = VALUES.index(pairs[0][0].value)
            last = list(filter(lambda x: x.value != pairs[0][0].value, self.cards))
            return 2, {'max': pair_max, 'last': last}
        else:
            last = self.cards[:4]
            return 1, {'max': VALUES.index(high_card.value), 'last': last}


player_1_wins = 0
with open('p054_poker.txt') as file:
    for line in file:
        cards = line.split(' ')
        player_1 = PokerHand([Card(x) for x in cards[:5]])
        player_2 = PokerHand([Card(x) for x in cards[5:]])

        p_1_combo, p_1_obj = player_1.analyze()
        p_2_combo, p_2_obj = player_2.analyze()

        if p_1_combo > p_2_combo:
            player_1_wins += 1
        elif p_1_combo == p_2_combo:
            if p_1_obj['max'] > p_2_obj['max']:
                player_1_wins += 1
            elif p_1_obj['max'] == p_2_obj['max']:
                for i in reversed(range(len(p_1_obj['last']))):
                    if VALUES.index(p_1_obj['last'][i].value) > VALUES.index(p_2_obj['last'][i].value):
                        player_1_wins += 1
                        break
                    elif VALUES.index(p_1_obj['last'][i].value) < VALUES.index(p_2_obj['last'][i].value):
                        break
print(player_1_wins)
