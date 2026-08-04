import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suit
                                      for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    

def spades_high(card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    deck = FrenchDeck()
    print(f"beer_card: {beer_card}")
    print(f"len(FrenchDeck()): {len(deck)}")
    print(f"first card: {deck[0]}")
    print(f"last card: {deck[-1]}")

    print("some random cards:")
    from random import choice 
    for i in range(3):
        print(choice(deck))

    print(f"from card 3 to 7: {deck[3:8]}")
    print(f"all the Aces: {deck[12::13]}")

    # check the card existance
    print(f"ace of spades in deck: {Card('A', 'spades') in deck}")
    print(f"joker of spades in deck: {Card('7', 'beasts') in deck}")

    print(f"sorted by rank: {sorted(deck, key=spades_high)}")