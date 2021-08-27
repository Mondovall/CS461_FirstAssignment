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

    def shuffle_cards(self):
        for i in range(len(self.cards) -1, 0, -1):
            random_card = random.randint(0, i)
            self.cards[i], self.cards[random_card] = self.cards[random_card], self.cards[i]


    def deal_cards(self):
        return self.cards.pop()




class Player:

    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw_cards(self, deck):
        for i in range(0, 13):
            self.hand.append(deck.deal_cards())
        return self.hand

    def show_hand(self):
        for i in self.hand:
            print(i.value, i.suit, "\n")


class Points(Deck):
    def __init__(self, player):
        self.player = player


deck = Deck()
deck.shuffle_cards()
player1 = Player("Player1")
player1.draw_cards(deck)

player1.show_hand()









