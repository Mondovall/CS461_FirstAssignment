import random
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Deck:
    def __init__(self):
        self.cards = []
        self.make_deck()

    def make_deck(self):
        for i in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for j in range(1, 14):
                if j == 1:
                    self.cards.append(Card("A", i))
                elif j == 11:
                    self.cards.append(Card("J", i))
                elif j == 12:
                    self.cards.append(Card("Q", i))
                elif j == 13:
                    self.cards.append(Card("K", i))
                else:
                    self.cards.append(Card(str(j), i))

    def print_deck(self):
        for i in self.cards:
            print(i.value, " of ", i.suit)


deck = Deck()
deck.print_deck()




